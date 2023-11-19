# $language = "python"
# $interface = "1.0"

# Coded by JackieGaming
import os, signal
import subprocess
import time
import random

initialTab = crt.GetScriptTab()
SECURECRTPROC = "SecureCRT.exe"
SWORD3PROC = "Sword3PaySys_Y.exe"
S3RELAYSERVERPROC = "S3RelayServer_Y.exe"
CREATE_NO_WINDOW = 0x08000000


def getTabByName(strName):
    for nTabIndex in range(1, crt.GetTabCount() + 1):
        objTab = crt.GetTab(nTabIndex)
        if objTab.Caption == strName:
            return objTab

    # Default to returning nothing if we never find a tab by the given name
    return None


def quit_s3relay():
	gettab = getTabByName("S3relay")
        gettab.Activate
        gettab.Screen.Send("exit\r")
        gettab.Screen.Send("y\r")
        crt.Sleep(random.randint(5000,7000))
        gettab.Screen.Send("exit\r")
        crt.Sleep(random.randint(5000,7000))
        gettab.Close()
               

def quit_securecrt():  
    subprocess.call('taskkill /F /IM '+SWORD3PROC, creationflags=CREATE_NO_WINDOW)
    subprocess.call('taskkill /F /IM '+S3RELAYSERVERPROC, creationflags=CREATE_NO_WINDOW)
    subprocess.call('taskkill /F /IM '+SECURECRTPROC, creationflags=CREATE_NO_WINDOW)


quit_s3relay()
quit_securecrt()

