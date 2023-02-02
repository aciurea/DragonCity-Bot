import subprocess
from AppOpener import run
import pyautogui
import constants as C
from utils import delay, exists, getImagePositionRegion, moveAndClick, openChest
import time
import concurrent.futures

def close_app():
    try:
        subprocess.call("TASKKILL /F /IM DragonCity.exe", shell=False)
    except: print('Cannot kill the application')

def zoom_out():
    pyautogui.scroll(-5000)

def open_app():
    close_app()
    try:
        run("Dragon City")
    except: open_app()
    _check_if_app_started()
    moveAndClick([10, 50])
    delay(3)
    _close_all_the_windows()

def _get_close_btn():
    buy_now_close_pos = [1270, 84]
    close_params = [
        [C.APP_START_BUY_NOW, 670, 720, 900, 820, 0.8, 2],
        [C.APP_START_BUY_NOW_2, 670, 720, 900, 820, 0.8, 2],
        [C.APP_START_RED_CLOSE,  1000, 0, 1400, 200, 0.8, 2],
        [C.APP_START_BIG_CLOSE,  1400, 0, 1550, 50, 0.8, 2],
        [C.APP_START_CLAIM_DAILY,  500, 650, 1000, 850, 0.8, 2],
        [C.APP_START_NO,  600, 0, 1400, 600, 0.8, 2],
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        buy_now_btn1, buy_now_btn2, *result_list = executor.map(lambda args: getImagePositionRegion(*args), close_params)
        if exists(buy_now_btn1) or exists(buy_now_btn2):
            print('Buy now found') 
            return buy_now_close_pos
        for close_btn in result_list:
            if exists(close_btn): return close_btn
        return [-1]
   
def _close():
    close_btn = _get_close_btn()
    moveAndClick([1270, 84])
    while(exists(close_btn)):
        moveAndClick(close_btn)
        delay(.5)
        close_btn = _get_close_btn()
    return close_btn

def _get_artifact():
    artifacts_list = [
        ['./img/utils/artifact.png', 370, 290, 1350, 830, 0.8, 2],
        ['./img/utils/artifact_2.png', 370, 290, 1350, 830, 0.8, 2]
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        result_list = executor.map(lambda args: getImagePositionRegion(*args), artifacts_list)
        for artifact in result_list:
            if exists(artifact): return artifact
        return [-1]

def _retry_to_open_app(start_time):
    if (time.time() - start_time > 50):
        close_app()
        delay(5)
        open_app()

def _close_all_the_windows():
    start = time.time()
    while(not exists(_get_artifact())):
        _retry_to_open_app(start)
        zoom_out()
        if not exists(_close()):
            openChest()
        delay(1.5)

def _check_if_app_started():
    start = time.time()
    time_limit = 50
    while((time.time() - start) < time_limit):
        image = getImagePositionRegion(C.APP_START_STATIC, 0, 380, 120, 530, .8, 1)
        if exists(image): return image
        delay(1)
    return [-1]
