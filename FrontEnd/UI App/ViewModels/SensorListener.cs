using SimulationApp.Services;
using System;
using System.Linq;
using System.Threading.Tasks;
using Windows.Devices.Bluetooth.GenericAttributeProfile;
using Windows.Devices.Enumeration;
using Windows.Storage.Streams;

namespace SimulationApp.ViewModels
{
    class SensorListener
    {
        private BackEndClient _client;
        private TrainingVM _vm;

        public SensorListener(TrainingVM vm, BackEndClient client)
        {
            _client = client;
            _vm = vm;
        }

        public async Task<bool> TryConnectToSensor()
        {
            // Disconnect if already connected
            if(_characteristic != null)
            {
                _characteristic.ValueChanged -= OnReceive;
            }

            var service_guid = new Guid("0000ffe0-0000-1000-8000-00805f9b34fb");
            var gatt_devices = await DeviceInformation.FindAllAsync(GattDeviceService.GetDeviceSelectorFromUuid(service_guid), null);
            var gatt_devicesConverted = gatt_devices.ToList();

            if(gatt_devicesConverted.Count > 0)
            {
                GattDeviceService service = await GattDeviceService.FromIdAsync(gatt_devicesConverted[0].Id);

                var characteristics = service.GetAllCharacteristics().ToList();

                var characteristic = characteristics.First();
                characteristic.ValueChanged += OnReceive;

                _characteristic = characteristic;

                var descriptorValue = GattClientCharacteristicConfigurationDescriptorValue.Notify;
                await characteristic.WriteClientCharacteristicConfigurationDescriptorAsync(descriptorValue);

                return true;
            }

            return false;
        }

        private GattCharacteristic _characteristic = null;

        public bool SensorNotificationEnabled { get; set; } = false;

        public void OnReceive(GattCharacteristic sender, GattValueChangedEventArgs eventArgs)
        {
            byte[] bArray = new byte[eventArgs.CharacteristicValue.Length];
            DataReader.FromBuffer(eventArgs.CharacteristicValue).ReadBytes(bArray);

            int[] bytesAsInts = bArray.Select(x => (int)x).ToArray();

            try
            {
                _vm.UpdateSensorData(bytesAsInts);
                if (SensorNotificationEnabled) _client.UpdateSensorData(bytesAsInts);
            }
            catch
            {
                bytesAsInts = new int[] {0,0,0,0};
                _vm.UpdateSensorData(bytesAsInts);
                if (SensorNotificationEnabled) _client.UpdateSensorData(bytesAsInts);
            }
        }
    }
}
