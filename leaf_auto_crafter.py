from PIL import ImageGrab
import pyautogui
from pynput import mouse
import time
def on_click(x, y, button, pressed):
    if pressed:
        rgb = ImageGrab.grab().load()[x,y]
        print(rgb)
        print(f'{x} {y}')

pyautogui.FAILSAFE = False
normal_fps_time = 0.1
twenty_fps_time = 0.60
challenge_fps_time = 0.03
while True:
    if ImageGrab.grab().load()[323, 930] == (255, 255, 255):
        time.sleep(normal_fps_time)
        pyautogui.moveTo(766, 789)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
