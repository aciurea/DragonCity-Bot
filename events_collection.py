from utils import getImagePositionRegion, get_monitor_quarters, exists, delay
from move import moveAndClick
from popup import Popup
from close import check_if_ok
from pyautogui import scroll

import time
import constants as C


class Events_Collection:
    _mon = get_monitor_quarters()

    @staticmethod
    def collect_events():
        events_btn = Events_Collection._get_events_btn()

        if not exists(events_btn): return print('Events button not found')

        moveAndClick(events_btn)
        delay(1)

        scroll_times = 5
        curr_time = time.time()

        while scroll_times >= 0 and time.time() - curr_time < 60:
            scroll_times -= 1

            claim_btn = Events_Collection._get_claim_btn()

            if exists(claim_btn):
                moveAndClick(claim_btn)
                delay(1)
                Events_Collection._collect_event()
            scroll(-1_000)
        check_if_ok()

    def _collect_event():
        curr_time = time.time()
        claim_btn2 = Events_Collection._get_inner_claim_btn()

        while exists(claim_btn2) and time.time() - curr_time < 30:
            moveAndClick(claim_btn2)
            delay(1)
            Popup.check_popup_chest()
            enjoy_btn = Events_Collection._get_enjoy_btn()

            if exists(enjoy_btn):
                moveAndClick(enjoy_btn)
                delay(1)
                Popup.check_popup_chest()
            claim_btn2 = Events_Collection._get_inner_claim_btn()

    def _get_enjoy_btn():
        return getImagePositionRegion(C.EVENTS_ENJOY_BTN, *Events_Collection._mon['4thRow'], .8, 1)
           
    @staticmethod
    def _get_inner_claim_btn():
        return getImagePositionRegion(C.EVENTS_CLAIM_BTN_2, *Events_Collection._mon['4thRow'], 0.8, 1)
    
    @staticmethod
    def _get_claim_btn():
        return getImagePositionRegion(C.EVENTS_CLAIM_BTN, *Events_Collection._mon['4thRow'], 0.8, 1)

    @staticmethod
    def _get_events_btn():
        return getImagePositionRegion(C.EVENTS_COLLECTION_BTN, *Events_Collection._mon['lastCol'], 0.8, 1)