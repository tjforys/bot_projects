from PIL import ImageGrab
import pyautogui
import keyboard
import time

def move_click(coord_x = None, coord_y = None):
    if coord_x and coord_y:
        pyautogui.moveTo(coord_x, coord_y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def is_auto_refresh_text_present():
    return ImageGrab.grab().load()[481, 320] == (255, 255, 255)


def teleport_to_witch_and_back():
    witch_area_x, witch_area_y = 1770, 465
    inner_pyramid_x, inner_pyramid_y = 1770, 329
    pyautogui.press("v")
    move_click(witch_area_x, witch_area_y)
    time.sleep(6)
    move_click(inner_pyramid_x, inner_pyramid_y)
    pyautogui.press("y")
    
def teleport_to_shard_boss_and_back():
    time.sleep(0.5)
    inner_pyramid_x, inner_pyramid_y = 1770, 329
    boss_x, boss_y = 1770, 767
    pyautogui.press("v")
    move_click(boss_x, boss_y)
    time.sleep(1)
    pyautogui.press("v")
    for i in range(5):
        move_click(1236, 740)
        time.sleep(2)
    pyautogui.press("v")
    move_click(inner_pyramid_x, inner_pyramid_y)
    pyautogui.press("y")
cancel_coords = 1792 
gem_x_coord = 1252
start_button_x_coord = 2090
refresh_button_x_coord = 590
claim_button_x_coord = 2050
cancel_coord_list = [336, 456, 576, 696, 816, 936, 1056]
gui_button_y = 1160

cancel_color = (221, 26, 30)
gem_color = (255, 0, 68)
cheese_color = (244, 180, 27)
beer_color = (174, 195, 190)
borb_color = (206, 245, 135)

current_material_list = [gem_color]
start_game = False

while True:
    if keyboard.is_pressed("o"):
        start_game = True
        teleport_to_witch_and_back()
        witch_start_time=time.time()
        teleport_to_shard_boss_and_back()
        shard_boss_start_time = time.time()
    if start_game:
        if time.time() - witch_start_time >= 150:
            teleport_to_witch_and_back()
            witch_start_time = time.time()

        if time.time() - shard_boss_start_time >= 180:
            teleport_to_shard_boss_and_back()
            shard_boss_start_time = time.time()
        if is_auto_refresh_text_present():
            pyautogui.scroll(-1)

        current_screen = ImageGrab.grab().load()
        for y_coord in cancel_coord_list:
            if current_screen[gem_x_coord, y_coord] in current_material_list:
                if current_screen[cancel_coords, y_coord] != cancel_color:
                    move_click(start_button_x_coord, y_coord)

        move_click(claim_button_x_coord, gui_button_y)
        move_click(refresh_button_x_coord, gui_button_y)

        if keyboard.is_pressed("p"):
            start_game =False
            