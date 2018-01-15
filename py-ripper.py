#py-ripper
#rips dvd files to a directory on the desktop.

#imports
import shutil,win32api,win32file,os
from os import *
from shutil import *
#end imports

global drivesL

def rip(drv):
    for i in drv:
        print ("* - " + i)
    ch = input ("Pick one of the drive letters above to rip:")
    ch = ch.upper()
    x = win32file.GetDriveType(ch)
    ch2 = input ("Are [y]ou sure you wa[n]t to rip this drive:")
    ch2 = ch2.lower()
    if ch2 == "y":
        print ("Beginning to rip...")
    else:
        start()
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    pathD = desktop + "\\" + ch
    shutil.copytree(ch + ":\\",pathD,copy_function = copy2)
    print ("Finished ripping")

def drivels():
    drivesL = win32api.GetLogicalDriveStrings()
    drivesL = drivesL.split('\000')[:-1]
    return (drivesL)

def start():
    drives = drivels()
    rip(drives)
start()