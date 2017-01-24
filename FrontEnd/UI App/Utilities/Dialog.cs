using System.Windows;
using System.Windows.Controls;

using FirstFloor.ModernUI.Windows.Controls;


namespace SimulationApp.Utilities
{
    public class Dialog
    {
        public static void ShowMessageBox(string title, string message)
        {
            Application.Current.Dispatcher.Invoke(() => ModernDialog.ShowMessage(message, title, MessageBoxButton.OK));
        }

        public static bool ShowDialog(string title, UserControl content)
        {
            var dialog = new ModernDialog { Title = title, Content = content };
            dialog.Buttons = new [] { dialog.OkButton, dialog.CancelButton };
            dialog.ShowDialog();

            return dialog.DialogResult.HasValue && dialog.DialogResult.Value;
        }
    }
}
