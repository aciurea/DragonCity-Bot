import os
import psutil
import pyautogui
from screeninfo import get_monitors
from close import Close
import constants as C
from move import _get_artifact_pos, moveAndClick, moveTo
from popup import Popup
from timers import delay
from utils import exists, get_monitor_quarters, getImagePositionRegion, get_int
import time
from mem_edit import Process
import datetime
import concurrent.futures
from mail import Mail

res = get_monitors()[0]

jsonPos = {
    "POPUP_ICON": [get_int(res.width * 0.82421875), get_int(res.height * 0.121527)],
    "STATIC_CLOSE": [2048, 135]
}

mon_quarters = get_monitor_quarters()

def _check_if_is_special_offer():
    clock = getImagePositionRegion(C.APP_START_CLOCK, *mon_quarters['1stVerHalf'], .8, 2)
    
    return clock

def close_app():
    try:
        pid = Process.get_pid_by_name('DragonCity.exe')
        if(pid == None): return
        p = psutil.Process(pid)
        p.terminate()
    except: print('Cannot kill the application')

def zoom_out():
    res = get_monitors()[0]
    moveTo([res.width / 2, res.height / 2])
    pyautogui.scroll(-10000)

def open_app(i = 0):
    print('Started new cycle...')
    close_app()
    delay(2)
    if(i == 5):
        dd = datetime.datetime.now().strftime("%X")
        Mail.send('Cannot start the application ' + dd, subject='[Error] START APPLICATION')
        return False
    
   # your app model id
    app_model_id="SocialPoint.DragonCityMobile_jahftqv9k5jer!App" 
    try: os.system(f'start shell:AppsFolder\\{app_model_id}')
    except: open_app(i+1)

    delay(10)
    _check_if_app_started()
    _clean_all_popups()

def check_extra_bonus():
    btns = [
        [C.APP_START_EXTRA_CLAIM, *mon_quarters['2ndHorHalf']],
        [C.APP_START_ENJOY_CLAIM, *mon_quarters['2ndHorHalf']],
        [C.APP_START_ARENA_CLAIM, *mon_quarters['2ndHorHalf']],
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), btns)
            for btn in result_list:
                if exists(btn): 
                    moveAndClick(btn)
                    return check_extra_bonus()
    return [-1]

def _click_on_enjoy():
    x_start = 920
    y_start = 980
    x_end = 1820
    y_end = 1370
    
    current_pos = [x_start, y_start]
    x_size = 90
    y_size = 50
    
    while current_pos[1] <= y_end:
        while current_pos[0] <= x_end:
            moveAndClick(current_pos)
            current_pos[0] += x_size

        current_pos[0] = x_start
        current_pos[1] += y_size
        

def _clean_all_popups():
    delay(1)
    start = time.time()
    app_time_to_close_all_buttons = 40
    while(not exists(_get_artifact_pos())):
        zoom_out()
        if(time.time() - start > app_time_to_close_all_buttons): 
            _click_on_enjoy()
            Popup.check_popup_chest()
            return open_app()
        
        if exists(_check_if_is_special_offer()):
            print('is special offer')
            moveAndClick(jsonPos["STATIC_CLOSE"])
            delay(1)
            continue
        
        close_btn = Close.get_btn()
        if exists(close_btn): 
            print('close btn clicked')
            moveAndClick(close_btn)
            delay(1)
            continue
        else: 
            print('STATIC closed')
            moveAndClick(jsonPos["POPUP_ICON"]) 
            delay(2)
            Close.check_if_ok()
            
        Popup.check_popup_chest()
        check_extra_bonus()
        _check_enjoy_btn()
        delay(2)

    print('APP STARTED SUCCESSFULY')

def _check_enjoy_btn():
    print('inside enjoy....')
    btn = getImagePositionRegion(C.APP_START_ENJOY, *mon_quarters['2ndHorHalf'], .8, 1)

    if exists(btn): moveAndClick(btn)
        
def _check_if_app_started():
    try:
        screeshot = pyautogui.screenshot(region=(0, 0, 200, 200))
        screeshot.save('screenshot.png')
        start = time.time()
        time_limit = 30
        while((time.time() - start) < time_limit):
            image = getImagePositionRegion("screenshot.png", 0, 0, 201, 201, .8, 1)
            if not exists(image):
                os.remove('screenshot.png')
                return [-1]
            delay(1)
    except Exception as e:
        delay(5)
        print(f'Error occurred: {str(e)}')

