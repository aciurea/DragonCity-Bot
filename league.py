import time
from battle import Battle
from close import Close, check_if_ok
from utils import delay, dragMapToCenter, exists, get_monitor_quarters, getImagePositionRegion, moveAndClick
import constants as C

class League:
    battle_pos = [790, 1250]
    league_pos = [735, 625]
    claim_pos = [910, 1140]
    mon_quarters = get_monitor_quarters()

    def enter_league():
        dragMapToCenter()
        delay(.2)
        moveAndClick(dragMapToCenter())
        delay(.5)
        moveAndClick(League.battle_pos)
        delay(.5)
        moveAndClick(League.league_pos)
        delay(2)
        League.open_battle()
        check_if_ok()

    def open_battle():
        if exists(getImagePositionRegion(C.LEAGUE_NOT_READY, *League.mon_quarters['top_right'], .8, 2)): 
            return print('League not ready.')

        position = League.mon_quarters['2ndHorHalf']
        position[1] -= 150
        oponent = getImagePositionRegion(C.LEAGUE_OPONENT, *position, .8, 1)
        start = time.time()
        
        while time.time() - start < 360:
            if exists(getImagePositionRegion(C.LEAGUE_NOT_READY, *League.mon_quarters['top_right'], .8, 2)): 
                return print('League not ready.')
            if exists(oponent):
                moveAndClick(oponent)
                delay(1)
                red_btn = Close.get_popup_red_btn()
                if exists(red_btn): return moveAndClick(red_btn)

                Battle.fight(change_dragon=False)
                moveAndClick(League.claim_pos)
                delay(.5)
                moveAndClick(getImagePositionRegion(C.LEAGUE_CLAIM, *League.mon_quarters['full'], .8, 2))
                delay(.5)
                oponent = getImagePositionRegion(C.LEAGUE_OPONENT, *position, .8, 1)
            else: return print('No oponent found.')
