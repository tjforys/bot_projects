from PIL import ImageGrab
import pyautogui
from pynput import mouse
import time
def on_click(x, y, button, pressed):
    if pressed:
        rgb = ImageGrab.grab().load()[x,y]
        print(rgb)
        print(f'{x} {y}')
# 2309 155
# 1164 888
# 1307 982
# 760 798
# with mouse.Listener(on_click=on_click) as listener:
#    listener.join()
# lista = [(x, y)
#    for x in range(1164, 1307)
#    for y in range(888, 982)
# ]
# time.sleep(5)
# print(ImageGrab.grab().load()[655, 884])
# 323 930
# 655 884
# y=920
# lista = [x for x in range(1260, 1300)]
# # print(range(1160, 1200).count())
# # print([ImageGrab.grab().load()[x,y] for x in lista])
pyautogui.FAILSAFE = False
normal_fps_time = 0.1
twenty_fps_time = 0.60
while True:
    if ImageGrab.grab().load()[323, 930] == (255, 255, 255):
        time.sleep(normal_fps_time)
        pyautogui.moveTo(766, 789)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

# 766 789
