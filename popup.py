import time
from screeninfo import get_monitors
from move import moveAndClick, multiple_click
from utils import exists, get_monitor_quarters, getImagePositionRegion, get_int
import constants as C
import concurrent.futures
from timers import delay

res = get_monitors()[0]
_percent = { "claim_btn": [.490625, .79652], "tap_btn": [.494140625, .694] }

_jsonPos =  { 
    "TAP_BTN": [get_int(res.width * _percent["tap_btn"][0]), get_int(res.height * _percent["tap_btn"][1])],
    "CLAIM_BTN": [get_int(res.width * _percent["claim_btn"][0]), get_int(res.height * _percent["claim_btn"][1])],
}

class Popup:
    mon_quarters = get_monitor_quarters()

    @staticmethod
    def _get_chest():
        sections = [
            [C.POPUP_LEFT_HEADER, *Popup.mon_quarters['1stHorHalf']],
            [C.POPUP_TAP, *Popup.mon_quarters['2ndHorHalf']],
        ]
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 2), sections)
            for btn in result_list:
                if exists(btn): return btn
            return [-1]
        
    @staticmethod
    def _claim_chest():
        claim_btn = getImagePositionRegion(C.POPUP_CLAIM, *Popup.mon_quarters['2ndHorHalf'], .8, 5, 1)

        if exists(claim_btn):
            multiple_click(claim_btn, 3)
            print('Chest opened!')
        else: moveAndClick(_jsonPos['CLAIM_BTN'])
        delay(5) # Opening popup is kind of slow, just wait 5 seconds to be safe.
        
    @staticmethod
    def _open_chest():
        tab_btn = getImagePositionRegion(C.POPUP_TAP, *Popup.mon_quarters['3rdRow'], .8, 1)
        if exists(tab_btn): 
          multiple_click(tab_btn, times=10)
        else:
            print("Tap not found")
            multiple_click(_jsonPos['TAP_BTN'], times=10)
        Popup._claim_chest()

    @staticmethod
    def check_popup_chest():
        if exists(Popup._get_chest()):
          print("Chest found, try to open it.")
          Popup._open_chest()