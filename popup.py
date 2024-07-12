import time
from screeninfo import get_monitors
from move import moveAndClick, multiple_click
from utils import exists, get_json_file, get_monitor_quarters, getImagePositionRegion, get_int
import constants as C
import concurrent.futures
from timers import delay

jsonPos = get_json_file('popup.json')

class Popup:
    [res] = get_monitors()
    mon_quarters = get_monitor_quarters()
    _percent = [.490625, .79652]
    _enjoy_claim_static_pos = [get_int(res.width * Popup._percent[0]) , get_int(res.height * Popup._percent[1])]

    @staticmethod
    def _get_chest():
        sections = [
            [C.POPUP_TAP, *Popup.mon_quarters['3rdRow']],
        ]
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), sections)
            for btn in result_list:
                if exists(btn): return btn
            return [-1]
        
    @staticmethod
    def _claim_chest():
        claim_btn = getImagePositionRegion(C.POPUP_CLAIM, *Popup.mon_quarters['2ndHorHalf'], .8, 5, 1)

        if exists(claim_btn):
            multiple_click(claim_btn, 3)
            print('Chest opened!')
        else: moveAndClick(Popup._enjoy_claim_static_pos)
        delay(5) # Opening popup is kind of slow, just wait 5 seconds to be safe.
        
    @staticmethod
    def _open_chest():
        tab_btn = getImagePositionRegion(C.POPUP_TAP, *Popup.mon_quarters['3rdRow'], .8, 1)
        if exists(tab_btn): 
          multiple_click(tab_btn, times=10)
        else:
            print("Tap not found")
            multiple_click(jsonPos['TAP_BTN'], times=10)
        Popup._claim_chest()

    @staticmethod
    def check_popup_chest():
        if exists(Popup._get_chest()):
          print("Chest found, try to open it.")
          Popup._open_chest()