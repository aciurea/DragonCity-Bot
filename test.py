from freeze import freeze_dragons
from towers import collect_gems
from utils import delay, dragMapToCenter, exists, get_text, getImagePositionRegion, moveTo
import mouse
import keyboard as K
from pynput import keyboard
import time

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
            # dragMapToCenter()
            print('mouse pos',mouse.get_position())
            # get_text()
        if K.is_pressed('t'):
            print(get_text())
        if K.is_pressed('l'):
            freeze_dragons()
            print()
        if K.is_pressed('s'):
            print(time.time() - start)
        if K.is_pressed('q'):
            break  # if user pressed a key other than the given key the loop will break
         
        delay(.2)

get_pos()
