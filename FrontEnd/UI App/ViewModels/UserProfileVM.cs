using System;
using System.Collections.Generic;
using System.Linq;
using SimulationApp.Models;
using SimulationApp.Utilities;


namespace SimulationApp.ViewModels
{
    public class UserProfileVM : ViewModelBase
    {
        public UserProfileVM(string username, IDictionary<DroneCommand,int> commandSamples = null)
        {
            Username = username;

            if (commandSamples != null)
            {
                CommandSamples = commandSamples;
                InitializeActiveCommands(commandSamples);
            }
        }

        #region Properties

        public string Username { get; private set; }
        public IList<DroneCommand> ActiveCommands { get; } = new List<DroneCommand>();
        public IDictionary<DroneCommand, int> CommandSamples = new Dictionary<DroneCommand, int>();

        #region Move Forward

        public bool MoveForwardChecked
        {
            get { return _moveForwardChecked; }
            set
            {
                if (SetValue(ref _moveForwardChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveForward, value);
                }
            }         
        }

        public int MoveForwardNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.MoveForward) ? CommandSamples[DroneCommand.MoveForward] : 0;
        public bool MoveForwardEnabled => MoveForwardNumberOfSamples > 0;
        public string MoveForwardTooltip => $"Number of samples: {MoveForwardNumberOfSamples}";

        #endregion

        #region Move Back

        public bool MoveBackChecked
        {
            get { return _moveBackChecked; }
            set
            {
                if (SetValue(ref _moveBackChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveBack, value);
                }
            }
        }

        public int MoveBackNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.MoveBack) ? CommandSamples[DroneCommand.MoveBack] : 0;
        public bool MoveBackEnabled => MoveBackNumberOfSamples > 0;
        public string MoveBackTooltip => $"Number of samples: {MoveBackNumberOfSamples}";

        #endregion

        #region Move Right

        public bool MoveRightChecked
        {
            get { return _moveRightChecked; }
            set
            {
                if (SetValue(ref _moveRightChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveRight, value);
                }
            }
        }

        public int MoveRightNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.MoveRight) ? CommandSamples[DroneCommand.MoveRight] : 0;
        public bool MoveRightEnabled => MoveRightNumberOfSamples > 0;
        public string MoveRightTooltip => $"Number of samples: {MoveRightNumberOfSamples}";

        #endregion

        #region Move Left

        public bool MoveLeftChecked
        {
            get { return _moveLeftChecked; }
            set
            {
                if (SetValue(ref _moveLeftChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveLeft, value);
                }
            }
        }

        public int MoveLeftNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.MoveLeft) ? CommandSamples[DroneCommand.MoveLeft] : 0;
        public bool MoveLeftEnabled => MoveLeftNumberOfSamples > 0;
        public string MoveLeftTooltip => $"Number of samples: {MoveLeftNumberOfSamples}";

        #endregion

        #region Move Up

        public bool MoveUpChecked
        {
            get { return _moveUpChecked; }
            set
            {
                if (SetValue(ref _moveUpChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveUp, value);
                }
            }
        }

        public int MoveUpNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.MoveUp) ? CommandSamples[DroneCommand.MoveUp] : 0;
        public bool MoveUpEnabled => MoveUpNumberOfSamples > 0;
        public string MoveUpTooltip => $"Number of samples: {MoveUpNumberOfSamples}";

        #endregion

        #region Move Down

        public bool MoveDownChecked
        {
            get { return _moveDownChecked; }
            set
            {
                if (SetValue(ref _moveDownChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.MoveDown, value);
                }
            }
        }

        public int MoveDownNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.MoveDown) ? CommandSamples[DroneCommand.MoveDown] : 0;
        public bool MoveDownEnabled => MoveDownNumberOfSamples > 0;
        public string MoveDownTooltip => $"Number of samples: {MoveDownNumberOfSamples}";

        #endregion

        #region Turn Right

        public bool TurnRightChecked
        {
            get { return _turnRightChecked; }
            set
            {
                if (SetValue(ref _turnRightChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.TurnRight, value);
                }
            }
        }

        public int TurnRightNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.TurnRight) ? CommandSamples[DroneCommand.TurnRight] : 0;
        public bool TurnRightEnabled => TurnRightNumberOfSamples > 0;
        public string TurnRightTooltip => $"Number of samples: {TurnRightNumberOfSamples}";

        #endregion

        #region Turn Left

        public bool TurnLeftChecked
        {
            get { return _turnLeftChecked; }
            set
            {
                if (SetValue(ref _turnLeftChecked, value))
                {
                    UpdateActiveCommands(DroneCommand.TurnLeft, value);
                }
            }

        }

        public int TurnLeftNumberOfSamples => CommandSamples.ContainsKey(DroneCommand.TurnLeft) ? CommandSamples[DroneCommand.TurnLeft] : 0;
        public bool TurnLeftEnabled => TurnLeftNumberOfSamples > 0;
        public string TurnLeftTooltip => $"Number of samples: {TurnLeftNumberOfSamples}";

        #endregion

        #endregion

        #region Helper Methods

        private void InitializeActiveCommands(IDictionary<DroneCommand, int> commandSamples)
        {
            var activeCommands = commandSamples.Select(commandPair => commandPair.Key).ToList();

            foreach (var command in activeCommands)
            {
                switch (command)
                {
                    case DroneCommand.MoveForward:
                        MoveForwardChecked = true;
                        break;
                    case DroneCommand.MoveBack:
                        MoveBackChecked = true;
                        break;
                    case DroneCommand.MoveRight:
                        MoveRightChecked = true;
                        break;
                    case DroneCommand.MoveLeft:
                        MoveLeftChecked = true;
                        break;
                    case DroneCommand.MoveUp:
                        MoveUpChecked = true;
                        break;
                    case DroneCommand.MoveDown:
                        MoveDownChecked = true;
                        break;
                    case DroneCommand.TurnRight:
                        TurnRightChecked = true;
                        break;
                    case DroneCommand.TurnLeft:
                        TurnLeftChecked = true;
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

        private bool _moveForwardChecked;
        private bool _moveBackChecked;

        private bool _moveRightChecked;
        private bool _moveLeftChecked;

        private bool _moveUpChecked;
        private bool _moveDownChecked;

        private bool _turnRightChecked;
        private bool _turnLeftChecked;

        #endregion
    }
}
