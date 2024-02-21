import os
import psutil
import pyautogui
from screeninfo import get_monitors
import constants as C
from move import _get_artifact_pos, moveAndClick, moveTo
from timers import delay
from utils import exists, get_json_file, get_monitor_quarters, get_screen_resolution, getImagePositionRegion, openChest
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

    delay(10)
    _check_if_app_started()
    _clean_all_popups()

def _get_btn():
    # TODO check this if it has the right icons to click on 
    # VIP buttons
    # Wizzard's hollow big button
    
    mon_quarters = get_monitor_quarters()
    top_right = mon_quarters['top_right']
    high_priority_btns = [
        [C.APP_CLOSE_DIVINE, *top_right],
        [C.APP_CLOSE_GEMS, *top_right],
        [C.APP_CLOSE_PIGGY, *top_right],
        [C.APP_CLOSE_SETTINGS, *top_right],
        [C.APP_CLOSE_TOWER, *top_right],
    ]
    lower_priority_btns = [[C.APP_CLOSE_OFFERS, *top_right]]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for b in [high_priority_btns, lower_priority_btns]:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), b)
            for close_btn in result_list:
                if exists(close_btn): return close_btn
        return [-1]

def _clean_all_popups():
    start = time.time()
    app_time_to_close_all_buttons = 50
    while(not exists(_get_artifact_pos())):
        if(time.time() - start > app_time_to_close_all_buttons): return open_app()
        close_btn = _get_btn()
        if(exists(close_btn)): moveAndClick(close_btn)
        else: moveAndClick(jsonPos["POPUP_ICON"])
        
        # TODO: check if the chest is open
        # openChest()
        delay(2)
        zoom_out()
    print('APP STARTED SUCCESSFULY')

def _check_if_app_started():
    screeshot = pyautogui.screenshot(region=(0, 0, 200, 200))
    screeshot.save('screenshot.png')
    start = time.time()
    time_limit = 30
    while((time.time() - start) < time_limit):
        image = getImagePositionRegion("screenshot.png", 0, 0, 200, 200, .8)
        if not exists(image):
            os.remove('screenshot.png')
            return [-1]
        delay(1)


# _clean_all_popups()