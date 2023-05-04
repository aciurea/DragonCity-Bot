from screeninfo import get_monitors
from breed import sellEgg
from freeze import _freeze_dragons, freeze_dragons
from utils import delay, getImagePositionRegion, moveTo
from extract_text import get_text
import mouse
import keyboard as K
import time
import pyautogui

from utilss.drag_map import dragMapToCenter

def moveY():
    delay(2)
    y = 0
    while(y < 901):
        moveTo([750, y])
        y += 100
        delay(.8)



def get_pos():
    start = time.time()
    while 1:
        if K.is_pressed('p'):  # if key 'q' is pressed 
            # collect_gems( dragMapToCenter())
            dragMapToCenter()
            # doHeroicRace()
            [ res ] = get_monitors()
            print('mouse pos',mouse.get_position())
            # _freeze_dragons(-1, get_text(oponent=True))
            # _freeze_dragons(999999991, get_text(oponent=False))
            # get_text()
        if K.is_pressed('q'):
            break  # if user pressed a key other than the given key the loop will break
         
        delay(.2)

get_pos()
