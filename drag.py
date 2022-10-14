import time
import pyautogui
from utils import getImagePosition


def drag(center):
    island = getImagePosition('./img/utils/center_island.png')
    if (island[0] == -1):
        return print('Cannot move the map since there is no point of reference')

    pyautogui.moveTo(island)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(center[0], center[1], 1)
    time.sleep(1)
    pyautogui.mouseUp()


def dragMap(position):
    center = [800, 400]

    # if (position == 'down'):
    #     center = [800, 400]
    # if (position == 'up'):
    #     center = [800, 500]
    drag(center)


def getMovePositions():
    return [
        'down',
        'up',
    ]
