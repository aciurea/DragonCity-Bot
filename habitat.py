from close import check_if_ok
from move import moveAndClick
from utils import delay, dragMapToCenter, exists, get_monitor_quarters, getImagePositionRegion, move_to_left
import constants as C

class Habitat:
    mon_quarters = get_monitor_quarters()
    sell_pos = [715, 1160]
    shop = [2440, 1250]
    habitats = [1260, 565]
    category = [2325, 1300]
    legendary = [1865, 1305]
    legendary_habitat = [1275, 1085]
    ok = [1395, 1265]
    cancel = [1153, 1255]
    habitats_on_map = [[1982, 1056], [1912, 1110], [1838, 1138],[1762, 1172], [1884, 1012], [1766, 1102], [1700, 1133], [1816, 1051], [1707, 1033], [1770, 1000]]


    def prepare_habitat_to_buy(habitat_pos):
            moveAndClick(dragMapToCenter())
            delay(1)
            actions = [Habitat.shop, Habitat.habitats, Habitat.category, Habitat.legendary, Habitat.legendary_habitat]
            for action in actions:
                moveAndClick(action)
                delay(.5)
            move_to_left()
            moveAndClick(habitat_pos)
            delay(.5)

    def buy_habitat():
        if not Habitat.sell_habitat(): return
        for habitat_pos in Habitat.habitats_on_map:
            Habitat.prepare_habitat_to_buy(habitat_pos)
            moveAndClick(Habitat.ok)

    def sell_habitat():
        Habitat.prepare_habitat_to_buy(Habitat.habitats_on_map[0])
        delay(.5)
        moveAndClick(Habitat.cancel)
        for habitat_pos in Habitat.habitats_on_map:
            moveAndClick(habitat_pos)
            info = getImagePositionRegion(C.HABITAT_INFO, *Habitat.mon_quarters['4thRow'], .8, 1)
            if not exists(info):
                check_if_ok()
                return False
            moveAndClick(info)
            delay(.5)
            moveAndClick(Habitat.sell_pos)
        return True
