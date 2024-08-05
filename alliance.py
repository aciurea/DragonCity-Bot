from datetime import datetime
import time
from screeninfo import get_monitors
from breed import Breed
from close import check_if_ok
from move import moveAndClick, multiple_click
from popup import Popup
from utils import delay, exists, get_monitor_quarters, getImagePositionRegion
from position_map import Position_Map

import constants as C


class Alliance:
    _width = 38.1640625 / 100
    _height = 33.33 / 100
    res = get_monitors()[0]
    alliance_pos = [_width * res.width, _height * res.height]

    def get_work():
        if exists(getImagePositionRegion(C.ALLIANCE_HATCH, *get_monitor_quarters()['2ndHorHalf'], .8, 2)):
            print('alliance hatch work to do')
            return lambda: Breed.breed('hatch', 10)

        if exists(getImagePositionRegion(C.ALLIANCE_BREED, *get_monitor_quarters()['2ndHorHalf'], .8, 2)):
            print('alliance breed work to do')
            return lambda: Breed.breed('breed', 10)
        
        return lambda: print('nothing to do on alliance. Is rest time')

    def get_continue_btn():
        return getImagePositionRegion(C.ALLIANCE_CONTINUE, *get_monitor_quarters()['2ndHorHalf'], .8, 2)
    
    def get_claim_btn():
        return getImagePositionRegion(C.ALLIANCE_CLAIM, *get_monitor_quarters()['4thRow'], .8, 2)
    
    def open_alliance():
        if not exists(Position_Map.center_map()):
            check_if_ok()
        Position_Map.drag_map_to_the_bottom()
        multiple_click(Alliance.alliance_pos, 3)
        delay(10)
        cont = Alliance.get_continue_btn()
        if exists(cont):
            moveAndClick(cont)
            delay(1)
            check_if_ok()
            return
        delay(.5)
        claim_btn = Alliance.get_claim_btn()
        if exists(claim_btn):
            moveAndClick(Alliance.get_claim_btn())
            delay(1)
            Popup.check_popup_chest()
            delay(10)
        work = Alliance.get_work()
        check_if_ok() 
        work()
