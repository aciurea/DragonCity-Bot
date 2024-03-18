from close import Close, check_if_ok
from move import fast_click, moveAndClick
from utils import delay, dragMapToCenter, exists, get_monitor_quarters, getImagePositionRegion, move_to_left
import constants as C
import mouse

class Habitat:
    mon_quarters = get_monitor_quarters()
    store_pos = [715, 1160]
    shop = [2440, 1250]
    habitats = [1260, 565]
    category = [2325, 1300]
    legendary = [1865, 1305]
    legendary_habitat = [1275, 1085]
    ok = [1395, 1265]
    cancel = [1153, 1255]
    habitats_on_map = [
                    [1817, 716],
                    [1844, 656],
                    [1929, 605],
                    [1874, 761],
                    [1925, 683],
                    [1989, 640],
                    [1947, 797], 
                    [1859, 857], 
                    [2065, 677], 
                    [2113, 727],
                ]
    height_diff = 35

    def prepare_habitat_to_buy(habitat_pos):
            dragMapToCenter()
            delay(.2)
            moveAndClick(dragMapToCenter())
            delay(1)
            actions = [Habitat.shop,Habitat.habitats, Habitat.category, Habitat.legendary, Habitat.legendary_habitat]
            for action in actions:
                moveAndClick(action)
                delay(.5)
            # click on current position, in order to be able to move the map
            fast_click(mouse.get_position())
            move_to_left()
            moveAndClick(habitat_pos)
            delay(.5)

    def buy_habitat():
        if not Habitat.store_habitat(): return

        for habitat_pos in Habitat.habitats_on_map:
            Habitat.prepare_habitat_to_buy(habitat_pos)
            moveAndClick(Habitat.ok)
        
    def store_habitat():
        Habitat.prepare_habitat_to_buy(Habitat.habitats_on_map[0])
        delay(.5)
        moveAndClick(Habitat.cancel)

        for habitat_pos in Habitat.habitats_on_map:
            # collect first
            moveAndClick([habitat_pos[0], habitat_pos[1] - Habitat.height_diff])
            delay(.5)
            if exists(Close.get_popup_red_btn()):
                check_if_ok()
                return False
            # store habitat
            info = getImagePositionRegion(C.HABITAT_INFO, *Habitat.mon_quarters['4thRow'], .8, 1)
            if exists(info):
                moveAndClick(info)
                delay(1)
                moveAndClick(Habitat.store_pos)
            delay(1)
        return True
