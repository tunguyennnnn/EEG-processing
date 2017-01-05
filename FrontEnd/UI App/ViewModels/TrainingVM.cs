using System;
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
        }

        #region Properties

        public bool IsTrainingInProgress
        {
            get { return _isTrainingInProgress; }
            set { SetValue(ref _isTrainingInProgress, value); }
        }

        #endregion

        #region Commands

        public ICommand TrainCommand => new DelegateCommand(StartTraining);

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

        private void StartTraining()
        {
            IsTrainingInProgress = true;

            Task.Delay(8000).ContinueWith(t => StopTraining());
        }

        private void StopTraining()
        {
            IsTrainingInProgress = false;
        }

        #endregion

        #region Private Variables

        private readonly FrontEndServer _server;
        private bool _isTrainingInProgress;
        
        #endregion
    }
}
