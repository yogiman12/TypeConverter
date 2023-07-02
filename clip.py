from pyperclip import copy , paste 
from pyautogui import hotkey 
from keyboard import add_hotkey , wait
from threading import Thread

EngToArKeyboard = {'`': 'ذ','1': '1','2': '2','3': '3','4': '4','5': '5','6': '6','7': '7','8': '8','9': '9','0': '0','-': '-','=': '=',
                        'q': 'ض','w': 'ص','e': 'ث','r': 'ق','t': 'ف','y': 'غ','u': 'ع','i': 'ه','o': 'خ','p': 'ح','[': 'ج',']': 'د',
                       'a': 'ش','s': 'س','d': 'ي','f': 'ب','g': 'ل','h': 'ا','j': 'ت','k': 'ن','l': 'م',';': 'ك',
                       '\'': 'ط','z': 'ئ','x': 'ء','c': 'ؤ','v': 'ر','b': 'ﻻ','n': 'ى','m': 'ة',',': 'و','.': 'ز','/': 'ظ',
                       ' ': ' '
}

        
def clip(text):
    copy(text)

def convEnToAr (text):
    ArText = ' '
    
    for char in range(0,len(text)):
        ArText +=EngToArKeyboard.get(text[char])
    
    clip(ArText)
def execute_code():
    
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'x')
    convEnToAr(paste().lower())
    hotkey('ctrl', 'v')


def keyboard_shortcut_handler():
    add_hotkey('ctrl+q', execute_code)     # Code to be executed when Ctrl+Q is pressed
    wait()


# Start the keyboard shortcut handler in a separate thread
shortcut_thread = Thread(target=keyboard_shortcut_handler)
shortcut_thread.start()

# Wait for the shortcut thread to finish
shortcut_thread.join()


