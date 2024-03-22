from PIL import ImageGrab
import pyautogui
from pynput import mouse
import time
import keyboard
def on_click(x, y, button, pressed):
    if pressed:
        rgb = ImageGrab.grab().load()[x,y]
        # print(rgb)
        print(f'{x} {y}')

# def main()
# with mouse.Listener(on_click=on_click) as listener:
#    listener.join()
        
cancel_coords = 1792 
# 657

482, 231
time.sleep(3)

gem_color = (255, 0, 68)
cheese_color = (244, 180, 27)
beer_color = (173, 193, 188)
borb_color = (206, 245, 135)

gem_x_coord = 1252
cancel_color = (221, 26, 30)
start_button_x_coord = 2090
refresh_button_x_coord = 590
claim_button_x_coord = 2050
# trade_coord_list = [330, 450, 567, 691, 808, 930, 1050]
cancel_coord_list = [336, 456, 576, 696, 816, 936, 1056]
start_game = False
gui_button_y = 1160

# for y_coord in cancel_coord_list:   

#     print((ImageGrab.grab().load()[gem_x_coord, y_coord], ImageGrab.grab().load()[cancel_coords, y_coord]) )
while True:
    if keyboard.is_pressed("o"):
        start_game = True
    if start_game:
        if ImageGrab.grab().load()[481, 320] == (255, 255, 255):
            pyautogui.scroll(-1)
        for y_coord in cancel_coord_list:
            if ImageGrab.grab().load()[gem_x_coord, y_coord] == gem_color:
                if ImageGrab.grab().load()[cancel_coords, y_coord] == cancel_color:
                    continue
                else:
                    pyautogui.moveTo(start_button_x_coord, y_coord)
                    pyautogui.mouseDown()
                    pyautogui.mouseUp()
            else:
                continue
            # if keyboard.is_pressed("p"):
            #     start_game =False
            #     break
        # if start_game:
        pyautogui.moveTo(claim_button_x_coord, gui_button_y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.moveTo(refresh_button_x_coord, gui_button_y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        if keyboard.is_pressed("p"):
            start_game =False
            
    

