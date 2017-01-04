using System.Windows.Controls;


namespace SimulationApp
{
    public partial class GraphView : UserControl
    {
        public GraphView()
        {
            InitializeComponent();

            var vm = new GraphVM();
            this.DataContext = vm;

            vm.SendMockData();
        }
    }
}
