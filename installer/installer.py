'''
Created by Jeremy Mill, originally for use in the hi tech classrooms at the University of CT

Licensed under the GPLv3

jeremymill@gmail.com
github.com/livinginsyn
'''

import os
import shutil as util
import _winreg as wreg
import subprocess

#first thing to find is the version of the OS
try:
    os.environ["PROGRAMFILES(X86)"]
    ver = 64
except:
    ver = 32
    
def sixty_folder():
    directory = 'C:\\Program Files (x86)\\RestartMe\\'
    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        overwrite = True
    return directory
    
def thirty_folder():
    directory = 'C:\\Program Files\\RestartMe\\'
    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        overwrite = True
    return directory
    
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
def install(directory,ver):
    files = ["Restart.exe","admin_key_32.reg","admin_key_64.reg","RestartMe_32.lnk","RestartMe_64.lnk"]
    for item in files:
        to_copy = resource_path(item)
        util.copy(to_copy,directory)
    #now make the reg key for running as admin for all users
    if ver == 32:
        reg_file = "admin_key_32.reg"
        lnk_file = "RestartMe_32.lnk"
    if ver == 64:
        reg_file = "admin_key_64.reg"
        lnk_file = "RestartMe_64.lnk"
    #use regedit in silent mode to place the value in the key
    reg_file_path = os.path.join(directory,reg_file)
    subprocess.Popen(["regedit.exe","/s",reg_file_path])
    #create the short cut
    to_copy = os.path.join(directory,lnk_file)
    util.copy(to_copy,"C:\\Users\\Public\\Desktop\\")
    os.rename("C:\\Users\\Public\\Desktop\\"+lnk_file,"C:\\Users\\Public\\Desktop\\RestartMe.lnk")
    
#the meat and potatoes
if ver == 64:
    directory = sixty_folder()
    install(directory,ver)
elif ver == 32:
    directory = thirty_folder()
    install(directory,ver)
    
