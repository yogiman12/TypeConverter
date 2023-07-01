import pyperclip
import pyautogui
import keyboard
import threading

EngToArKeyboard = {'`': 'ذ','q': 'ض','w': 'ص','e': 'ث','r': 'ق','t': 'ف','y': 'غ','u': 'ع','i': 'ه','o': 'خ','p': 'ح','[': 'ج',']': 'د',
                       'a': 'ش','s': 'س','d': 'ي','f': 'ب','g': 'ل','h': 'ا','j': 'ت','k': 'ن','l': 'م',';': 'ك',
                       '\'': 'ئ','z': 'ئ','x': 'ء','c': 'ؤ','v': 'ر','b': 'ﻻ','n': 'ى','m': 'ة',',': 'و','.': 'ز','/': 'ظ',
                       ' ': ' '
}

        
def clip(text):
    pyperclip.copy(text)

def convEnToAr (text):
    ArText = ''
    
    for char in range(0,len(text)):
        ArText +=EngToArKeyboard.get(text[char])
    
    clip(ArText)
def execute_code():
    
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'x')
    convEnToAr(pyperclip.paste())
    pyautogui.hotkey('ctrl', 'v')


def keyboard_shortcut_handler():
    keyboard.add_hotkey('ctrl+q', execute_code)     # Code to be executed when Ctrl+Q is pressed
    keyboard.wait()


# Start the keyboard shortcut handler in a separate thread
shortcut_thread = threading.Thread(target=keyboard_shortcut_handler)
shortcut_thread.start()

# Wait for the shortcut thread to finish
shortcut_thread.join()


