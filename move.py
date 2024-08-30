import mouse
import pyautogui
from screeninfo import get_monitors
import time

from timers import delay
from utils import exists, get_int, getImagePosition

res = get_monitors()[0]

def moveTo(position):
    mouse.move(*position)
    delay(0.2)

def fast_click(pos):
    pyautogui.click(*pos)

def multiple_click(pos, times=5, time_between_clicks=0.1):
    while times > 0:
        fast_click(pos)
        delay(time_between_clicks)
        times -= 1
        
def multiple_fn(times=5, fn=lambda: None, time_between_clicks=0.1):
    while times > 0:
        moveAndClick(fn(), msg = str(fn.__name__) + ' not found')
        delay(time_between_clicks)
        times -= 1

def moveAndClick(pos, msg = 'Nothing to click'):
    if not exists(pos): return print(msg)
    moveTo(pos)
    fast_click(pos)
    delay(0.1)

def _get_artifact_pos():
    return getImagePosition('./img/utils/artifact.png', 1, .8, .5)

def is_artifact_visible():
    return exists(_get_artifact_pos())

def center_map():
    moveTo([1,1])
    artifact = _get_artifact_pos()
    if(artifact[0] == get_int(res.width / 2) and artifact[1] == get_int(res.height / 2)):
        moveAndClick(artifact)
        return artifact

    if not exists(artifact):
        print('Cannot move the map since there is no point of reference')
        return [-1]
    _drag_map(artifact, [get_int(res.width / 2), get_int(res.height / 2)])
    return artifact

def _drag_map(artifact, next = [800, 450]):
    pyautogui.moveTo(*artifact, 0)
    pyautogui.mouseDown()
    pyautogui.moveTo(*next, 0)
    delay(1)
    pyautogui.mouseUp()
    delay(0.01)
    pyautogui.mouseUp()

def is_artifact_at_pos(pos):
    try:
        [x, y] = _get_artifact_pos()
        return x == pos[0] and y == pos[1]
    except: return False

def drag_to(curr, next):
    pyautogui.moveTo(*curr)
    pyautogui.dragTo(next[0], next[1], 0.2)
    delay(.1)