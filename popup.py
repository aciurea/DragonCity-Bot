import time
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
            # [C.POPUP_LEFT_CORNER, *Popup.mon_quarters['bottom_left']],
            [C.POPUP_HEADER, *Popup.mon_quarters['top_left']],
            [C.POPUP_TAP, *Popup.mon_quarters['3rdRow']],
        ]
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), sections)
            for btn in result_list:
                if exists(btn): return btn
            return [-1]
        
    @staticmethod
    def multiple_click(tab_btn):
        times = 5
        while times > 0:
            moveAndClick(tab_btn)
            delay(.1)
            times -= 1

    @staticmethod
    def claim_chest():
        start = time.time()

        claim_btn = getImagePositionRegion(C.POPUP_CLAIM, *Popup.mon_quarters['full'], .8, 1)
        while(time.time() - start < 10 and not exists(claim_btn)):
            delay(1)
            claim_btn = getImagePositionRegion(C.POPUP_CLAIM, *Popup.mon_quarters['full'], .8, 1)
        if exists(claim_btn):
            moveAndClick(claim_btn)
            print('Chest opened!')
        else: moveAndClick(jsonPos['CLAIM_BTN'])
        delay(5) # Opening popup is kind of slow, just wait 5 seconds to be safe.
        
    @staticmethod
    def open_chest():
        tab_btn = getImagePositionRegion(C.POPUP_TAP, *Popup.mon_quarters['3rdRow'], .8, 1)
        if exists(tab_btn): 
          Popup.multiple_click(tab_btn)
        else:
            print("Tap not found")
            Popup.multiple_click(jsonPos['TAP_BTN'])
        Popup.claim_chest()

    @staticmethod
    def check_popup_chest():
        if exists(Popup.get_chest()):
          print("Chest found, try to open it.")
          Popup.open_chest()