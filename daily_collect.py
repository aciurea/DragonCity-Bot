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
    wait_time = 3600 * 4  

    def _get_daily_streak():
        grid = Daily_Collect.grid
        pos = [grid['x0'], grid["y0"], grid["x2"],grid["y6"]]

        return getImagePositionRegion(C.DAILY_STREAK, *pos, 0.8, 1)

    def _go_to_daily_streak():
        center_map()
        moveAndClick(Daily_Collect.news_pos)
        delay(2)
        moveTo(Daily_Collect.pos_to_start_scroll)
        
        scroll(-10_000)
        delay(.5)
        # scroll to the top

    def _kill_browser():
        pid = Process.get_pid_by_name('brave.exe')
        if(pid == None): return
        p = psutil.Process(pid)
        p.terminate()

    def _get_claim_btn_browser():
        mon = get_monitor_quarters()
        return getImagePositionRegion(C.DAILY_CLAIM_BROWSER, *mon['full'], .8, 1)

    def _get_claim_after_browser():
        mon = get_monitor_quarters()
        return getImagePositionRegion(C.DAILY_CLAIM_AFTER_BROWSER, *mon['4thRow'], .8, 1)

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
            if not exists(claim_btn):
                delay(1)
                check_if_ok()
                Daily_Collect._kill_browser()
                return
              
            multiple_click(claim_btn, 10)
            Daily_Collect._kill_browser()
          
            delay(10)
            check_if_ok()
            collect_food()
            collect_food()
            moveAndClick(Daily_Collect._get_claim_after_browser())
            collect_food()
            Popup.check_popup_chest()
            check_if_ok()
        Daily_Collect.last_time_started = time.time()