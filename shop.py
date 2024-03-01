from close import check_if_ok
from move import fast_click
from utils import dragMapToCenter, get_json_file, moveAndClick, delay, scroll

class Shop:
    pos = get_json_file('shop.json')

    def buy_orbs(key):
        times = 6
        while times > 0:
            times -= 1
            fast_click(Shop.pos[key])

    def go_to_orbs():
        scroll_pos = Shop.pos['vertical_scroll']
        scroll(scroll_pos, [0, scroll_pos[1]])
        delay(1)
        fast_click([0, scroll_pos[1]])

    def open_shop():
        dragMapToCenter()
        moveAndClick(Shop.pos['shop'])
        delay(.5)
        moveAndClick(Shop.pos['orbs'])
        delay(.5)
        Shop.go_to_orbs()
        
        delay(1)

        Shop.buy_orbs('buy_heroic')
        Shop.buy_orbs('buy_legendary')
        check_if_ok()