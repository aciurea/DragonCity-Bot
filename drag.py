import time
import pyautogui
from utils import getImagePositionRegion


def drag(center):
    island = getImagePositionRegion('./img/utils/center_island.png', 0, 0, 1600, 900)
    if (island[0] == -1):
        return print('Cannot move the map since there is no point of reference')

    pyautogui.moveTo(island)
    dragMap(center)


def dragMap(position):
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(position[0], position[1], .5)
    time.sleep(.5)
    pyautogui.mouseUp()


def dragMapToCenter(center=[800, 400]):
    print('Drag map to center')
    drag(center)


def getMovePositions():
    return [
        'down',
        'up',
    ]
