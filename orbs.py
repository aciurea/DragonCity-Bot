from close import check_if_ok
from move import moveAndClick, multiple_click
from utils import delay, exists, get_monitor_quarters, getImagePositionRegion
from position_map import Position_Map
import constants as C


class Orbs:
    habitat_pos = [724, 629]
    
    def collect_orbs():
        Position_Map.center_map()
        multiple_click(Orbs.habitat_pos, times=10)
        delay(1)
        claim_btn = getImagePositionRegion(C.ORBS_CLAIM, *get_monitor_quarters()['2ndHorHalf'], .8, 2)

        if not exists(claim_btn): return print('Orbs not ready')
        moveAndClick(claim_btn)
        check_if_ok()