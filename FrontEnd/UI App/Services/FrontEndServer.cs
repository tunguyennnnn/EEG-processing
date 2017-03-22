using System.Threading.Tasks;
using System.Windows;
using Grpc.Core;

using Interop;

using SimulationApp.Models;
using SimulationApp.ViewModels;
using System.Collections.Generic;
using System.Linq;

namespace SimulationApp.Services
{
    public class FrontEndServer
    {
        private const int Port = 50051;
        private readonly Server _server;

        public FrontEndServer(MainVM vm)
        {
            _server = new Server
            {
                Services = { FrontEnd.BindService(new FrontEndImpl(vm)) },
                Ports = { new ServerPort("localhost", Port, ServerCredentials.Insecure) }
            };
        }

        public void Start()
        {
            _server.Start();
        }

        public void Stop()
        {
            _server.ShutdownAsync().Wait();
        }
    }

    public class FrontEndImpl : FrontEnd.FrontEndBase
    {
        private readonly TrainingVM _trainingVM;
        private readonly GraphVM _graphVM;

        public FrontEndImpl(MainVM vm)
        {
            _trainingVM = vm.Training;
            _graphVM = vm.Graph;
        }

        public override Task<StatusReply> ExecuteMentalCommand(CommandRequest request, ServerCallContext context)
        {
            var command = (DroneCommand) request.CommandType;

            Application.Current?.Dispatcher?.Invoke(() => _trainingVM.ExecuteDroneCommand(DroneCommand.Reset));
            Application.Current?.Dispatcher?.Invoke(() => _trainingVM.ExecuteDroneCommand(command));

            return Task.FromResult(new StatusReply() { Code = 0 });
        }

        public override Task<StatusReply> UpdateBCIData(BCIDataRequest request, ServerCallContext context)
        {
            var dataArray = request.BCIData;

            var BCIData = new List<IList<double>>();
            
            foreach(var channelData in dataArray)
            {
                var channelDataDouble = channelData.Values.Select(v => (double)v).ToList();
                BCIData.Add(channelDataDouble);
            }

            _graphVM.OnGraphPointReceived(BCIData);
  
            return Task.FromResult(new StatusReply() { Code = 0 });
        }
    }
}
