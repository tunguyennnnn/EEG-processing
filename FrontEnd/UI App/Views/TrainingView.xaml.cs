using System;
using System.Windows.Controls;

namespace SimulationApp.Views
{
    public partial class Simulation : UserControl
    {
        public Simulation()
        {
            InitializeComponent();

            Dispatcher.ShutdownStarted += OnDispatcherShutdownStarted;
        }

        private void OnDispatcherShutdownStarted(object sender, EventArgs eventArgs)
        {
            var vm = (IDisposable) DataContext;
            vm.Dispose();
        }
    }
}
