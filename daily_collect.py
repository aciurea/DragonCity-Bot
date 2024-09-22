from mem_edit import Process
import psutil
from pyautogui import scroll

from close import check_if_ok
from move import moveAndClick, moveTo
from popup import Popup
from utils import delay, exists, getImagePositionRegion, get_screen_resolution
from screen import Screen
from position_map import Position_Map


class Daily_Collect:
    news_pos = Screen.get_pos([0.95572916, 0.2138])
    pos_to_start_scroll = Screen.get_pos([0.16979167, 0.151])
    claim_btn_pos = Screen.get_pos([0.6140625, 0.813])
    screen_res = get_screen_resolution()

    @staticmethod
    def collect():
        Daily_Collect._go_to_daily_streak()
        delay(5)

        daily_streak = Daily_Collect._get_daily_streak()

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

    def _get_daily_streak():
        base = './img/daily'
        path = f'{base}/{Daily_Collect.screen_res}_daily_streak.png'
        pos = [*Screen.get_pos([0.0859375, 0.109]), *Screen.get_pos([0.6, 1])]
        times = 10

        while times > 0:
            times -= 1
            daily_streak = getImagePositionRegion(path, *pos, 0.8, 1)
            if exists(daily_streak):
                return daily_streak
            else:
                moveTo(Daily_Collect.pos_to_start_scroll)
                scroll(-2_000)
                delay(.2)

    @staticmethod
    def _go_to_daily_streak():
        if not exists(Position_Map.center_map()):
            return check_if_ok()
        moveAndClick(Daily_Collect.news_pos)

    def _kill_browser():
        pid = Process.get_pid_by_name('brave.exe')
        if pid is not None:
            p = psutil.Process(pid)
            p.terminate()

    @staticmethod
    def _claim_items_from_browser():
        bbox = [0.45625, 0.83796296, 0.53802083, 0.9037037]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference('claimi', t['text']):
                moveAndClick(t['position'])
                delay(5)
                check_if_ok()
                Popup.check_popup_chest()
                Popup.check_popup_chest()
                break
