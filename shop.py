import time

from pyautogui import scroll
from close import check_if_ok
from move import center_map, moveTo, multiple_click
from utils import get_json_file, moveAndClick, delay, exists

class Shop:
    last_time_started = 0
    wait_time = 3600 * 3 
    pos = get_json_file('shop.json')

    def go_to_orbs():
        scroll_pos = Shop.pos['vertical_scroll']
        moveTo(scroll_pos)
        scroll(-10_000)
        delay(.5)

    def open_shop():
        if time.time() - Shop.last_time_started < Shop.wait_time: return

        if not exists(center_map()):
           return check_if_ok()
        moveAndClick(Shop.pos['shop'])
        delay(.5)
        moveAndClick(Shop.pos['orbs'])
        delay(.5)
        Shop.go_to_orbs()
        
        multiple_click(Shop.pos['buy_heroic'], 6)
        multiple_click(Shop.pos['buy_legendary'], 6)
        check_if_ok()
        Shop.last_time_started = time.time()