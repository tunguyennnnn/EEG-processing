using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Threading.Tasks;
using System.Windows.Input;

using SimulationApp.Controls;
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
            
            MockUserProfiles();
        }

        // TODO: Remove mocking as soon as the actual API is built
        public void MockUserProfiles()
        {
            var tu = new UserProfileVM("tu", new List<DroneCommand>() { DroneCommand.MoveUp, DroneCommand.MoveDown });
            var jin = new UserProfileVM("jin", new List<DroneCommand>() { DroneCommand.MoveForward, DroneCommand.MoveBack });
            var katherine = new UserProfileVM("katherine", new List<DroneCommand>() { DroneCommand.TurnRight, DroneCommand.TurnLeft });

            UserProfiles.Add(tu);
            UserProfiles.Add(jin);
            UserProfiles.Add(katherine);

            ActiveProfile = UserProfiles[0];
        }

        #region Properties

        public bool IsTrainingInProgress
        {
            get { return _isTrainingInProgress; }
            set { SetValue(ref _isTrainingInProgress, value); }
        }

        public ObservableCollection<UserProfileVM> UserProfiles { get; } = new ObservableCollection<UserProfileVM>();

        public UserProfileVM ActiveProfile
        {
            get { return _activeProfileVM; }
            set { SetValue(ref _activeProfileVM, value); }
        }

        #endregion

        #region Commands

        public ICommand TrainCommand => new DelegateCommand<DroneCommand>(StartTraining);
        public ICommand TrainClassifierCommand => new DelegateCommand(TrainClassifier);

        public ICommand AddUserProfileCommand => new DelegateCommand(AddUserProfile);
        public ICommand DeleteActiveProfileCommand => new DelegateCommand(DeleteActiveProfile);

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
                _client.TrainClassifier(ActiveProfile.Username, ActiveProfile.ActiveCommands);
                StopTraining();
                _client.RecognizeCommands(ActiveProfile.Username);
            });
        }

        private void AddUserProfile()
        {
            var profileCreationDialog = new ProfileCreationDialog();
          
            if (Dialog.ShowDialog("New Profile", profileCreationDialog))
            {
                var username = profileCreationDialog.Username;

                if (!string.IsNullOrEmpty(username))
                {
                    var profile = new UserProfileVM(username);
                    UserProfiles.Add(profile);
                    ActiveProfile = profile;
                }
                else
                {
                    Dialog.ShowMessageBox("Error", "Username cannot be empty");
                }
            }
        }

        private void DeleteActiveProfile()
        {
            if (UserProfiles.Count > 1)
            {
                UserProfiles.Remove(ActiveProfile);
                ActiveProfile = UserProfiles[0];
            }
            else
            {
                Dialog.ShowMessageBox("Error", "Cannot delete last profile");
            }
        }

        #endregion

        #region Private Variables

        private readonly FrontEndServer _server;
        private readonly BackEndClient _client;
        private bool _isTrainingInProgress;

        private UserProfileVM _activeProfileVM;

        #endregion
    }
}
