import os
import psutil
import pyautogui
from screeninfo import get_monitors
import constants as C
from move import moveAndClick, moveTo
from timers import delay
from utils import exists, get_json_file, get_monitor_quarters, getImagePositionRegion, openChest
import time
import concurrent.futures
from mem_edit import Process
import datetime

jsonPos = get_json_file('open.json')

def close_app():
    try:
        pid = Process.get_pid_by_name('DragonCity.exe')
        if(pid == None): return
        p = psutil.Process(pid)
        p.terminate()
    except: print('Cannot kill the application')

def zoom_out():
    [ res ] = get_monitors()
    moveTo([res.width / 2, res.height / 2])
    pyautogui.scroll(-10000)

def open_app(i = 0):
    close_app()
    delay(2)
    if(i == 5):
        print('Cannot start the application ad ', datetime.datetime.now().strftime("%X"))
        return False
    
   # your app model id
    app_model_id="SocialPoint.DragonCityMobile_jahftqv9k5jer!App" 
    try: os.system(f'start shell:AppsFolder\\{app_model_id}')
    except: open_app(i+1)

    delay(15)
    _check_if_app_started()
    moveAndClick([10, 50])
    _close_all_the_windows()

def _get_btn():
    mon_quarters = get_monitor_quarters()
    top_right = mon_quarters['top_right']
    btns = [
        [C.APP_START_BIG_CLOSE, *top_right, 0.8, 2]
    ]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result_list = executor.map(lambda args: getImagePositionRegion(*args), btns)
        for close_btn in result_list:
            if exists(close_btn): return close_btn
        return [-1]

def _close():
    close_btn = _get_btn()
    if exists(close_btn):
        moveAndClick(close_btn)
    else:
        print('close button not found')
        moveAndClick(jsonPos["POPUP_ICON"])
        # openChest()
      
def _get_artifact():
    return getImagePositionRegion('./img/utils/artifact.png', 0, 0, 2600, 1600, 0.8, 2)

def _close_all_the_windows():
    start = time.time()
    app_time_to_close_all_buttons = 50
    zoom_out()
    while(not exists(_get_artifact())):
        if(time.time() - start > app_time_to_close_all_buttons): return open_app()
        _close()
        delay(2)

def _check_if_app_started():
    start = time.time()
    time_limit = 30
    while((time.time() - start) < time_limit):
        image = getImagePositionRegion(C.APP_START_STATIC, *jsonPos['APP_START_STATIC'])
        if exists(image): return image
        delay(1)
    return [-1]
