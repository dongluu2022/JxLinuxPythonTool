# $language = "python"
# $interface = "1.0"

# Coded by JackieGaming
import subprocess
import time

host = "192.168.1.100"
user = "root"
passwd = "pgaming"
initialTab = crt.GetScriptTab()

def startS3RelayServer():
    SW_MINIMIZE = 6
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_MINIMIZE
    subprocess.Popen(r'C:\SV\Pays\S3RelayServer_Y.exe', startupinfo=info)
    time.sleep(5)


def startSword3PaySys():
    SW_MINIMIZE = 6
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_MINIMIZE
    subprocess.Popen(r'C:\SV\Pays\Sword3PaySys_Y.exe', startupinfo=info)
    time.sleep(5)

def run_goddess(host1,user1,passwd1):
    #Command string to run connection and send command to run
	cmd_goddess = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user1, passwd1, host1)
    #
        crt.Sleep(3000)
        goddess = crt.Session.ConnectInTab(cmd_goddess) #Mo tab
        goddess.Activate
        goddess.Caption = "Goddess" #Doi ten
        goddess.Screen.Send("cd /home/jxser/gateway\r") #Goi lenh
        goddess.Screen.Send("./goddess_y\r") #Goi lenh
   

def run_bishop(host1,user1,passwd1):
	cmd_bishop = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user1, passwd1, host1)
        crt.Sleep(3000)
        bishop = crt.Session.ConnectInTab(cmd_bishop)
        bishop.Activate
        bishop.Caption = "Bishop"
        bishop.Screen.Send("cd /home/jxser/gateway\r")
        bishop.Screen.Send("./bishop_y\r")    


def run_s3relay(host1,user1,passwd1):
	cmd_s3relay = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user1, passwd1, host1)
        crt.Sleep(3000)
        s3relay = crt.Session.ConnectInTab(cmd_s3relay)
        s3relay.Activate
        s3relay.Caption = "S3relay"
        s3relay.Screen.Send("cd /home/jxser/gateway/s3relay\r")
        s3relay.Screen.Send("./s3relay_y\r")    


def run_jxlinux(host1,user1,passwd1):
	cmd_jxlinux = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user1, passwd1, host1)
        crt.Sleep(3000)
        jxlinux = crt.Session.ConnectInTab(cmd_jxlinux)
        jxlinux.Activate
        jxlinux.Caption = "Gameserver"
        jxlinux.Screen.Send("cd /home/jxser/server1\r")
        jxlinux.Screen.Send("./jx_linux_y\r")    

startS3RelayServer()
startSword3PaySys()
run_goddess(host,user,passwd)
run_bishop(host,user,passwd)
run_s3relay(host,user,passwd)
run_jxlinux(host,user,passwd)

