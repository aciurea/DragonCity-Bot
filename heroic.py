from screeninfo import get_monitors
from close import check_if_ok
from move import center_map
from utils import closePopup, delay, exists, get_int, get_monitor_quarters, getImagePositionRegion, go_back, moveAndClick
import constants as C

def exit_heroic():
    go_back()
    delay(.5)
    closePopup()

class Heroic:
    [res] = get_monitors()
    heroic_arena = [get_int(0.56730769 * res.width), get_int(0.3825 * res.height)]
    mon = get_monitor_quarters()

    @staticmethod
    def is_heroic_race():
        mon = get_monitor_quarters()
        center_map()
        moveAndClick(Heroic.heroic_arena)
        delay(.5)

        return exists(getImagePositionRegion(C.HEROIC_ARENA, *mon['top_right'], .8, 1))
    
    def _start_fight():
        delay(.5)
        fight_btn = getImagePositionRegion(C.HEROIC_START_FIGHT_BTN, 0, 0, Heroic.res.width, Heroic.res.height, .9, 1)
        if exists(fight_btn):
            print('isAvailable', fight_btn)
            moveAndClick(fight_btn)
            delay(.5)
            select_dragon_btn = getImagePositionRegion(C.HEROIC_SELECT_BTN, *Heroic.mon['bottom_left'], .8, 1)
            if not exists(select_dragon_btn): return
            moveAndClick(select_dragon_btn)
            delay(.5)
            moveAndClick([get_int(0.3861538 * Heroic.res.width), get_int(0.39 * Heroic.res.height)])
            delay(.5)
            moveAndClick([get_int(0.4892307 * Heroic.res.width), get_int(0.909375 * Heroic.res.height)])

    def fight_in_heroic_arena():
        x_start = get_int(0.7461538* Heroic.res.width)
        fight_btn = getImagePositionRegion(C.HEROIC_FIGHT, x_start, 0, Heroic.res.width, Heroic.res.height)
        if exists(fight_btn):
            moveAndClick(fight_btn)
            delay(.5)
            Heroic._start_fight()

        check_if_ok()