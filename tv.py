
import time
from close import check_if_ok
from utils import (
                delay,
                dragMapToCenter,
                exists,
                get_json_file,
                get_monitor_quarters,
                getImagePositionRegion,
                moveAndClick
            )

import constants as C 
from popup import Popup

class TV:
    jsonPos = get_json_file('tv.json')
    mon_quarters = get_monitor_quarters()

    def get_watched_video_close_btn():
        return getImagePositionRegion(C.TV_CLOSE_WATCHED_VIDEO, *TV.mon_quarters['1stRow'], .8, 1)
    
    def is_ready_to_close():
        can_close = getImagePositionRegion(C.TV_READY_TO_CLOSE_WATCHED_VIDEO, *TV.mon_quarters['1stRow'], .8, 1)
        return exists(can_close) or exists(TV.get_watched_video_close_btn())
    
    def failed_video():
        return exists(getImagePositionRegion(C.TV_FAILED_VIDEO, *TV.mon_quarters['1stHorHalf'], .8, 1))

    @staticmethod
    def watch_add():
        start = time.time()
        while time.time() - start < 60:
            if TV.failed_video(): return False
            if TV.is_ready_to_close():
                close_btn = TV.get_watched_video_close_btn()
                moveAndClick([close_btn[0] + 5, close_btn[1] + 10])
                return True
            delay(1)
        raise Exception("Watched video didn't close in time")

    def collect_reward():
        claim_btn = getImagePositionRegion(C.TV_CLAIM, *TV.mon_quarters['3rdRow'], .8, 1)
        last_claim = getImagePositionRegion(C.TV_LAST_CLAIM, *TV.mon_quarters['3rdRow'], .8, 1)

        if exists(claim_btn):
            moveAndClick(claim_btn)
        elif exists(getImagePositionRegion(C.TV_DTV, *TV.mon_quarters['1stRow'], .8, 1)):
            check_if_ok()
        elif exists(last_claim):
            moveAndClick(last_claim)
        
        Popup.check_popup_chest()
    
    def get_rewards_btn():
        rewards_btn = getImagePositionRegion(C.TV_GET_REWARDS_BTN, *TV.mon_quarters["4thRow"], .8, 1)
        if exists(rewards_btn): return rewards_btn
        
        return  getImagePositionRegion(C.TV_PRAIZES, *TV.mon_quarters["4thRow"], .8, 1)
    
    def open_tv():
        dragMapToCenter()
        moveAndClick(TV.jsonPos['TV'])
        delay(1)
    
        rewards_btn = TV.get_rewards_btn()
        while exists(rewards_btn):
            moveAndClick(rewards_btn)
            delay(1)
            rewards_btn = getImagePositionRegion(C.TV_GET_REWARDS_BTN, *TV.mon_quarters["4thRow"], .8, 1)
            if not TV.watch_add(): return print("Failed video")
            delay(2)
            TV.collect_reward()
            delay(1)

            rewards_btn = TV.get_rewards_btn()
            delay(3)
        check_if_ok()
