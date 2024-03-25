from close import check_if_ok
from move import center_map, drag_map_to_the_bottom, moveAndClick, multiple_click
from popup import Popup
from utils import delay, exists, get_monitor_quarters, getImagePositionRegion
import constants as C


class Alliance:
    alliance_pos = [977, 480]

    def get_continue_btn():
        return getImagePositionRegion(C.ALLIANCE_CONTINUE, *get_monitor_quarters()['2ndHorHalf'], .8, 2)
    
    def get_claim_btn():
        return getImagePositionRegion(C.ALLIANCE_CLAIM, *get_monitor_quarters()['4thRow'], .8, 2)
    
    def open_alliance():
        center_map()
        drag_map_to_the_bottom()
        multiple_click(Alliance.alliance_pos, 3)
        delay(5)
        moveAndClick(Alliance.get_continue_btn())
        delay(.5)
        claim_btn = Alliance.get_claim_btn()
        if exists(claim_btn):
            moveAndClick(Alliance.get_claim_btn())
            Popup.check_popup_chest()
            delay(5)
        # wait for the button claim to appear
        check_if_ok()
