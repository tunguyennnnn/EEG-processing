using System;
using System.Collections.ObjectModel;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
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

            _sensorListener = new SensorListener(this, _client);
            _sensorListener.TryConnectToSensor();
            
            LoadUserProfiles();
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

        public string EnableSensor
        {
            get { return _enableSensor; }
            set { SetValue(ref _enableSensor, value); }
        }

        public string LockSensor
        {
            get { return _lockSensor; }
            set { SetValue(ref _lockSensor, value); }
        }

        public string ModeSensor
        {
            get { return _modeSensor; }
            set { SetValue(ref _modeSensor, value); }
        }

        private string _enableSensor = "Off";
        private string _lockSensor = "Off";
        private string _modeSensor = "Forward/Backward";

        public string ToggleRecognitionLabel
        {
            get { return _toggleRecognitionLabel; }
            set { SetValue(ref _toggleRecognitionLabel, value); }
        }

        private string _toggleRecognitionLabel = "Start Recognition";

        #endregion

        #region Commands

        public ICommand TrainCommand => new DelegateCommand<DroneCommand>(StartTraining);
        public ICommand ResetCommand => new DelegateCommand<DroneCommand>(ResetCommandData);
        public ICommand TrainClassifierCommand => new DelegateCommand(TrainClassifier);
        public ICommand ToggleRecognitionCommand => new DelegateCommand(ToggleRecognition);

        public ICommand AddUserProfileCommand => new DelegateCommand(AddUserProfile);
        public ICommand DeleteActiveProfileCommand => new DelegateCommand(DeleteActiveProfile);

        public ICommand DroneTakeoffCommand => new DelegateCommand(DroneTakeoff);
        public ICommand DroneLandCommand => new DelegateCommand(DroneLand);

        public ICommand ReconnectSensorCommand => new DelegateCommand(ReconnectSensor);
        public ICommand ReloadUserProfilesCommand => new DelegateCommand(LoadUserProfiles);

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

        public void UpdateSensorData(int[] bytesAsInts)
        { 
            var enableActive = bytesAsInts[0] > 2;
            var lockActive = bytesAsInts[1] > 2;
            var utilActive = bytesAsInts[2] > 2;
            var modeActive = bytesAsInts[3] > 2;

            if (enableActive)
            {
                EnableSensor = "On";
            }
            else
            {
                EnableSensor = "Off";
            }

            if (lockActive)
            {
                LockSensor = "On";
            }
            else
            {
                LockSensor = "Off";
            }

            if (modeActive)
            {
                if(ModeSensor == "Forward/Backward")
                {
                    ModeSensor = "Left/Right";
                }
                else if (ModeSensor == "Left/Right")
                {
                    ModeSensor = "Turn Left/Right";
                }
                else if (ModeSensor == "Turn Left/Right")
                {
                    ModeSensor = "Forward/Backward";
                }
                else
                {
                    throw new NotImplementedException();
                }
            }
        }

        #endregion

        #region Helper Methods

        private void LoadUserProfiles()
        {
            UserProfiles.Clear();

            var profiles = _client.GetUserProfiles();

            foreach (var profile in profiles)
            {
                var p = new UserProfileVM(profile.Key, profile.Value);
                UserProfiles.Add(p);
            }

            if (UserProfiles.Count > 0)
            {
                ActiveProfile = UserProfiles[0];
            }
        }

        private void StartTraining(DroneCommand command)
        {
            IsTrainingInProgress = true;

            Task.Run(() =>
            {
                _client.StopRecognition();
                _sensorListener.SensorNotificationEnabled = false;

                _client.AcquireDataForCommand(ActiveProfile.Username, command);

                var updatedProfileData = _client.GetUserProfile(ActiveProfile.Username);
                var updatedProfile = new UserProfileVM(ActiveProfile.Username, updatedProfileData);

               Application.Current?.Dispatcher?.Invoke(() =>
               {
                   UserProfiles.Remove(ActiveProfile);
                   UserProfiles.Add(updatedProfile);

                   ActiveProfile = updatedProfile;
               });

                StopTraining();
            });
        }

        private void ResetCommandData(DroneCommand command)
        {
            _client.ResetDataForCommand(ActiveProfile.Username, command);
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
            });
        }

        bool _isRecognizing = false;
        private void ToggleRecognition()
        {
           if(_isRecognizing)
            {
                _client.StopRecognition();
                ToggleRecognitionLabel = "Start Recognition";
                _sensorListener.SensorNotificationEnabled = false;
                _isRecognizing = false;
            }
            else
            {
                _client.RecognizeCommands(ActiveProfile.Username);
                ToggleRecognitionLabel = "Stop Recognition";
                _sensorListener.SensorNotificationEnabled = true;
                _isRecognizing = true;
            }
        }

        private void AddUserProfile()
        {
            var profileCreationDialog = new ProfileCreationDialog();
          
            if (Dialog.ShowDialog("New Profile", profileCreationDialog))
            {
                var username = profileCreationDialog.Username;

                if (!string.IsNullOrEmpty(username))
                {
                    // Create profile on the back-end
                    _client.CreateUserProfile(username);
                    // Reload profile list
                    LoadUserProfiles();
                    // Select newly created profile
                    ActiveProfile = UserProfiles.First(p => p.Username == username);
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
                // Delete profile on the back-end
                _client.DeleteUserProfile(ActiveProfile.Username);
                // Reload profile list
               LoadUserProfiles();
            }
            else
            {
                Dialog.ShowMessageBox("Error", "Cannot delete last profile");
            }
        }

        private async void ReconnectSensor()
        {
            var sensorConnected = await _sensorListener.TryConnectToSensor();
            Dialog.ShowMessageBox("Info", sensorConnected ? "Sensor connected!" : "Sensor connection failed! Make sure that sensor is paired.");
        }

        private void DroneTakeoff()
        {
            _client.DroneTakeoff();
        }

        private void DroneLand()
        {
            _client.DroneLand();
        }

        #endregion

        #region Private Variables

        private readonly FrontEndServer _server;
        private readonly BackEndClient _client;
        private bool _isTrainingInProgress;

        private SensorListener _sensorListener;

        private UserProfileVM _activeProfileVM;

        #endregion
    }
}
