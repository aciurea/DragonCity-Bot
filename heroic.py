import random
from screeninfo import get_monitors
from arena import Arena
from battle import Battle
from breed import Breed
from close import check_if_ok
from collectFood import heroic_collect
from move import center_map
from popup import Popup
from utils import delay, exists, get_int, get_monitor_quarters, getImagePositionRegion, moveAndClick
import constants as C

class Heroic:
    [res] = get_monitors()
    heroic_arena = [get_int(0.56730769 * res.width), get_int(0.32 * res.height)]
    mon = get_monitor_quarters()

    @staticmethod
    def is_heroic_race():
        mon = get_monitor_quarters()
        center_map()
        moveAndClick(Heroic.heroic_arena)
        delay(.5)

        return exists(getImagePositionRegion(C.HEROIC_ARENA, *mon['1stCol'], .8, 1))
    
    def _start_fight():
        delay(1)

        in_progress = getImagePositionRegion(C.HEROIC_IN_PROGRESS, *Heroic.mon['full'], .8, 1)

        if exists(in_progress): return print('Heroic fight no ready yet.')

        fight_btn = getImagePositionRegion(C.HEROIC_START_FIGHT_BTN, 0, 0, Heroic.res.width, Heroic.res.height, .9, 1)

        if exists(fight_btn):
            moveAndClick(fight_btn)
            delay(.5)
            select_new_dragon_btn = getImagePositionRegion(C.ARENA_SELECT_DRAGON, *Arena.mon_quarters['full'], .8, 1)
            moveAndClick(select_new_dragon_btn)
            delay(1)
            new_dragon = getImagePositionRegion(C.ARENA_NEW_DRAGON, *Arena.mon_quarters['2ndRow'], .8, 1)
            if not exists(new_dragon): raise Exception('No dragons available')
            moveAndClick(new_dragon)
            delay(1)
            moveAndClick([get_int(0.4892307 * Heroic.res.width), get_int(0.909375 * Heroic.res.height)])
            delay(5)
            Battle.fight()
        check_if_ok()

    def fight_in_heroic_arena():
        fight_btn = getImagePositionRegion(C.HEROIC_FIGHT, *Heroic.mon['full'], 0.8, 1)
        if exists(fight_btn):
            moveAndClick(fight_btn)
            delay(.5)
            Heroic._start_fight()
        check_if_ok()
        return exists(fight_btn)
    
    def claim_node():
        claim = getImagePositionRegion(C.HEROIC_CLAIM, *Heroic.mon['4thRow'], 0.8, 1)

        if exists(claim):
            moveAndClick(claim)
            delay(1)
            Popup.check_popup_chest()
            delay(1)

    def race():
        if Heroic.is_heroic_race():
           Heroic.claim_node()
           
           if not Heroic.fight_in_heroic_arena():
                for work in [heroic_collect, Breed.breed]:
                    work()
        else: print('Not in heroic race')
