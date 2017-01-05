using System.Threading.Tasks;
using System.Windows;
using Interop;
using Grpc.Core;
using SimulationApp.Models;
using SimulationApp.ViewModels;


namespace SimulationApp
{
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

            Application.Current?.Dispatcher?.Invoke(() => _vm.ExecuteDroneCommand(command));

            return Task.FromResult(new StatusReply() { Code = 0 });
        }
    }

    public class FrontEndServer
    {
        private const int Port = 50051;
        private Server server;

        public FrontEndServer(TrainingVM vm)
        {
            server = new Server
            {
                Services = { FrontEnd.BindService(new FrontEndImpl(vm)) },
                Ports = { new ServerPort("localhost", Port, ServerCredentials.Insecure) }
            };
        }

        public void Start()
        {
            server.Start();
        }

        public void Stop()
        {
            server.ShutdownAsync().Wait();
        }
    }
}
