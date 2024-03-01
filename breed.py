from screeninfo import get_monitors
from close import check_if_ok
from hatch import Hatch
from move import center_map
from utils import ( delay, exists,
                    get_int, get_monitor_quarters,
                    getImagePositionRegion,
                    moveAndClick)
import constants as C


class Breed:
    [res] = get_monitors()
    artifact_center_pos = [res.width / 2, res.height / 2]
    rock_pos = [get_int(0.405769 * res.width), get_int(0.7375 * res.height)]
    tree_pos = [get_int(0.29 * res.width), get_int(0.691 * res.height)]
    habitat_pos = [get_int(0.31769 * res.width), get_int(0.720625 * res.height)]
    hatchery_pos = [get_int(0.346153 * res.width), get_int(0.639375 * res.height)]
    mon_quarters = get_monitor_quarters()
    _close_btn_pos = None
    _re_breed_btn = None
    _hatchery_full_close_btn = [get_int(0.783461538 * res.width), get_int(0.261875 * res.height)]
    
    def _get_re_breed():
       if(Breed._re_breed_btn == None):
           Breed._re_breed_btn = getImagePositionRegion(C.RE_BREED_BTN, *Breed.mon_quarters['4thRow'], .8, 1)
       return Breed._re_breed_btn
    
    def _re_breed():
        delay(.5)
        btn = Breed._get_re_breed()

        if not exists(btn): return print('Rebreed button not found')

        moveAndClick(btn)
     
        delay(1)
        moveAndClick([1276, 1079])
        delay(.1)
        moveAndClick([2418, 120])

        # if Breed._close_btn_pos == None:
        #     Breed._close_btn_pos = check_if_ok()
        # else: moveAndClick(Breed._close_btn_pos)
    
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

    def start_fresh():
        Breed.clear_hatchery()

        for breed_place in [Breed.rock_pos, Breed.tree_pos]:
            center_map()
            moveAndClick(breed_place)
            delay(1)
        check_if_ok()
        # in case the tree and rock had eggs, wait 15 secs to hatch and clear them.
        delay(10)
        Breed.clear_hatchery()
     
    @staticmethod
    def breed(work_type="breed"):
        Breed.start_fresh()
        time_to_hatch_egg = 6
        first_time = True

        times = 30
        while times > 0:
            times -= 1
            
            for breed_place in [Breed.rock_pos, Breed.tree_pos]:
                center_map()
                moveAndClick(breed_place)
                Breed._re_breed()
                delay(.5)

            delay(time_to_hatch_egg)

            if work_type == "breed": Breed.clear_hatchery()
            else: Hatch.place_egg()
            # collect phase
            for breed_place in [Breed.rock_pos, Breed.tree_pos]:
                center_map()
                moveAndClick(breed_place)
                delay(1)
            check_if_ok()
            print('Breed cycle done')
            if first_time:
                first_time = False
                time_to_hatch_egg = 2

# Breed.breed("hatch")