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

        public void ResetDataForCommand(string username, DroneCommand command)
        {
            var request = new ResetDataRequest { Username = username, Command = (CommandType)command };

            try
            {
                var status = _client.ResetDataForCommand(request);
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

        public void StopRecognition()
        {
            var request = new EmptyRequest();

            try
            {
                var status = _client.StopRecognizion(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }

        public void CreateUserProfile(string username)
        {
            var request = new UserProfileOperationRequest() {Username = username};

            try
            {
                var status = _client.CreateUserProfile(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }


        public void DeleteUserProfile(string username)
        {
            var request = new UserProfileOperationRequest() { Username = username };

            try
            {
                var status = _client.DeleteUserProfile(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }


        public Dictionary<DroneCommand, int> GetUserProfile(string username)
        {
            var request = new UserProfileOperationRequest() { Username = username };

            try
            {
                var profileDataReply = _client.GetUserProfile(request);

                var commandSampleMap = new Dictionary<DroneCommand, int>();

                foreach(var commandPair in profileDataReply.ProfileData)
                {
                    var commandType = (DroneCommand) commandPair.Key;
                    commandSampleMap[commandType] = commandPair.Value;
                }

                return commandSampleMap;
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
                return null;
            }
        }

        public Dictionary<string, Dictionary<DroneCommand, int>> GetUserProfiles()
        {
            var request = new EmptyRequest();

            try
            {
                var profilListReply = _client.GetUserProfiles(request);

                var profileMap = new Dictionary<string, Dictionary<DroneCommand, int>>();

                foreach (var profilePair in profilListReply.ProfileList)
                {
                    var commandMap = new Dictionary<DroneCommand, int>();

                    foreach (var commandPair in profilePair.Value.ProfileData)
                    {
                        var commandType = (DroneCommand)commandPair.Key;
                        commandMap[commandType] = commandPair.Value;
                    }

                    var username = profilePair.Key;
                    profileMap[username] = commandMap;
                }

                return profileMap;
            }
            catch (Grpc.Core.RpcException e)
            {
                if (e.Message.Contains("StatusCode=Unavailable"))
                {
                    Dialog.ShowMessageBox("Error", "BackEnd Unavailable");
                }
                else
                {
                    Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
                }
               
                return new Dictionary< string, Dictionary <DroneCommand, int>> ();
            }
        }

        public void UpdateSensorData(int[] sensorData)
        {
            var request = new UpdateSensorDataRequest();
            request.SensorData.AddRange(sensorData);

            try
            {
                var status = _client.UpdateSensorData(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }

        public void DroneTakeoff()
        {
            var request = new EmptyRequest();

            try
            {
                var status = _client.DroneTakeoff(request);
            }
            catch (Grpc.Core.RpcException e)
            {
                Dialog.ShowMessageBox("Error", "Exception on the callee side: " + e.Message);
            }
        }

        public void DroneLand()
        {
            var request = new EmptyRequest();

            try
            {
                var status = _client.DroneLand(request);
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
