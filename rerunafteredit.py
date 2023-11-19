# $language = "python"
# $interface = "1.0"

# Coded by JackieGaming
import subprocess
import time
import random

initialTab = crt.GetScriptTab()


def getTabByName(strName):
    for nTabIndex in range(1, crt.GetTabCount() + 1):
        objTab = crt.GetTab(nTabIndex)
        if objTab.Caption == strName:
            return objTab
    return None


def rerun_s3relay():
	gettab = getTabByName("S3relay")
        gettab.Activate
        gettab.Screen.Send("exit\r")
        gettab.Screen.Send("y\r")
        crt.Sleep(random.randint(5000,7000))
        gettab.Screen.Send("./s3relay_y\r")
        crt.Sleep(random.randint(2000,5000))


def rerun_jxlinux():
    gettab1 = getTabByName("Gameserver")
    gettab1.Activate
    crt.Sleep(random.randint(2000,5000))
    gettab1.Screen.Send("./jx_linux_y\r")
        

rerun_s3relay()
rerun_jxlinux()


