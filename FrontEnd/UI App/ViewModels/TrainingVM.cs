using System.ComponentModel;
using System.Threading.Tasks;
using System.Windows.Input;

using SimulationApp.Models;


namespace SimulationApp.ViewModels
{
    public class TrainingVM : INotifyPropertyChanged
    {
        public TrainingVM()
        {
            var server = new FrontEndServer(this);
            server.Start();
        }

        #region Events

        public event PropertyChangedEventHandler PropertyChanged;

        public delegate void CommandTrigerredHandler(DroneCommand droneCommand);
        public event CommandTrigerredHandler DroneCommandTriggered;

        #endregion

        #region Properties

        public bool IsTrainingInProgress
        {
            get { return _isTrainingInProgress; }
            set
            {
                _isTrainingInProgress = value;
                NotifyPropertyChanged(nameof(IsTrainingInProgress));
            }
        }

        #endregion

        #region Commands

        public ICommand TrainCommand => new DelegateCommand(StartTraining, null);

        #endregion

        #region Public Methods

        public void ExecuteDroneCommand(DroneCommand droneCommand)
        {
            DroneCommandTriggered?.Invoke(droneCommand);
        }

        #endregion

        #region Helper Methods

        private void StartTraining(object o)
        {
            IsTrainingInProgress = true;

            Task.Delay(8000).ContinueWith(t => StopTraining());
        }

        private void StopTraining()
        {
            IsTrainingInProgress = false;
        }

        private void NotifyPropertyChanged(string prop)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(prop));
        }

        #endregion

        #region Private Variables

        private bool _isTrainingInProgress;

        #endregion
    }
}
