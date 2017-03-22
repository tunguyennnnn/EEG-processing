using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows;
using System.Windows.Threading;
using LiveCharts;

namespace SimulationApp.ViewModels
{
    public class GraphVM
    {
        #region Properties

        public ChartValues<double> AF3ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> F7ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> F3ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> FC5ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> T7ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> P7ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> O1ChartValues { get; set; } = new ChartValues<double>();

        public ChartValues<double> O2ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> P8ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> T8ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> FC6ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> F4ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> F8ChartValues { get; set; } = new ChartValues<double>();
        public ChartValues<double> AF4ChartValues { get; set; } = new ChartValues<double>();

        #endregion

        #region Public Methods

        public void OnGraphPointReceived(IList<IList<double>> values)
        {
            PlotNewData(values);
            CleanUpChart();
        }

        #endregion

        #region Helper Methods

        private void PlotNewData(IList<IList<double>> values)
        {
            Application.Current.Dispatcher.Invoke(new Action(() => { }), DispatcherPriority.ContextIdle, null);

            AF3ChartValues.AddRange(values[0]);
            F7ChartValues.AddRange(values[1]);
            F3ChartValues.AddRange(values[2]);
            FC5ChartValues.AddRange(values[3]);
            T7ChartValues.AddRange(values[4]);
            P7ChartValues.AddRange(values[5]);
            O1ChartValues.AddRange(values[6]);

            O2ChartValues.AddRange(values[7]);
            P8ChartValues.AddRange(values[8]);
            T8ChartValues.AddRange(values[9]);
            FC6ChartValues.AddRange(values[10]);
            F4ChartValues.AddRange(values[11]);
            F8ChartValues.AddRange(values[12]);
            AF4ChartValues.AddRange(values[13]);
        }

        private void CleanUpChart()
        {
            if (AF3ChartValues.Count > 1024)
            {
                AF3ChartValues = new ChartValues<double>(AF3ChartValues.Skip(128));
                F7ChartValues = new ChartValues<double>(F7ChartValues.Skip(128));
                F3ChartValues = new ChartValues<double>(F3ChartValues.Skip(128));
                FC5ChartValues = new ChartValues<double>(FC5ChartValues.Skip(128));
                T7ChartValues = new ChartValues<double>(T7ChartValues.Skip(128));
                P7ChartValues = new ChartValues<double>(P7ChartValues.Skip(128));
                O1ChartValues = new ChartValues<double>(O1ChartValues.Skip(128));

                O2ChartValues = new ChartValues<double>(O2ChartValues.Skip(128));
                P8ChartValues = new ChartValues<double>(P8ChartValues.Skip(128));
                T8ChartValues = new ChartValues<double>(T8ChartValues.Skip(128));
                FC6ChartValues = new ChartValues<double>(FC6ChartValues.Skip(128));
                F4ChartValues = new ChartValues<double>(F4ChartValues.Skip(128));
                F8ChartValues = new ChartValues<double>(F8ChartValues.Skip(128));
                AF4ChartValues = new ChartValues<double>(AF4ChartValues.Skip(128));
            }
        }

        #endregion
    }
}
