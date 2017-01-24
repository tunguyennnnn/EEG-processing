using System.Collections.Generic;
using System.Linq;

using Grpc.Core;

using Interop;
using Client = Interop.BackEnd.BackEndClient;

using SimulationApp.Models;
using SimulationApp.Utilities;

namespace SimulationApp.Services
{
    public class BackEndClient
    {
        public BackEndClient()
        {
            _channel = new Channel("127.0.0.1:50052", ChannelCredentials.Insecure);
            _client = new Client(_channel);      
        }

        public void StopClient()
        {
            _channel.ShutdownAsync().Wait();
        }

        public void AcquireDataForCommand(string username, DroneCommand command)
        {
            var request = new AquireDataRequest { Username = username, Command = (CommandType) command };

            try
            {
                var status = _client.AcquireDataForCommand(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }

        public void TrainClassifier(string username, IEnumerable<DroneCommand> commandList)
        {
            var request = new TrainClassifierRequest { Username = username};
            request.CommandList.AddRange(commandList.Cast<CommandType>());

            try
            {
                var status = _client.TrainClassifier(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }

        public void RecognizeCommands(string username)
        {
            var request = new RecognizeCommandsRequest { Username = username };

            try
            {
                var status = _client.RecognizeCommands(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }

        private readonly Channel _channel;
        private readonly Client _client;
    }
}
