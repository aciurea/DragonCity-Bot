from screeninfo import get_monitors
# from breed import sellEgg
# from utils import delay, moveTo
import mouse
import keyboard as K
import time
import pyautogui
from arena import Arena, Battle
from breed import Breed
from collectFood import heroic_collect

from move import moveAndClick
from utils import dragMapToCenter

def delay(seconds):
    if seconds < 0:
        seconds = 0
    time.sleep(seconds)

def moveY():
    delay(2)
    y = 0
    while(y < 901):
        # moveTo([750, y])
        y += 100
        delay(.8)

def get_pos():
    start = time.time()
    while 1:

        if K.is_pressed('n'):
            arr = [1, 2, 3, 4, 5]
            print(arr[1::])
            print(arr[1::-1])
            print(arr[2::-1])
            print(arr[0::-1])
        if K.is_pressed('m'):
            # heroic_collect()
            Breed.breed('feed')
        if K.is_pressed('c'):
            dragMapToCenter()
        if K.is_pressed('p'):  # if key 'q' is pressed 
          
            # [ res ] = get_monitors()
            # print(res.width, res.height, res.width_mm, res.height_mm)
            print('mouse pos',mouse.get_position())
          
            # print(Battle.is_fight_in_progress())
            # print(get_text(oponent=False))
            # print(get_text(oponent=True))
            # _freeze_dragons(-1, 313707)
            # _freeze_dragons(999999991, 285192)
            # get_text()
        # if K.is_pressed('t'):
        #     print(get_text())
        if K.is_pressed('s'):
            Arena.skip_strong_dragons()
        if K.is_pressed('q'):
            break  # if user pressed a key other than the given key the loop will break
         
        delay(.2)

get_pos()
