import time
from close import Close, check_if_ok
from move import fast_click, moveAndClick, multiple_click
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
    last_time_started = 0
    wait_time = 3600 * 3
    habitats_on_map = [
                    [1757, 707],
                    [1803, 638],
                    [1868, 604],
                    [1809, 749],
                    [1856, 679],
                    [1968, 625],
                    [1896, 790],
                    [1937, 726],
                    [2002, 681],
                    [2046, 742],
                    [2075, 648]
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
            delay(.5)
            move_to_left()
            moveAndClick([habitat_pos[0], habitat_pos[1]])
            delay(.5)

    def buy_habitat():
        if time.time() - Habitat.last_time_started < Habitat.wait_time: return

        # TODO check the claim btn when leveling up
        if not Habitat.store_habitat(): return

        for habitat_pos in Habitat.habitats_on_map:
            Habitat.prepare_habitat_to_buy(habitat_pos)
            moveAndClick(Habitat.ok)
        Habitat.last_time_started = time.time()

    def get_continue():
        return getImagePositionRegion(C.HABITAT_CONTINUE, *Habitat.mon_quarters['4thRow'], .8, 1)

    def store_habitat():
        Habitat.prepare_habitat_to_buy(Habitat.habitats_on_map[0])
        delay(.5)
        moveAndClick(Habitat.cancel)

        for habitat_pos in Habitat.habitats_on_map:
            # collect first
            moveAndClick([habitat_pos[0], habitat_pos[1] - Habitat.height_diff])
            delay(1)
            if exists(Close.get_popup_red_btn()):
                check_if_ok()
                return False
            
            multiple_click([habitat_pos[0], habitat_pos[1] - Habitat.height_diff], times=5)

            continue_btn = Habitat.get_continue()
            if exists(continue_btn):
                moveAndClick(continue_btn)
                check_if_ok()
                delay(.5)
                multiple_click([habitat_pos[0], habitat_pos[1] - Habitat.height_diff], times=5)


            # store habitat
            info = getImagePositionRegion(C.HABITAT_INFO, *Habitat.mon_quarters['4thRow'], .8, 1)
            if exists(info):
                moveAndClick(info)
                delay(1)
                moveAndClick(Habitat.store_pos)
            delay(1)
        return True
