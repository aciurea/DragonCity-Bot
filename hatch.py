from screeninfo import get_monitors
from close import check_if_ok
from move import center_map, moveAndClick
import constants as C
from timers import delay

from utils import exists, get_int, getImagePositionRegion

class Hatch:
    [res] = get_monitors()
    hatchery_pos = [get_int(0.346153 * res.width), get_int(0.639375 * res.height)]
    terra_pos = [get_int(0.625 * res.width), get_int(0.704375 * res.height)]
    # dragon_pos_in_habitat = [get_int(0.544230769 * res.width), get_int(0.849375 * res.height)]
    sell_egg_btn_from_habitat = [get_int(0.82461538 * res.width), get_int(0.89125 * res.height)]
    confirm_sell_btn = [get_int(0.55730769 * res.width), get_int(0.676875*res.height)]
    place_btn_pos = [get_int(0.52961538 * res.width), get_int(0.6875 * res.height)]

    def _get_terra_egg():
        y_start = get_int(0.778125 * Hatch.res.height)
        return getImagePositionRegion(C.BREED_TERRA_EGG, 0, y_start, Hatch.res.width, Hatch.res.height, .8, 3)


    def sell_egg():
        egg = Hatch._get_terra_egg()
        if exists(egg):
            moveAndClick(egg)
            #sell
            delay(1)
            moveAndClick([get_int(0.681153846 * Hatch.res.width),  get_int(0.6825 * Hatch.res.height)])
            delay(1)
            # confirm sell
            moveAndClick([get_int(0.5526923 * Hatch.res.width), get_int(0.685625 * Hatch.res.height)])
            return Hatch.sell_egg()

    def _sell_dragon():
        delay(.3)
        y_start = get_int(0.778125 * Hatch.res.height)
        dragon_pos_in_habitat = getImagePositionRegion(C.HATCH_DRAGON, 0, y_start, Hatch.res.width, Hatch.res.height, .8, 1)
        if exists(dragon_pos_in_habitat):
            moveAndClick(dragon_pos_in_habitat)
            delay(.5)
            moveAndClick(Hatch.sell_egg_btn_from_habitat)
            delay(.5)
            moveAndClick(Hatch.confirm_sell_btn)
            return Hatch._sell_dragon()
      
    def _clear_hatchery_with_dragon_placement():
        hatchery_pos_from_habitat = [get_int(0.6596153* Hatch.res.width), get_int(0.636875 * Hatch.res.height)]
        check_if_ok()
        moveAndClick(hatchery_pos_from_habitat)
        egg = Hatch._get_terra_egg()
        habitat_pos_after_sell = [get_int(0.63153846 * Hatch.res.width), get_int(0.714375 * Hatch.res.height)]
        if exists(egg):
            moveAndClick(egg)
            delay(.3)
            moveAndClick(Hatch.place_btn_pos)
            delay(1)
            moveAndClick(habitat_pos_after_sell)
            return Hatch._clear_hatchery_with_dragon_placement()

        moveAndClick(habitat_pos_after_sell)
        delay(.3)
        Hatch._sell_dragon()
        
    def place_egg():
        center_map()
        moveAndClick(Hatch.hatchery_pos)
        egg = Hatch._get_terra_egg()
        if exists(egg):
            moveAndClick(egg)
            delay(.5)
            moveAndClick(Hatch.place_btn_pos)
            delay(2)
            moveAndClick(Hatch.terra_pos)
            Hatch._sell_dragon()
            Hatch._clear_hatchery_with_dragon_placement()

# Hatch.sell_egg()
    