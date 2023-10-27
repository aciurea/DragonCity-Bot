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

def _get_artifact_pos():
    return getImagePosition('./img/utils/artifact.png', 5, .8, .5)

def center_map():
    [res] = get_monitors()
    artifact = _get_artifact_pos()
    if(artifact[0] == get_int(res.width / 2) and artifact[1] == get_int(res.height / 2)):
        moveAndClick(artifact)
        return artifact

    if not exists(artifact):
        print('Cannot move the map since there is no point of reference')
        return [-1]
    print('artifact is ', artifact)
    _drag_map(artifact, [get_int(res.width / 2), get_int(res.height / 2)])
    return artifact

def drag_map_to_the_top():
    artifact = _get_artifact_pos()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    next_pos = [get_int(res.width / 2), get_int(res.height / 2) - 300]
    _drag_map(artifact, next_pos)
    return next_pos
    
def drag_map_to_the_bottom():
    artifact = _get_artifact_pos()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    next_pos = [get_int(res.width / 2), get_int(res.height / 2) + 300]
    _drag_map(artifact, next_pos)
    return next_pos

def drag_map_to_the_right():
    artifact = center_map()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    next_pos = [get_int(res.width / 2) + 500, get_int(res.height / 2)]
    _drag_map(artifact, next_pos)
    return next_pos

def drag_map_to_the_left():
    artifact = center_map()
    if not exists(artifact): return [-1]
    print('move to bottom')
    [res] = get_monitors()
    next_pos = [get_int(res.width / 2) - 500, get_int(res.height / 2)]
    _drag_map(artifact, next_pos)
    return next_pos

def _drag_map(artifact, next = [800, 450]):
    pyautogui.moveTo(*artifact, 0)
    pyautogui.mouseDown()
    pyautogui.moveTo(*next, 0)
    delay(1)
    pyautogui.mouseUp()

def is_artifact_at_pos(pos):
    try:
        [x, y] = _get_artifact_pos()
        return x == pos[0] and y == pos[1]
    except: return False