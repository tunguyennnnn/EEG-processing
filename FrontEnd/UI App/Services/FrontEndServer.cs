using System.Threading.Tasks;
using System.Windows;
using Grpc.Core;

using Interop;

using SimulationApp.Models;
using SimulationApp.ViewModels;


namespace SimulationApp.Services
{
    public class FrontEndServer
    {
        private const int Port = 50051;
        private readonly Server _server;

        public FrontEndServer(TrainingVM vm)
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
        private readonly TrainingVM _vm;

        public FrontEndImpl(TrainingVM vm)
        {
            _vm = vm;
        }

        public override Task<StatusReply> ExecuteMentalCommand(CommandRequest request, ServerCallContext context)
        {
            var command = (DroneCommand) request.CommandType;

            Application.Current?.Dispatcher?.Invoke(() => _vm.ExecuteDroneCommand(DroneCommand.Reset));
            Application.Current?.Dispatcher?.Invoke(() => _vm.ExecuteDroneCommand(command));

            return Task.FromResult(new StatusReply() { Code = 0 });
        }
    }
}
