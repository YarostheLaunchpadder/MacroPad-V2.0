import sys
import contextlib
import ctypes
import time
import os
from PIL import ImageTk, Image
from tkinter import *
from tkinter.font import Font
import webbrowser
from PIL import ImageTk, Image

with contextlib.redirect_stdout(None):  # Makes no pygame prompt appear
    import launchpad_py as launchpad

import warnings

warnings.filterwarnings('ignore')

# THEME MANUAL SELECTION ----------------- white, #2d2d2d
backgound = '#2d2d2d'
foreground = 'white'
'''
menuwindow = Tk()  # create a Window
menuwindow.iconbitmap("ui/logo/logo_small.ico")
menuwindow.title("MacroPad")
menuwindow.resizable(width=False, height=False)
menuwindow.configure(bg=backgound)

window_height = 400
window_width = 500

screen_width = menuwindow.winfo_screenwidth()
screen_height = menuwindow.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

menuwindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# C struct redefinitions
SendInput = ctypes.windll.user32.SendInput
PUL = ctypes.POINTER(ctypes.c_ulong)
'''
keys = {"a": 0x1E,
        "b": 0x30,
        "c": 0x2E,
        "d": 0x20,
        "e": 0x12,
        "f": 0x21,
        "g": 0x22,
        "h": 0x23,
        "i": 0x17,
        "j": 0x24,
        "k": 0x25,
        "l": 0x26,
        "m": 0x32,
        "n": 0x31,
        "o": 0x18,
        "p": 0x19,
        "q": 0x10,
        "r": 0x13,
        "s": 0x1F,
        "t": 0x14,
        "u": 0x16,
        "v": 0x2F,
        "w": 0x11,
        "x": 0x2D,
        "y": 0x15,
        "z": 0x2C,
        "Esc": 0x01,
        1: 0x02,
        2: 0x03,
        3: 0x04,
        4: 0x05,
        5: 0x06,
        6: 0x07,
        7: 0x08,
        8: 0x09,
        9: 0x0A,
        10: 0x0B,
        "-": 0x0C,
        "=": 0x0D,
        "Backspace": 0x0E,
        "Tab": 0x0F,
        "[": 0x1A,
        "]": 0x1B,
        "Enter": 0x1C,
        "Ctrl": 0x1D,
        ";": 0x27,
        "Apostrophe": 0x28,
        "Shift": 0x2A,
        "Backslash": 0x2B,
        ",": 0x33,
        ".": 0x34,
        "/": 0x35,
        "*": 0x37,
        "Alt": 0x38,
        "Space": 0x39,
        "Caps Lock": 0x3A,
        "F1": 0x3B,
        "F2": 0x3C,
        "F3": 0x3D,
        "F4": 0x3E,
        "F5": 0x3F,
        "F6": 0x40,
        "F7": 0x41,
        "F8": 0x42,
        "F9": 0x43,
        "F10": 0x44,
        "F11": 0x57,
        "F12": 0x58,
        "@": 0x91,
        ":": 0x92,
        "_": 0x93,
        "Home": 0xC7,
        "Pause": 0xC5,
        "Page Up": 0xC9,
        "Page Down": 0xD1,
        "End": 0xCF,
        "Delete": 0xD3,
        "Insert": 0xD2,
        "Windows": 0xDB,
        "Arrow Left": 0xCB,
        "Arrow Up": 0xC8,
        "Arrow Down": 0xD0,
        "Arrow Right": 0xCD,
        "Sys RQ": 0xB7}

# C struct redefinitions
SendInput = ctypes.windll.user32.SendInput
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Keyboard functions for in-game drivers

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def setup():
    pass


def loadapp(lpmodel):
    pass


def load_preset(file):
    pass


def save_preset(location):
    pass


def exitapp():
    pass


def launchpadtrigger(currentlp):
    pass

def mapkey():
    pass


def checkargs(arguments):
    if len(arguments) > 1: # If there are arguments that means that we want to open the preset straight away!
        load_preset(arguments[1])
    
checkargs(sys.argv)