from utils import delay, exists, get_center, getImagePosition, moveAndClick, moveTo
import pyautogui

def dragMapToCenter():
    artifact = getImagePosition('./img/utils/artifact.png', 5, .8, .5)
    center = get_center()
    if(artifact[0] == center[0] and artifact[1] == center[1]):
        moveAndClick(artifact)
        return artifact

    if not exists(artifact):
        print('Cannot move the map since there is no point of reference')
        return [-1]
    drag_to(artifact, center)
    return artifact

def move_to_top():
    artifact = dragMapToCenter()
    if not exists(artifact): return
    delay(1)
    drag_to(artifact, [artifact[0], artifact[1]+300])

def move_to_bottom():
    artifact = dragMapToCenter()
    if not exists(artifact): return
    delay(1)
    drag_to(artifact, [artifact[0], artifact[1]-200])

def move_to(pos):
    pyautogui.mouseUp()
    pyautogui.moveTo(pos[0], pos[1], 0)

def drag_to(curr, next):
    pyautogui.moveTo(curr[0], curr[1], duration=0)
    delay(.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(next[0], next[1], duration=0)
    delay(.1)
    pyautogui.mouseUp()