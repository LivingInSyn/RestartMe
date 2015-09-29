using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RestartMe
{
    public class Restarter
    {
        public void restart_now()
        {
            ProcessStartInfo psi = new ProcessStartInfo("shutdown", "/r /t 3");
            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            Process.Start(psi);
        }
    }
}
