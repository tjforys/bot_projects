import pyautogui
# import time
import keyboard
print('Press Ctrl-C to quit.')

# pyautogui.click(x=pyautogui.size()[0]/2, y=pyautogui.size()[1]/2)
# pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2, 2)
a=0
start_game = False
pyautogui.FAILSAFE = False
while True:
    if keyboard.is_pressed("o"):
        start_game = True
    if start_game:
        for i in range(1, 12):
            pyautogui.moveTo(x=pyautogui.size()[0]/2, y=pyautogui.size()[1]/2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            pyautogui.moveTo(10, pyautogui.size()[1]*i/12)
            pyautogui.moveTo(pyautogui.size()[0], pyautogui.size()[1]*i/12, 1)
            if keyboard.is_pressed("p"):
                start_game =False
                break
            a+=1
        
# for i in range(1,12):
    
#     print((pyautogui.size()[0]/i, pyautogui.size()[1]/i))
# # pyautogui.moveTo(pyautogui.size()[0], pyautogui.size()[1])