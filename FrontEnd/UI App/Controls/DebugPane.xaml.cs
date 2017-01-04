using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using SimulationApp.Models;
using SimulationApp.ViewModels;

namespace SimulationApp.Controls
{
    public partial class DebugPane : UserControl
    {
        public DebugPane()
        {
            InitializeComponent();
            DataContextChanged += OnDataContextChanged;
        }

        private void OnDataContextChanged(object sender, DependencyPropertyChangedEventArgs e)
        {
            _viewModel = e.NewValue as TrainingVM;
        }

        private void MoveForward(object sender, MouseEventArgs e) { _viewModel.ExecuteDroneCommand(DroneCommand.MoveForward); }
        private void MoveBack(object sender, MouseEventArgs e)    { _viewModel.ExecuteDroneCommand(DroneCommand.MoveBack); }
        private void MoveRight(object sender, MouseEventArgs e)   { _viewModel.ExecuteDroneCommand(DroneCommand.MoveRight); }
        private void MoveLeft(object sender, MouseEventArgs e)    { _viewModel.ExecuteDroneCommand(DroneCommand.MoveLeft); }
        private void MoveUp(object sender, MouseEventArgs e)      { _viewModel.ExecuteDroneCommand(DroneCommand.MoveUp); }
        private void MoveDown(object sender, MouseEventArgs e)    { _viewModel.ExecuteDroneCommand(DroneCommand.MoveDown); }    
        private void TurnRight(object sender, MouseEventArgs e)   { _viewModel.ExecuteDroneCommand(DroneCommand.TurnRight); }
        private void TurnLeft(object sender, MouseEventArgs e)    { _viewModel.ExecuteDroneCommand(DroneCommand.TurnLeft); }
        private void Reset(object sender, MouseEventArgs e)       { _viewModel.ExecuteDroneCommand(DroneCommand.Reset); }

        private TrainingVM _viewModel;
    }
}
