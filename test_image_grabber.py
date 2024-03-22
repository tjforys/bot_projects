from PIL import ImageGrab
import time

coords = (1252, 816)
time.sleep(3)
print(ImageGrab.grab().load()[coords[0], coords[1]])