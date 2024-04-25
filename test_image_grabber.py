from PIL import ImageGrab
import time
cancel_coord_list = [336, 456, 576, 696, 816, 936, 1056]
coords = (1252, 576)
cancel_coords = (1792, 336)
time.sleep(3)
for coord_y in cancel_coord_list:
    print(ImageGrab.grab().load()[coords[0], coord_y])