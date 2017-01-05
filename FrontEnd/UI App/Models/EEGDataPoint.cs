using CsvHelper.Configuration;

namespace SimulationApp.Models
{
   public class EEGDataPoint
    {
        public double AF3 { get; set; }
        public double F7  { get; set; }
        public double F3  { get; set; }
        public double FC5 { get; set; }
        public double T7  { get; set; }
        public double P7  { get; set; }
        public double O1  { get; set; }

        public double O2  { get; set; }
        public double P8  { get; set; }
        public double T8  { get; set; }
        public double FC6 { get; set; }
        public double F4  { get; set; }
        public double F8  { get; set; }
        public double AF4 { get; set; }
    }

    public sealed class EEGDataMap : CsvClassMap<EEGDataPoint>
    {
        public EEGDataMap()
        {
            Map(m => m.AF3).Name("AF3");
            Map(m => m.F7).Name("F7");
            Map(m => m.F3).Name("F3");
            Map(m => m.FC5).Name("FC5");
            Map(m => m.T7).Name("T7");
            Map(m => m.P7).Name("P7");
            Map(m => m.O1).Name("O1");

            Map(m => m.O2).Name("O2");
            Map(m => m.P8).Name("P8");
            Map(m => m.T8).Name("T8");
            Map(m => m.FC6).Name("FC6");
            Map(m => m.F4).Name("F4");
            Map(m => m.F8).Name("F8");
            Map(m => m.AF4).Name("AF4");
        }
    }
}
