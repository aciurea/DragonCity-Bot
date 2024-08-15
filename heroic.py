from screeninfo import get_monitors
from arena import Arena
from battle import Battle
from breed import Breed
from close import Close, check_if_ok
from collectFood import heroic_collect
from league import League
from move import center_map
from popup import Popup
from utils import delay, exists, get_int, get_monitor_quarters, getImagePositionRegion, get_grid_monitor
import constants as C
from move import moveAndClick, multiple_click

class Heroic:
    res = get_monitors()[0]
    skip_button = [1210, 1355]
    
    skip_pos = [1225, 1355]
    heroic_top_pos = [1150, 295]
    heroic_arena = [get_int(0.56730769 * res.width), get_int(0.32 * res.height)]
    mon = get_monitor_quarters()
    missions = [C.HEROIC_FOOD, C.HEROIC_BREED, C.HEROIC_HATCH, C.HEROIC_FEED, C.HEROIC_LEAGUE]
    actions = [heroic_collect, lambda: Breed.breed('breed'), lambda: Breed.breed('hatch'), lambda: Breed.breed('feed'), League.enter_league]

    @staticmethod
    def is_heroic_race():
        mon = get_monitor_quarters()
        if not exists(center_map()):
            check_if_ok()
        multiple_click(Heroic.heroic_top_pos, 3, 0.01)
        delay(.5)

        return exists(getImagePositionRegion(C.HEROIC_ARENA, *mon['1stCol'], .8, 1))
    
    def _start_fight():
        delay(1)

        in_progress = getImagePositionRegion(C.HEROIC_IN_PROGRESS, *Heroic.mon['full'], .8, 1)

        if exists(in_progress): return print('Heroic fight no ready yet.')

        fight_btn = getImagePositionRegion(C.HEROIC_START_FIGHT_BTN, 0, 0, Heroic.res.width, Heroic.res.height, .9, 1)

        if exists(fight_btn):
            moveAndClick(fight_btn)
            delay(1.5)
            select_new_dragon_btn = getImagePositionRegion(C.HEROIC_SELECT_BTN, *Arena.mon_quarters['full'], .8, 1)
            moveAndClick(select_new_dragon_btn)
            delay(1)
            new_dragon = getImagePositionRegion(C.ARENA_NEW_DRAGON, *Arena.mon_quarters['2ndRow'], .8, 1)
            if not exists(new_dragon): raise Exception('No dragons available')
            moveAndClick(new_dragon)
            delay(1)
            moveAndClick([get_int(0.4892307 * Heroic.res.width), get_int(0.909375 * Heroic.res.height)])
            delay(5)
            Battle.fight(change_dragon=False)
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

    def free_spin():
        free_spin_pos = [2352, 1295] 
        moveAndClick(free_spin_pos)
        delay(1)
        grid = get_grid_monitor()
        pos = [
            grid['x5'],
            grid['y4'],
            grid['x7'],
            grid['y6']
        ]
        free_spin_btn = getImagePositionRegion(C.HEROIC_FREE_SPIN, *pos, 0.8, 1)

        if exists(free_spin_btn):
            moveAndClick(free_spin_btn)
            delay(10)
        moveAndClick(free_spin_pos)
        delay(1)
        
    def race(times = 0):
        if times > 1: return

        if not Heroic.is_heroic_race():
            print('Not in heroic race')
            return
        
        if times == 1: # collected once the items. Do free spin
            Heroic.free_spin() 
        
        popup_btn = Close.get_popup_red_btn()
        if exists(popup_btn):
            moveAndClick(popup_btn)
            delay(1)
            
        Heroic.claim_node()
        Heroic.fight_in_heroic_arena()
        delay(.5)

        
        work_to_do = []
        for index, mission in enumerate(Heroic.missions):
            pos = getImagePositionRegion(mission, *Heroic.mon['2ndVerHalf'], 0.8, 1)
            if exists(pos): 
                print('Mission is ', mission)
                work_to_do.append(Heroic.actions[index])
        check_if_ok()
        for work in work_to_do: work()
        
        Heroic.race(times + 1)
        
        
           
