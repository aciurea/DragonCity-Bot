import mouse
import pyautogui

from utils import exists, delay


def moveTo(position):
    mouse.move(*position)
    delay(0.2)


def fast_click(pos):
    pyautogui.click(*pos)


def multiple_click(pos, times=5, time_between_clicks=0.1):
    mouse.move(*pos)
    delay(.05)

    while times > 0:
        fast_click(pos)
        delay(time_between_clicks)
        times -= 1


def multiple_fn(times=5, fn=lambda: None, time_between_clicks=0.1):
    while times > 0:
        moveAndClick(fn(), msg=f'{str(fn.__name__)} not found')
        delay(time_between_clicks)
        times -= 1


def moveAndClick(pos, msg='Nothing to click'):
    if not exists(pos): return print(msg)
    moveTo(pos)
    fast_click(pos)
    delay(0.1)


def drag_to(curr, next):
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(*curr)
    pyautogui.dragTo(next[0], next[1], 0.2)
    delay(.1)
