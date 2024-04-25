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


def teleport_to_witch_and_back(back_x, back_y):
    time.sleep(0.5)
    witch_area_x, witch_area_y = 1770, 465
    pyautogui.press("v")
    move_click(witch_area_x, witch_area_y)
    time.sleep(3)
    move_click(back_x, back_y)
    pyautogui.press("y")
    return time.time()
    
def teleport_to_shard_boss_and_back(back_x, back_y):
    time.sleep(0.5)
    boss_x, boss_y = 1770, 767
    time.sleep(0.5)
    pyautogui.press("v")
    time.sleep(0.5)
    move_click(boss_x, boss_y)
    time.sleep(8)
    move_click(back_x, back_y)
    time.sleep(0.5)
    pyautogui.press("y")
    time.sleep(0.5)
    return time.time()

cancel_coords = 1792 
gem_x_coord = 1252
start_button_x_coord = 2090
refresh_button_x_coord = 590
claim_button_x_coord = 2050
cancel_coord_list = [336, 456, 576, 696, 816, 936, 1056]
gui_button_y = 1160

cancel_color = (221, 26, 30)
cancel_color_2 = (221, 27, 31)
gem_color = (255, 0, 68)
gem_color_2 = (253, 1, 68)
cheese_color = (244, 180, 27)
beer_color = (174, 195, 190)
borb_color = (206, 245, 135)
basic_leaf_color = (62, 137, 72)
mulch_color = (20, 21, 41)
benitoite_color = (43, 120, 213)
benitoite_color_2 = (44, 120, 211)
obsidian_color = (34, 31, 71)
obsidian_color_2 = (35, 32, 71)
celestial_color = (118, 66, 138)
celestial_color_2 = (118, 66, 137)

current_material_list = [benitoite_color, benitoite_color_2, obsidian_color, obsidian_color_2, celestial_color, celestial_color_2]
gem_list = [gem_color, gem_color_2]
cancel_colors = [cancel_color, cancel_color_2]

witch_area_x, witch_area_y = 1770, 465
inner_pyramid_x, inner_pyramid_y = 1770, 329
dark_glade_x, dark_glade_y = 1770, 592
mountain_x, mountain_y = 1770, 485
biotite_x, biotite_y = 1770, 917



back_x, back_y = biotite_x, biotite_y

start_game = False
farm_bosses = True
kill_witch = True
kill_shard_boss = False

pyautogui.FAILSAFE = False
while True:
    if keyboard.is_pressed("o"):
        start_game = True
        if kill_witch:
            witch_start_time=teleport_to_witch_and_back(back_x, back_y)
        if kill_shard_boss:
            shard_boss_start_time = teleport_to_shard_boss_and_back(back_x, back_y)
    if start_game:
        if kill_witch:
            if time.time() - witch_start_time >= 60:
                witch_start_time=teleport_to_witch_and_back(back_x, back_y)

        if kill_shard_boss:
            if time.time() - shard_boss_start_time >= 180:
                shard_boss_start_time = teleport_to_shard_boss_and_back(back_x, back_y)

        if is_auto_refresh_text_present():
            pyautogui.scroll(-1)

        current_screen = ImageGrab.grab().load()
        for y_coord in cancel_coord_list:
            if current_screen[gem_x_coord, y_coord] in current_material_list:
                if current_screen[cancel_coords, y_coord] not in cancel_colors:
                    move_click(start_button_x_coord, y_coord)

        move_click(claim_button_x_coord, gui_button_y)
        move_click(refresh_button_x_coord, gui_button_y)

        if keyboard.is_pressed("p"):
            start_game =False
            