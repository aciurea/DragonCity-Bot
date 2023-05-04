import subprocess
import pyautogui
from screeninfo import get_monitors
import constants as C
from utils import delay, exists, getImagePositionRegion, moveAndClick, moveTo, openChest
import time
import concurrent.futures
import subprocess


def close_app():
    try: subprocess.call("TASKKILL /F /IM DragonCity.exe", shell=False)
    except: print('Cannot kill the application')

def zoom_out():
    [ res ] = get_monitors()
    moveTo([res.width / 2, res.height / 2])
    pyautogui.scroll(-5000)

def open_app(tries = 0):
    if(tries > 5): return
    path = "C:\Program Files\WindowsApps\SocialPoint.DragonCityMobile_23.4.1.0_x86__jahftqv9k5jer\DragonCity\DragonCity.exe"
    close_app()
    delay(2)
    try: subprocess.Popen(path, shell=True)
    except: open_app(tries+1)

    print('App opened')
    _check_if_app_started()
    delay(3)
    _close_all_the_windows()

def _get_close_btn():
    buy_now_close_pos = [1270, 84]
    close_params = [
        [C.APP_START_BUY_NOW, 670, 720, 900, 820, 0.8, 1],
        [C.APP_START_BUY_NOW_2, 670, 720, 900, 820, 0.8, 1],
        [C.APP_START_RED_CLOSE,  1000, 0, 1400, 200, 0.8, 1],
        [C.APP_START_BIG_CLOSE,  2294, 0, 2538, 230, 0.8, 2],
        [C.APP_START_CLAIM_DAILY,  500, 650, 1000, 850, 0.8, 1],
        [C.APP_START_NO,  600, 0, 1400, 600, 0.8, 1],
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        buy_now_btn1, buy_now_btn2, *result_list = executor.map(lambda args: getImagePositionRegion(*args), close_params)
        if exists(buy_now_btn1) or exists(buy_now_btn2):
            return buy_now_close_pos
        for close_btn in result_list:
            if exists(close_btn): return close_btn
        return [2122, 156] # default close button 
   
def _get_artifact():
    return getImagePositionRegion('./img/utils/artifact.png', 370, 290, 1350, 830, 0.8, 2)

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
        moveAndClick(_get_close_btn())
        delay(2)

def _check_if_app_started():
    start = time.time()
    time_limit = 50
    while((time.time() - start) < time_limit):
        print('run')
        image = getImagePositionRegion(C.APP_START_STATIC, 0, 670, 225, 905, .8, 1) # update the start
        print(image)
        if exists(image): return image
        delay(1)
    return [-1]
