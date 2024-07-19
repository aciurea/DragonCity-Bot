import time

from pyautogui import scroll
from close import check_if_ok
from move import moveTo, multiple_click
from utils import moveAndClick, delay, exists
from position_map import Position_Map

class Shop:
    last_time_started = 0
    wait_time = 3600 * 3 
    pos = {
        "shop": [2440, 1250],
        "orbs": [1280, 1090],
        "vertical_scroll": [2560, 865],
        "buy_heroic": [2220, 670],
        "buy_legendary": [2215, 1190]
    }

    def go_to_orbs():
        scroll_pos = Shop.pos['vertical_scroll']
        moveTo(scroll_pos)
        scroll(-10_000)
        delay(.5)

    def open_shop():
        if time.time() - Shop.last_time_started < Shop.wait_time: return

        Position_Map.center_map()
        delay(1)
        moveAndClick(Shop.pos['shop'])
        delay(.5)
        moveAndClick(Shop.pos['orbs'])
        delay(.5)
        Shop.go_to_orbs()
        
        multiple_click(Shop.pos['buy_heroic'], 6)
        multiple_click(Shop.pos['buy_legendary'], 6)
        check_if_ok()
        Shop.last_time_started = time.time()