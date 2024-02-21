from screeninfo import get_monitors
from move import moveAndClick
from utils import exists, get_json_file, get_monitor_quarters, getImagePositionRegion
import constants as C
import concurrent.futures
from timers import delay

jsonPos = get_json_file('popup.json')

class Popup:
    [res] = get_monitors()
    mon_quarters = get_monitor_quarters()
    
    @staticmethod
    def get_chest():
        sections = [
            [C.POPUP_LEFT_CORNER, *Popup.mon_quarters['bottom_left']],
            [C.POPUP_HEADER, *Popup.mon_quarters['top_left']],
            [C.POPUP_TAP, *Popup.mon_quarters['3rdRow']],
        ]
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), sections)
            for btn in result_list:
                if exists(btn): return btn
            return [-1]
        
    @staticmethod
    def open_chest():
        tab_btn = getImagePositionRegion(C.POPUP_TAP, *Popup.mon_quarters['3rdRow'], .8, 1)
        if exists(tab_btn): moveAndClick(tab_btn)
        else: moveAndClick(jsonPos['TAP_BTN'])
        delay(3)
        claim_btn = getImagePositionRegion(C.POPUP_CLAIM, *Popup.mon_quarters['full'], .8, 1)
        
        if exists(claim_btn):
            moveAndClick(claim_btn)
            print('Chest opened!')
        else: moveAndClick(jsonPos['CLAIM_BTN'])

    @staticmethod
    def check_popup_chest():
        if exists(Popup.get_chest()):
          Popup.open_chest()
