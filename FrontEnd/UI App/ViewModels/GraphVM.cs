using CsvHelper;
using LiveCharts;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Timers;
using System.Windows;

namespace SimulationApp
{
    public class GraphVM
    {
        public GraphVM()
        {
            LoadMockData();
        }

        public void OnGraphPointReceived(EEGDataPoint point)
        {
            if(Buffer.Count < 128)
            {
                Buffer.Add(point);
            }
            else
            {
                AddPointsToChart();
                Buffer.Clear();
                CleanUpChart();
            }
        }

        private void AddPointsToChart()
        {
           // Application.Current.Dispatcher.Invoke(new Action(() => { }), DispatcherPriority.ContextIdle, null);

            //using (var d = Application.Current.Dispatcher.DisableProcessing())
            //{
                AF3ChartValues.AddRange(Buffer.Select(p => p.AF3));
                F7ChartValues.AddRange(Buffer.Select(p => p.F7));
                F3ChartValues.AddRange(Buffer.Select(p => p.F3));
                FC5ChartValues.AddRange(Buffer.Select(p => p.FC5));
                T7ChartValues.AddRange(Buffer.Select(p => p.T7));
                P7ChartValues.AddRange(Buffer.Select(p => p.P7));
                O1ChartValues.AddRange(Buffer.Select(p => p.O1));

                O2ChartValues.AddRange(Buffer.Select(p => p.O2));
                P8ChartValues.AddRange(Buffer.Select(p => p.P8));
                T8ChartValues.AddRange(Buffer.Select(p => p.T8));
                FC6ChartValues.AddRange(Buffer.Select(p => p.FC6));
                F4ChartValues.AddRange(Buffer.Select(p => p.F4));
                F8ChartValues.AddRange(Buffer.Select(p => p.F8));
                AF4ChartValues.AddRange(Buffer.Select(p => p.AF4));
            //}
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

        public List<EEGDataPoint> Buffer = new List<EEGDataPoint>();

        public ChartValues<double> AF3ChartValues { get; set; }
        public ChartValues<double> F7ChartValues { get; set; }
        public ChartValues<double> F3ChartValues { get; set; }
        public ChartValues<double> FC5ChartValues { get; set; }
        public ChartValues<double> T7ChartValues { get; set; }
        public ChartValues<double> P7ChartValues { get; set; }
        public ChartValues<double> O1ChartValues { get; set; }

        public ChartValues<double> O2ChartValues { get; set; }
        public ChartValues<double> P8ChartValues { get; set; }
        public ChartValues<double> T8ChartValues { get; set; }
        public ChartValues<double> FC6ChartValues { get; set; }
        public ChartValues<double> F4ChartValues { get; set; }
        public ChartValues<double> F8ChartValues { get; set; }
        public ChartValues<double> AF4ChartValues { get; set; }

        // Data Mocking
        private double _timePeriod = 1000.0/128.0;

        private void LoadMockData()
        {
            // Read text file
            TextReader textReader = File.OpenText("Resources/EEG.csv");

            // Load and map CSV records
            var csv = new CsvReader(textReader);
            csv.Configuration.RegisterClassMap<EEGDataMap>();
            csv.Configuration.IgnoreHeaderWhiteSpace = true;
            var records = csv.GetRecords<EEGDataPoint>();

            MockPoints = new Queue<EEGDataPoint>(records);


            AF3ChartValues = new ChartValues<double>();
            F7ChartValues = new ChartValues<double>();
            F3ChartValues = new ChartValues<double>();
            FC5ChartValues = new ChartValues<double>();
            T7ChartValues = new ChartValues<double>();
            P7ChartValues = new ChartValues<double>();
            O1ChartValues = new ChartValues<double>();

            O2ChartValues = new ChartValues<double>();
            P8ChartValues = new ChartValues<double>();
            T8ChartValues = new ChartValues<double>();
            FC6ChartValues = new ChartValues<double>();
            F4ChartValues = new ChartValues<double>();
            F8ChartValues = new ChartValues<double>();
            AF4ChartValues = new ChartValues<double>();
        }

        public void SendMockData()
        {
            Timer = new Timer
            {
                Interval = _timePeriod
            };
            Timer.Elapsed += new ElapsedEventHandler(SendNextPoint);

            Timer.Start();
        }

        private void SendNextPoint(object sender, EventArgs eventArgs)
        {
            if (MockPoints.Count > 0)
            {
                var nextPoint = MockPoints.Dequeue();

                Application.Current?.Dispatcher?.Invoke(() => OnGraphPointReceived(nextPoint));           
            }
        }

        public Timer Timer { get; set; }
        public Queue<EEGDataPoint> MockPoints { get; set; }
    }
}
