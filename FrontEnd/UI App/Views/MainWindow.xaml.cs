using FirstFloor.ModernUI.Windows.Controls;
using SimulationApp.ViewModels;

namespace SimulationApp.Views
{
    public partial class MainWindow : ModernWindow
    {
        public MainWindow()
        {
            InitializeComponent();

            Loaded += MainWindow_Loaded;
        }

        private void MainWindow_Loaded(object sender, System.Windows.RoutedEventArgs e)
        {
            DataContext = new MainVM();
        }
    }
}
