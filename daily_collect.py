import time
from mem_edit import Process
import psutil
from pyautogui import scroll

from close import check_if_ok
from collectFood import collect_food
from move import center_map, moveAndClick, moveTo, multiple_click
from popup import Popup
from utils import delay, exists, get_grid_monitor, get_monitor_quarters, getImagePositionRegion
from screen import Screen
import constants as C


class Daily_Collect:
    claim_btn_pos = [1548, 1178]
    news_pos = [2443, 297]
    pos_to_start_scroll = [442, 1243]
    grid = get_grid_monitor()
    wait_time = 3600 * 2  

    def _get_daily_streak(times = 10):
        if(times == 0): return [-1]
        pos = [
            Daily_Collect.grid['x0'],
            Daily_Collect.grid["y0"],
            Daily_Collect.grid["x2"],
            Daily_Collect.grid["y6"]
        ]

        daily_streak = getImagePositionRegion(C.DAILY_STREAK, *pos, 0.8, 1)
        if(exists(daily_streak)): return daily_streak
        else:
            moveTo(Daily_Collect.pos_to_start_scroll)
            scroll(-1_000)
            return Daily_Collect._get_daily_streak(times - 1)

    def _go_to_daily_streak():
        if not exists(center_map()):
            return check_if_ok()
        moveAndClick(Daily_Collect.news_pos)
        delay(2)

    def _kill_browser():
        pid = Process.get_pid_by_name('brave.exe')
        if(pid == None): return
        p = psutil.Process(pid)
        p.terminate()

    def _get_claim_btn_browser(times = 10, amount=300):
        if times == 0: return [-1]
        mon = get_monitor_quarters()
        daily_claim = getImagePositionRegion(C.DAILY_CLAIM_BROWSER, *mon['full'], .8, 1)
        if exists(daily_claim): return daily_claim
        else:
            scroll(-amount)
            return Daily_Collect._get_claim_btn_browser(times - 1)

    def _get_claim_after_browser():
        mon = get_monitor_quarters()
        return getImagePositionRegion(C.DAILY_CLAIM_AFTER_BROWSER, *mon['4thRow'], .8, 1)
    
    def _get_store_btn():
        mon = get_monitor_quarters()
        return getImagePositionRegion(C.DAILY_STORE, *mon['1stRow'], .8, 1)

    def _get_daily_streak_browser():
        mon = get_monitor_quarters()
        return getImagePositionRegion(C.DAILY_BROWSER, *mon['1stRow'], .8, 1)

    def collect():
        Daily_Collect._go_to_daily_streak()
        delay(3)
        daily_streak = Daily_Collect._get_daily_streak(times= 20)

        if exists(daily_streak):
            moveAndClick(daily_streak)
            delay(1)
            
            moveAndClick(Daily_Collect.claim_btn_pos)
            delay(15)
            
            Daily_Collect._kill_browser()
            delay(1)
            
            check_if_ok()
            delay(15)
            Daily_Collect._claim_items_from_browser()
            check_if_ok()
            
    @staticmethod
    def _claim_items_from_browser():
        bbox = [0.45625, 0.83796296, 0.53802083, 0.9037037]
        text_positions = Screen.get_text_pos(bbox)
        
        for t in text_positions:
            if Screen.is_match_with_one_difference('claimi', t['text']):
                moveAndClick(t['position'])
                delay(3)
                Popup.check_popup_chest()
                Popup.check_popup_chest()
                break

