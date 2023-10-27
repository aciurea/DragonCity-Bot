import mouse
import pyautogui
from screeninfo import get_monitors

from timers import delay
from utils import exists, get_int, getImagePosition

def moveTo(position):
    mouse.move(*position)
    delay(0.1)

def fast_click(pos):
    pyautogui.click(*pos)

def moveAndClick(pos, msg = 'Nothing to click'):
    if not exists(pos): return print(msg)
    moveTo(pos)
    pyautogui.leftClick()
    delay(0.05)

def move_to_top():
    artifact = center_map()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    _drag_map(artifact, [get_int(res.width / 2), get_int(res.height / 2) + 400])
    pyautogui.mouseUp()

def center_map():
    [res] = get_monitors()
    artifact = getImagePosition('./img/utils/artifact.png', 5, .8, .5)
    if(artifact[0] == get_int(res.width / 2) and artifact[1] == get_int(res.height / 2)):
        moveAndClick(artifact)
        return artifact

    if not exists(artifact):
        print('Cannot move the map since there is no point of reference')
        return [-1]
    print('artifact is ', artifact)
    _drag_map(artifact, [get_int(res.width / 2), get_int(res.height / 2)])
    return artifact
    
def move_to_bottom():
    artifact = center_map()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    _drag_map(artifact, [get_int(res.width / 2), get_int(res.height / 2) - 400])
    pyautogui.mouseUp()

def move_to_right():
    artifact = center_map()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    _drag_map(artifact, [get_int(res.width / 2) + 500, get_int(res.height / 2)])
    pyautogui.mouseUp()

def move_to_left():
    artifact = center_map()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    _drag_map(artifact, [get_int(res.width / 2) - 500, get_int(res.height / 2)])
    pyautogui.mouseUp()

def _drag_map(artifact, next = [800, 450]):
    pyautogui.moveTo(*artifact, 0)
    pyautogui.mouseDown(duration=1)
    pyautogui.moveTo(*next, 0)
    delay(1)
    pyautogui.mouseUp()
    delay(.5)
    pyautogui.mouseUp()