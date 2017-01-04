using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media.Animation;
using SimulationApp.Models;
using SimulationApp.ViewModels;

namespace SimulationApp.Controls
{
    public partial class Drone3D : UserControl
    {
        public Drone3D()
        {
            InitializeComponent();

            Viewport.Loaded += OnViewportLoaded;
            DataContextChanged += OnDataContextChanged;
        }

        private void OnViewportLoaded(object sender, RoutedEventArgs e)
        {
            _forwardAnimation = (Storyboard) FindResource("MoveForward");
            _backAnimation = (Storyboard)FindResource("MoveBack");

            _rightAnimation = (Storyboard)FindResource("MoveRight");
            _leftAnimation = (Storyboard)FindResource("MoveLeft");

            _upAnimation = (Storyboard)FindResource("MoveUp");
            _downAnimation = (Storyboard)FindResource("MoveDown");

            _turnRightAnimation = (Storyboard)FindResource("TurnRight");
            _turnLeftAnimation = (Storyboard)FindResource("TurnLeft");

            _resetAnimation = (Storyboard)FindResource("Reset");
        }

        private void OnDataContextChanged(object sender, DependencyPropertyChangedEventArgs e)
        {
            var vm = e.NewValue as TrainingVM;

            if (vm != null)
            {
                vm.DroneCommandTriggered += OnDroneCommandTriggered;
            }
        }

        private void OnDroneCommandTriggered(DroneCommand droneCommand)
        {
            switch(droneCommand)
            {
                case DroneCommand.MoveForward:
                    _forwardAnimation.Begin();
                    break;
                case DroneCommand.MoveBack:
                    _backAnimation.Begin();
                    break;
                case DroneCommand.MoveRight:
                    _rightAnimation.Begin();
                    break;
                case DroneCommand.MoveLeft:
                    _leftAnimation.Begin();
                    break;
                case DroneCommand.MoveUp:
                    _upAnimation.Begin();
                    break;
                case DroneCommand.MoveDown:
                    _downAnimation.Begin();
                    break;
                case DroneCommand.TurnRight:
                    _turnRightAnimation.Begin();
                    break;
                case DroneCommand.TurnLeft:
                    _turnLeftAnimation.Begin();
                    break;
                case DroneCommand.Reset:
                    _resetAnimation.Begin();
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(droneCommand), droneCommand, null);
            }
        }

        private Storyboard _forwardAnimation;
        private Storyboard _backAnimation;

        private Storyboard _rightAnimation;
        private Storyboard _leftAnimation;

        private Storyboard _upAnimation;
        private Storyboard _downAnimation;

        private Storyboard _turnRightAnimation;
        private Storyboard _turnLeftAnimation;

        private Storyboard _resetAnimation;
    }
}
