import time
from mem_edit import Process
import psutil
from pyautogui import scroll

from close import check_if_ok
from collectFood import collect_food
from move import center_map, moveAndClick, moveTo, multiple_click
from popup import Popup
from utils import delay, exists, get_grid_monitor, get_monitor_quarters, getImagePositionRegion
import constants as C


class Daily_Collect:
    claim_btn_pos = [1548, 1178]
    news_pos = [2443, 297]
    pos_to_start_scroll = [442, 1243]
    grid = get_grid_monitor()
    last_time_started = 0
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
        center_map()
        moveAndClick(Daily_Collect.news_pos)
        delay(2)

    def _kill_browser():
        pid = Process.get_pid_by_name('brave.exe')
        if(pid == None): return
        p = psutil.Process(pid)
        p.terminate()

    def _get_claim_btn_browser(times = 5, amount=500):
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
        return getImagePositionRegion(C.DAILY_STORE, *mon['full'], .8, 1)

    def collect():
        if time.time() - Daily_Collect.last_time_started < Daily_Collect.wait_time: return
        print('Tried to collect the daily streak')
        
        Daily_Collect._go_to_daily_streak()
        daily_streak = Daily_Collect._get_daily_streak()

        if exists(daily_streak):
            moveAndClick(daily_streak)
            delay(1)
            moveAndClick(Daily_Collect.claim_btn_pos)
            delay(5)
            claim_btn = Daily_Collect._get_claim_btn_browser()

            if exists(claim_btn): 
                multiple_click(claim_btn, 2)
                delay(2)
                multiple_click(claim_btn, 2)
               
            store_btn = Daily_Collect._get_store_btn()
            if exists(store_btn):
                multiple_click(store_btn)
                delay(5)
                scroll(10_000)
                multiple_click(Daily_Collect._get_claim_btn_browser(times=7, amount=2_000), 2)
            Daily_Collect._kill_browser()
            delay(10)
            Popup.check_popup_chest()
            check_if_ok()
            collect_food()
            collect_food()
            moveAndClick(Daily_Collect._get_claim_after_browser())
            collect_food()
            Popup.check_popup_chest()
            check_if_ok()
        Daily_Collect.last_time_started = time.time()
