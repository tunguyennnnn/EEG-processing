using System.Collections;
using System.Collections.Generic;

namespace SimulationApp.Models
{
    public class UserProfile
    {
        public UserProfile(string username)
        {
            Username = username;
        }

        public string Username { get; private set; }
        public IList<DroneCommand> CommandList { get; set; }
    }
}
