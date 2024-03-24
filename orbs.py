from close import check_if_ok
from move import moveAndClick, multiple_click
from utils import delay, dragMapToCenter, exists, get_monitor_quarters, getImagePositionRegion
import constants as C


class Orbs:
    habitat_pos = [724, 629]
    
    def collect_orbs():
        dragMapToCenter()
        multiple_click(Orbs.habitat_pos, times=10)
        delay(.5)
        claim_btn = getImagePositionRegion(C.ORBS_CLAIM, *get_monitor_quarters()['2ndHorHalf'], .8, 2)

        if not exists(claim_btn): return print('Orbs not ready')
        moveAndClick(claim_btn)
        check_if_ok()