import os
import psutil
import pyautogui
import datetime
import pygetwindow as gw

from screeninfo import get_monitors
from close import Close
from move import moveAndClick, moveTo
from popup import Popup
from timers import delay
from utils import exists
from mem_edit import Process
from screen import Screen
from position_map import Position_Map

text = {
    'claim': 'claim',
    'ClaimReward': 'ClaimReward',
}


class OpenApp:
    @staticmethod
    def open_app(i=0):
        print('Started new cycle...')
        OpenApp._close_app()
        delay(2)
        if i == 5:
            dd = datetime.datetime.now().strftime("%X")
            raise f'[Error] Cannot start the application {dd}'

        # your app model id
        app_model_id = "SocialPoint.DragonCityMobile_jahftqv9k5jer!App"
        try:
            os.system(f'start shell:AppsFolder\\{app_model_id}')
            delay(5)
            OpenApp._check_if_app_started()
            OpenApp._clean_all_popups()
        except Exception as e:
            OpenApp.open_app(i + 1)
            print(e)

    @staticmethod
    def _close_app():
        try:
            pid = Process.get_pid_by_name('DragonCity.exe')
            if not pid: return
            p = psutil.Process(pid)
            p.terminate()
        except Exception as e: print('Cannot kill the application', e)

    @staticmethod
    def _zoom_out():
        res = get_monitors()[0]
        moveTo([res.width / 2, res.height / 2])
        pyautogui.scroll(-10000)

    @staticmethod
    def _claim_reward_after_arena():
        bbox = [0.445703125, 0.60416, 0.551953125, 0.65]
        text_positions = Screen.get_text_pos(bbox, gray_mode=True)

        for t in text_positions:
            if Screen.is_match(text['ClaimReward'], t['text']):
                moveAndClick(t['position'])

    @staticmethod
    def _check_if_app_started():
        bbox = [0, 0.9129, 0.0671875, 0.9537]
        text_positions = Screen.get_text_pos(bbox)
        retries = 30

        # wait until reads a text.
        while len(text_positions) == 0:
            delay(1)
            text_positions = Screen.get_text_pos(bbox)
            retries -= 1
            if retries == 0:
                raise Exception('Cannot start the application')

        retries = 180
        while retries > 0:
            retries -= 1
            for t in text_positions:
                if Screen.is_match('version', t['text']):
                    delay(1)
                    break
                else: return
            text_positions = Screen.get_text_pos(bbox)

    @staticmethod
    def _clean_all_popups():
        retries = 30

        while not OpenApp._cleared_all_popups():
            OpenApp._zoom_out()
            if retries == 0: return OpenApp.open_app()
            btns = Close.check_if_ok()

            if len(btns) == 0:
                Popup.check_popup_chest()
                OpenApp._claim_daily_reward()

                Popup._enjoy()
                OpenApp._claim_reward_after_arena()
                OpenApp._claim_after_browser()
                Close.check_lose_text()
                close_pos = Screen.get_pos([0.794270834, 0.0935185185])
                moveAndClick(close_pos)
            OpenApp._check_dc_in_foreground()
            retries -= 1
        Position_Map.center_map()
        print('APP STARTED SUCCESSFULY')

    @staticmethod
    def _cleared_all_popups():
        retries = 5
        while retries > 0:
            if not exists(Position_Map._get_artifact_pos()): return False
            delay(1)
            retries -= 1
        return True

    @staticmethod
    def _claim_daily_reward():
        bbox = [0.4645835, 0.8083, 0.5328125, 0.8612]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claim'], t['text']):
                moveAndClick(t['position'])

    @staticmethod
    def _claim_after_browser():
        bbox = [0.45625, 0.83796296, 0.53802083, 0.9037037]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match('claimi', t['text']):
                moveAndClick(t['position'])
                delay(3)
                Close.check_if_ok()
                delay(1)
                Popup.check_popup_chest()
                delay(3)
                Popup.check_popup_chest()

    @staticmethod
    def _check_dc_in_foreground():
        active_window = gw.getActiveWindow()
        if active_window is None: return

        if active_window.title is not None and active_window.title != 'Dragon City':
            active_window.close()
