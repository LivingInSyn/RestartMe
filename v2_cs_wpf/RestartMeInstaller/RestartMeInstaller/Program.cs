using IWshRuntimeLibrary;
using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RestartMeInstaller
{
    class Program
    {

        private static void deleteFiles(string filePath)
        {
            
            string[] fileEntries = Directory.GetFiles(filePath);
            foreach (string file in fileEntries)
            {
                //Console.WriteLine(file);
                System.IO.File.Delete(file);
            }
        }

        private static void copyNewFiles(string filePath)
        {

            filePath = filePath + @"\";

            System.IO.File.Copy("RestartMeFiles\\RestartMe.exe", filePath + "RestartMe.exe");
            System.IO.File.Copy("RestartMeFiles\\RestartMe.exe", filePath + "myicon.ico");
            System.IO.File.Copy("RestartMeFiles\\uninstall.exe", filePath + "uninstall.exe");


        }

        private static void makeRegEntries(string dir, int ver)
        {

            //create the uninstall string
            RegistryKey uninstallkey = Registry.LocalMachine.OpenSubKey("Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall", true);
            string uninstallString = "\"" + dir + @"\uninstall.exe" + "\"";

            RegistryKey uninstallSubKey = uninstallkey.CreateSubKey("Logoff_Utility");
            if (uninstallSubKey != null)
            {
                uninstallSubKey.SetValue("DisplayName", "HTC Restart Utility");
                uninstallSubKey.SetValue("UninstallString", uninstallString);
            }

            //NOW NEED TO CALL TO REGEDIT
            string regkey;
            if(ver == 32)
            {
                regkey = "RestartMeFiles\\admin_key_32.reg";
            }
            else
            {
                regkey = "RestartMeFiles\\admin_key_64.reg";
            }


            ProcessStartInfo psi = new ProcessStartInfo("regedit", "/s "+ regkey);
            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            Process.Start(psi);
            
        }

        private void createShortcuts(string tar_path)
        {
            /*string tar_path;
            if (ver == 32)
            {
                tar_path = "C:\\Program Files\\RestartMe\\";
            }
            else
            {
                tar_path = "C:\\Program Files (x86)\\RestartMe\\";
            }*/

            WshShell wsh = new WshShell();
            IWshRuntimeLibrary.IWshShortcut shortcut = wsh.CreateShortcut(
                "C:\\Users\\Public\\Desktop" + "\\Restart Computer.lnk") as IWshRuntimeLibrary.IWshShortcut;
            //empty string, no arguments
            shortcut.Arguments = "";
            shortcut.TargetPath = tar_path + "RestartMe.exe";
            // not sure about what this is for
            shortcut.WindowStyle = 1;
            shortcut.Description = "Restart the Computer";
            //I don't think I need this
            //shortcut.WorkingDirectory = "c:\\app";

            //I'll need to copy the ico file to disk
            shortcut.IconLocation = tar_path + "myicon.ico";
            shortcut.Save();

            
        }

        static void Main(string[] args)
        {

        }
    }
}
