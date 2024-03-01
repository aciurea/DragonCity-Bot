from screeninfo import get_monitors
from move import center_map, moveAndClick
import constants as C
from timers import delay

from utils import exists, get_int, get_monitor_quarters, getImagePositionRegion

class Hatch:
    [res] = get_monitors()
    mon_quarters = get_monitor_quarters()
    hatchery_pos = [get_int(0.346153 * res.width), get_int(0.639375 * res.height)]
    terra_habitat = [get_int(0.625 * res.width), get_int(0.704375 * res.height)]
    # dragon_pos_in_habitat = [get_int(0.544230769 * res.width), get_int(0.849375 * res.height)]
    sell_egg_btn_from_habitat = [get_int(0.82461538 * res.width), get_int(0.89125 * res.height)]
    confirm_sell_btn = [get_int(0.55730769 * res.width), get_int(0.676875*res.height)]
    place_btn_pos = [get_int(0.52961538 * res.width), get_int(0.6875 * res.height)]

    def _get_terra_egg():
        mon_quarters = get_monitor_quarters()

        return getImagePositionRegion(C.BREED_TERRA_EGG, *mon_quarters['4thRow'], .8, 1)


    def sell_egg():
        moveAndClick(Hatch.hatchery_pos)
        egg = Hatch._get_terra_egg()
        if exists(egg):
            moveAndClick(egg)
            #sell
            delay(.5)
            moveAndClick([get_int(0.681153846 * Hatch.res.width),  get_int(0.6825 * Hatch.res.height)])
            delay(.5)
            # confirm sell
            moveAndClick([get_int(0.5526923 * Hatch.res.width), get_int(0.685625 * Hatch.res.height)])
            return Hatch.sell_egg()

    def _sell_dragon():
        delay(.3)
        dragon_pos_in_habitat = getImagePositionRegion(C.HATCH_DRAGON, *Hatch.mon_quarters['4thRow'], .8, 1)
        print(dragon_pos_in_habitat)
        if exists(dragon_pos_in_habitat):
            moveAndClick(dragon_pos_in_habitat)
            delay(.5)
            moveAndClick(Hatch.sell_egg_btn_from_habitat)
            delay(.5)
            moveAndClick(Hatch.confirm_sell_btn)
            return Hatch._sell_dragon()
      
    # def _clear_hatchery_with_dragon_placement():
    #     hatchery_pos_from_habitat = [get_int(0.6596153* Hatch.res.width), get_int(0.636875 * Hatch.res.height)]
    #     check_if_ok()
    #     moveAndClick(hatchery_pos_from_habitat)
    #     egg = Hatch._get_terra_egg()
    #     habitat_pos_after_sell = [get_int(0.63153846 * Hatch.res.width), get_int(0.714375 * Hatch.res.height)]
    #     if exists(egg):
    #         moveAndClick(egg)
    #         delay(.3)
    #         moveAndClick(Hatch.place_btn_pos)
    #         delay(1)
    #         moveAndClick(habitat_pos_after_sell)
    #         return Hatch._clear_hatchery_with_dragon_placement()

    #     moveAndClick(habitat_pos_after_sell)
    #     delay(.3)
    #     Hatch._sell_dragon()
        
    def place_egg():
        center_map()
        moveAndClick(Hatch.hatchery_pos)
        egg = Hatch._get_terra_egg()
        if exists(egg):
            moveAndClick(egg)
            delay(.5)
            moveAndClick(Hatch.place_btn_pos)
            delay(2)
            moveAndClick(Hatch.terra_habitat)
            delay(1)
            Hatch._sell_dragon()
            return Hatch.place_egg()

# Hatch.place_egg()
    