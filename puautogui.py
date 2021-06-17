from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *

replaybut = (639, 410)
dinosaur = (415, 486)

def resetgame():
    pyautogui.click(replaybut)
def image():
    box = (dinosaur[0] + 55,dinosaur[1],dinosaur[0] + 145,dinosaur[1] + 5)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())
def pressSpace():
    pyautogui.press("space")
    time.sleep(0.1)


time.sleep(4)
resetgame()
while True:
    image()
    if (image() != 697):
        pressSpace()
        time.sleep(0.1)
