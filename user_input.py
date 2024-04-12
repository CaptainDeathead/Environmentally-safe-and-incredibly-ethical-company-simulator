from typing import Dict
from pynput import keyboard
from pynput.keyboard import Key
import string
from time import sleep

SPECIAL_TO_STRING = {
    Key.left: 'left',
    Key.right: 'right',
    Key.up: 'up',
    Key.down: 'down',
    Key.ctrl: 'ctrl'
}

KEYS: Dict = {
    'left': False, 'right': False, 'up': False, 'down': False, 'ctrl': False
}

for letter in list(string.ascii_lowercase):
    KEYS[letter] = False

def on_press(key: Key):
    try:            
        if key.char in list(KEYS.keys()): KEYS[key.char] = True
    except AttributeError:
        if key in list(SPECIAL_TO_STRING.keys()): KEYS[SPECIAL_TO_STRING[key]] = True
    return False
        
def on_release(key):
    try:            
        if key.char in list(KEYS.keys()): KEYS[key.char] = False
    except AttributeError:
        if key in list(SPECIAL_TO_STRING.keys()): KEYS[SPECIAL_TO_STRING[key]] = False
    return False

def get_input() -> str:
    listener: keyboard.Listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
    if KEYS['ctrl'] and KEYS['c']:
        print("\nKeyboard interupt detected. Program shutting down!")
        exit()