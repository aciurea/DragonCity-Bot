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
        found_daily_btn = False        
        Daily_Collect._go_to_daily_streak()
        daily_streak = Daily_Collect._get_daily_streak()

        if exists(daily_streak):
            moveAndClick(daily_streak)
            delay(1)
            moveAndClick(Daily_Collect.claim_btn_pos)
            delay(5)
            daily_browser = Daily_Collect._get_daily_streak_browser()

            if exists(daily_browser):
                print('Found daily browser')
                moveAndClick(daily_browser)
                delay(3)
            claim_btn = Daily_Collect._get_claim_btn_browser()

            if exists(claim_btn): 
                found_daily_btn = True
                multiple_click(claim_btn, 2)
                delay(2)
                multiple_click(claim_btn, 2)
               
            store_btn = Daily_Collect._get_store_btn()
            if exists(store_btn):
                multiple_click(store_btn)
                delay(5)
                scroll(3000)
            free_daily_claim_btn = Daily_Collect._get_claim_btn_browser(times=20, amount=1_000)
            if exists(free_daily_claim_btn): 
                found_daily_btn = True
                multiple_click(free_daily_claim_btn, 2)
                delay(2)

            Daily_Collect._kill_browser()
            if found_daily_btn == False:
                check_if_ok()
                return
            delay(10)
            Daily_Collect.wait_to_claim()
            Daily_Collect.wait_to_claim()
          
    def wait_to_claim():
        Popup.check_popup_chest()
        check_if_ok()

        times = 5
        claim_after_browser = Daily_Collect._get_claim_after_browser()

        while not exists(claim_after_browser) and times > 0:
            print('I am here...')
            collect_food()
            delay(29)
            times -= 1
            delay(10)
            Popup.check_popup_chest()
            check_if_ok()
            times -= 1
        moveAndClick(claim_after_browser)
        Popup.check_popup_chest()
        check_if_ok()
        
