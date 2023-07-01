import pyperclip
import pyautogui
import keyboard
import time

EngToArKeyboard = {'`': 'ذ','q': 'ض','w': 'ص','e': 'ث','r': 'ق','t': 'ف','y': 'غ','u': 'ع','i': 'ه','o': 'خ','p': 'ح','[': 'ج',']': 'د',
                       'a': 'ش','s': 'س','d': 'ي','f': 'ب','g': 'ل','h': 'ا','j': 'ت','k': 'ن','l': 'م',';': 'ك',
                       '\'': 'ئ','z': 'ئ','x': 'ء','c': 'ؤ','v': 'ر','b': 'ﻻ','n': 'ى','m': 'ة',',': 'و','.': 'ز','/': 'ظ',
                       ' ': ' '
}

def convEnToAr (text):
    ArText = ''
    
    for char in range(0,len(text)):
        ArText +=EngToArKeyboard.get(text[char])
    
    clip(ArText)
        
def clip(text):
    pyperclip.copy(text)

def execute_code():
    
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'x')
    convEnToAr(pyperclip.paste())
    pyautogui.hotkey('ctrl', 'v')
    # Code to be executed when Ctrl+Q is pressed
    print("Executing code...")
    # Add your code here

def check_keyboard_input():
    while True:
        try:
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
                time.sleep(0.1)
                execute_code()
                
        except:
            break

check_keyboard_input()
