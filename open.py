import os
import psutil
import pyautogui
import time
import datetime
import concurrent.futures
from PIL import Image, ImageGrab

import constants as C

from screeninfo import get_monitors
from close import Close
from move import moveAndClick, moveTo
from popup import Popup
from timers import delay
from utils import exists, get_monitor_quarters, getImagePositionRegion, get_int, get_grid_monitor, get_screen_resolution
from mem_edit import Process
from mail import Mail
from screen import Screen
from position_map import Position_Map



mon_quarters = get_monitor_quarters()

class OpenApp:

    @staticmethod
    def open_app(i = 0):
        print('Started new cycle...')
        OpenApp._close_app()
        delay(2)
        if(i == 5):
            dd = datetime.datetime.now().strftime("%X")
            raise('[Error] Cannot start the application ' + dd)
        
        # your app model id
        app_model_id="SocialPoint.DragonCityMobile_jahftqv9k5jer!App" 
        try: os.system(f'start shell:AppsFolder\\{app_model_id}')
        except: OpenApp.open_app(i + 1)

        delay(10)
        OpenApp._check_if_app_started()
        OpenApp._clean_all_popups()

    @staticmethod
    def _close_app():
        try:
            pid = Process.get_pid_by_name('DragonCity.exe')
            if(pid == None): return
            p = psutil.Process(pid)
            p.terminate()
        except: print('Cannot kill the application')

    @staticmethod
    def _zoom_out():
        res = get_monitors()[0]
        moveTo([res.width / 2, res.height / 2])
        pyautogui.scroll(-10000)

    @staticmethod
    def _claim_reward_after_arena():
        bbox = [0.445703125, 0.60416, 0.551953125, 0.65]
        st = time.time()
        text_positions = Screen.get_text_pos(bbox, gray_mode=True)
        print('took time: ', time.time() - st)

        for t in text_positions:
            if Screen.is_match_with_one_difference('claimreward', t['text'].lower()):
                moveAndClick(t['position'])

    @staticmethod
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

    @staticmethod
    def _clean_all_popups():
        start = time.time()
        app_time_to_close_all_buttons = 40
        while(not exists(Position_Map._get_artifact_pos())):
            OpenApp._zoom_out()
            if(time.time() - start > app_time_to_close_all_buttons): 
                Popup.check_popup_chest()
                OpenApp._claim_reward_after_arena()
                return OpenApp.open_app()
            
            btns = Close.check_if_ok()
            Popup.check_popup_chest()
            delay(1)
            if len(btns) == 0:
                Close.get_lose_text()
                close_pos = Screen.get_pos([0.794270834, 0.0935185185])
                moveAndClick(close_pos)
                delay(.5)
            delay(1)
        Position_Map.center_map()
        print('APP STARTED SUCCESSFULY')
    