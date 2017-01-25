using System;
using System.Collections.Generic;

using SimulationApp.Models;
using SimulationApp.Utilities;


namespace SimulationApp.ViewModels
{
    public class UserProfileVM : ViewModelBase
    {
        public UserProfileVM(string username, IEnumerable<DroneCommand> activeCommands = null)
        {
            Username = username;

            if (activeCommands != null)
            {
                InitializeActiveCommands(activeCommands);
            }
        }

        #region Properties

        public string Username { get; private set; }
        public IList<DroneCommand> ActiveCommands { get; } = new List<DroneCommand>();

        public bool MoveForwardEnabled
        {
            get { return _moveForwardEnabled; }
            set
            {
                if (SetValue(ref _moveForwardEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveForward, value);
                }
            }
            
        }

        public bool MoveBackEnabled
        {
            get { return _moveBackEnabled; }
            set
            {
                if (SetValue(ref _moveBackEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveBack, value);
                }
            }
        }

        public bool MoveRightEnabled
        {
            get { return _moveRightEnabled; }
            set
            {
                if (SetValue(ref _moveRightEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveRight, value);
                }
            }
        }

        public bool MoveLeftEnabled
        {
            get { return _moveLeftEnabled; }
            set
            {
                if (SetValue(ref _moveLeftEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveLeft, value);
                }
            }
        }

        public bool MoveUpEnabled
        {
            get { return _moveUpEnabled; }
            set
            {
                if (SetValue(ref _moveUpEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveUp, value);
                }
            }
        }

        public bool MoveDownEnabled
        {
            get { return _moveDownEnabled; }
            set
            {
                if (SetValue(ref _moveDownEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveDown, value);
                }
            }
        }

        public bool TurnRightEnabled
        {
            get { return _turnRightEnabled; }
            set
            {
                if (SetValue(ref _turnRightEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.TurnRight, value);
                }
            }
        }

        public bool TurnLeftEnabled
        {
            get { return _turnLeftEnabled; }
            set
            {
                if (SetValue(ref _turnLeftEnabled, value))
                {
                    UpdateActiveCommands(DroneCommand.TurnLeft, value);
                }
            }

        }

        #endregion

        #region Helper Methods

        private void InitializeActiveCommands(IEnumerable<DroneCommand> activeCommands)
        {
            foreach (var command in activeCommands)
            {
                switch (command)
                {
                    case DroneCommand.MoveForward:
                        MoveForwardEnabled = true;
                        break;
                    case DroneCommand.MoveBack:
                        MoveBackEnabled = true;
                        break;
                    case DroneCommand.MoveRight:
                        MoveRightEnabled = true;
                        break;
                    case DroneCommand.MoveLeft:
                        MoveLeftEnabled = true;
                        break;
                    case DroneCommand.MoveUp:
                        MoveUpEnabled = true;
                        break;
                    case DroneCommand.MoveDown:
                        MoveDownEnabled = true;
                        break;
                    case DroneCommand.TurnRight:
                        TurnRightEnabled = true;
                        break;
                    case DroneCommand.TurnLeft:
                        TurnLeftEnabled = true;
                        break;
                    case DroneCommand.Reset:
                        break;
                    default:
                        throw new ArgumentOutOfRangeException();
                }
            }
        }

        private void UpdateActiveCommands(DroneCommand command, bool isEnabled)
        {
            if (isEnabled)
            {
                ActiveCommands.Add(command);
            }
            else
            {
                ActiveCommands.Remove(command);
            }
        }

        #endregion

        #region Private Variables

        private bool _moveForwardEnabled;
        private bool _moveBackEnabled;

        private bool _moveRightEnabled;
        private bool _moveLeftEnabled;

        private bool _moveUpEnabled;
        private bool _moveDownEnabled;

        private bool _turnRightEnabled;
        private bool _turnLeftEnabled;

        #endregion
    }
}
