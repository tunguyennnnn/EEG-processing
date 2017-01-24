using System.Windows.Controls;

namespace SimulationApp.Controls
{
    public partial class ProfileCreationDialog : UserControl
    {
        public ProfileCreationDialog()
        {
            InitializeComponent();
        }

        public string Username => UsernameTextBox.Text;
    }
}
