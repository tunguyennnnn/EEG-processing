using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Windows.Input;

using SimulationApp.Models;
using SimulationApp.Services;
using SimulationApp.Utilities;


namespace SimulationApp.ViewModels
{
    public class TrainingVM : ViewModelBase, IDisposable
    {
        public TrainingVM()
        {
            _server = new FrontEndServer(this);
            _server.Start();

            _client = new BackEndClient();

            // Create default user proifle
            ActiveProfile = new UserProfile("tu") {CommandList = new List<DroneCommand>() {DroneCommand.MoveUp, DroneCommand.MoveDown} };
        }

        #region Properties

        public bool IsTrainingInProgress
        {
            get { return _isTrainingInProgress; }
            set { SetValue(ref _isTrainingInProgress, value); }
        }

        public UserProfile ActiveProfile
        {
            get { return _activeProfile; }
            set { SetValue(ref _activeProfile, value); }
        }

        #endregion

        #region Commands

        public ICommand TrainCommand => new DelegateCommand<DroneCommand>(StartTraining);
        public ICommand TrainClassifierCommand => new DelegateCommand(TrainClassifier);

        #endregion

        #region Events

        public delegate void CommandTrigerredHandler(DroneCommand droneCommand);
        public event CommandTrigerredHandler DroneCommandTriggered;

        #endregion

        #region Public Methods

        public void ExecuteDroneCommand(DroneCommand droneCommand)
        {
            DroneCommandTriggered?.Invoke(droneCommand);
        }

        public void Dispose()
        {
            _server.Stop();
        }

        #endregion

        #region Helper Methods

        private void StartTraining(DroneCommand command)
        {
            IsTrainingInProgress = true;

            Task.Run(() =>
            {
                _client.AcquireDataForCommand(ActiveProfile.Username, command);
                StopTraining();
            });
        }

        private void StopTraining()
        {
            IsTrainingInProgress = false;
        }

        private void TrainClassifier()
        {
            IsTrainingInProgress = true;

            Task.Run(() =>
            {
                _client.TrainClassifier(ActiveProfile.Username, ActiveProfile.CommandList);
                StopTraining();
                _client.RecognizeCommands(ActiveProfile.Username);
            });
        }

        #endregion

        #region Private Variables

        private readonly FrontEndServer _server;
        private readonly BackEndClient _client;
        private bool _isTrainingInProgress;

        private UserProfile _activeProfile;

        #endregion
    }
}
