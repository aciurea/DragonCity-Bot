from screeninfo import get_monitors
from close import check_if_ok
from hatch import Hatch
from move import center_map, is_artifact_at_pos
from utils import ( delay, exists,
                    get_int, get_monitor_quarters,
                    getImagePositionRegion,
                    moveAndClick)
import constants as C


class Breed:
    [res] = get_monitors()
    artifact_center_pos = [res.width / 2, res.height / 2]
    rock_pos = [get_int(0.405769 * res.width), get_int(0.7375 * res.height)]
    tree_pos = [get_int(0.26769 * res.width), get_int(0.695 * res.height)]
    habitat_pos = [get_int(0.31769 * res.width), get_int(0.720625 * res.height)]
    hatchery_pos = [get_int(0.346153 * res.width), get_int(0.639375 * res.height)]
    mon_quarters = get_monitor_quarters()
    _close_btn_pos = None
    _re_breed_btn = None
    _hatchery_full_close_btn = [get_int(0.783461538 * res.width), get_int(0.261875 * res.height)]
    
    def _get_re_breed():
       if(Breed._re_breed_btn == None):
           Breed._re_breed_btn = getImagePositionRegion(C.RE_BREED_BTN, *Breed.mon_quarters['bottom_right'], .8, 3)
       return Breed._re_breed_btn
    
    def _re_breed():
        delay(.3)
        btn = Breed._get_re_breed()
        moveAndClick(btn)
        y_start = get_int(Breed.res.height / 2)
        x_start = get_int(0.33423 * Breed.res.width)
        x_end = get_int(0.63769 * Breed.res.width)
        y_end = get_int(0.8125 * Breed.res.height)
        breed_btn = getImagePositionRegion(C.BREED_BTN, x_start, y_start, x_end, y_end, 0.8, 3)

        if exists(breed_btn): moveAndClick(breed_btn)

        if Breed._close_btn_pos == None:
            Breed._close_btn_pos = check_if_ok()
        else: moveAndClick(Breed._close_btn_pos)
    
    def did_breed():
        return exists(getImagePositionRegion(C.HATCHERY, *Breed.mon_quarters['bottom_right'], .8, 2))
    
    def clear_hatchery():
        center_map()
        Hatch.sell_egg()

    def do_work(btn):
        moveAndClick(btn)
        if Breed._is_hatchery_full():
            moveAndClick(Breed._hatchery_full_close_btn)
            center_map()
            return Breed.clear_hatchery()
    
        if Breed.did_breed():
            center_map()
            moveAndClick(btn)

        Breed._re_breed()
            
    def _is_hatchery_full():
        x_start = get_int(0.17 * Breed.res.width)
        y_start = get_int(0.3 * Breed.res.height)
        x_end = get_int(0.4 * Breed.res.width)
        y_end = get_int(0.5 * Breed.res.height)
        
        return exists(getImagePositionRegion(C.HATCHERY_FULL, x_start, y_start, x_end, y_end, 0.8, 3))

    @staticmethod
    def breed():
        center_map()
        if is_artifact_at_pos(Breed.artifact_center_pos):
            for breed_place in [Breed.rock_pos, Breed.tree_pos]:
                Breed.do_work(breed_place)
                center_map()
                delay(1)
        check_if_ok()

def breed():
    Breed.breed()

# while 1:
#     breed()
