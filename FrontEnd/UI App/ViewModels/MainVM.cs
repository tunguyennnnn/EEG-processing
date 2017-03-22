using SimulationApp.Services;

namespace SimulationApp.ViewModels
{
    public class MainVM
    {
        public MainVM()
        {
            Training = new TrainingVM();
            Graph = new GraphVM();

            var frontEndServer = new FrontEndServer(this);
            frontEndServer.Start();

            Training.SetFrontEndServer(frontEndServer);
        }

        public TrainingVM Training { get; private set; }
        public GraphVM Graph { get; private set; }
    }
}
