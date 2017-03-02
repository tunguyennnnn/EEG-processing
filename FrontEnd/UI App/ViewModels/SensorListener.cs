using SimulationApp.Services;
using System;
using System.Linq;
using Windows.Devices.Bluetooth.GenericAttributeProfile;
using Windows.Devices.Enumeration;
using Windows.Storage.Streams;

namespace SimulationApp.ViewModels
{
    class SensorListener
    {
        BackEndClient _client;

        public SensorListener(BackEndClient client)
        {
            _client = client;
            ConnectToSensor();
        }

        public async void ConnectToSensor()
        {
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
            }
        }

        private GattCharacteristic _characteristic = null;

        public void OnReceive(GattCharacteristic sender, GattValueChangedEventArgs eventArgs)
        {
            byte[] bArray = new byte[eventArgs.CharacteristicValue.Length];
            DataReader.FromBuffer(eventArgs.CharacteristicValue).ReadBytes(bArray);

            int[] bytesAsInts = bArray.Select(x => (int)x).ToArray();

            _client.UpdateSensorData(bytesAsInts);
        }
    }
}
