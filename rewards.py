
import time
from utils import (ThreadWithValue,
                   checkIfCanClaim,
                   closePopup,
                   closeVideo,
                   delay,
                   exists,
                   getImagePosition,
                   getImagePositionRegion,
                   moveAndClick,
                   video_error,
                   openChest)

import constants as C 

def collectTreasure():
    print('Looking to collect the treasure')
    treasure = getImagePositionRegion(C.TV_DAILY_CHEST, 1300, 700, 1500, 850, .8, 3)
    if exists(treasure):
        moveAndClick(treasure)
        delay(1)
    collect = getImagePositionRegion(C.TV_COLLECT, 0, 700, 300, 800, 0.8, 3)

    if exists(collect):
        moveAndClick(collect)
        openChest()
   
    closePopup()

def _get_claim_btn():
    list = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.TV_CLAIM_AND_NEXT, 640, 550, 1000, 670, 0.8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.TV_CLAIM,390, 550, 600, 670, 0.8, 3)).start()
    ]

    for btn in list:
        btn = btn.join()
        if exists(btn):
            return btn
    return [-1]


def _is_dtv():
    dtv = getImagePositionRegion(C.TV_DTV, 600, 0, 1400, 400, 0.8, 3)
    return exists(dtv)

def _claim():
    claim_btn = _get_claim_btn()
    print('Go to claim', claim_btn)

    if exists(claim_btn):
        moveAndClick(claim_btn)
        delay(.5)
        openChest()
        if _is_dtv(): closePopup()
        return claim_btn
    return [-1]

def _get_watch_video_btn():
    btns = [
        ThreadWithValue(target=getImagePositionRegion,args=(C.TV_GET_REWARDS_BTN, 200, 700, 500, 830, 0.8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion,args=(C.TV_PRIZES, 630, 700, 900, 820, 0.8, 3)).start()
    ]

    for btn in btns:
        btn = btn.join()
        if exists(btn): return btn
            
    return [-1]

def _check_last_claim_from_video():
    delay(1)
    claim_btn = getImagePositionRegion(C.TV_GREEN_CLAIM, 660, 550, 920, 700, 0.8, 10)
    if exists(claim_btn):
        moveAndClick(claim_btn)
        delay(1)
        openChest()

def _watch_videos():
    print('Watching videos...')
    st = time.time()
    while not exists(video_error() or time.time() - st < 60):
        moveAndClick( [802, 352]) # play videos btn
        checkIfCanClaim()
        closeVideo()
        if exists(_claim()): continue
        else: return _check_last_claim_from_video()
            
def openTv():
    delay(1)
    btn = _get_watch_video_btn()

    if not exists(btn):
        closePopup()
        return print('Nothing to watch for getting rewards...')

    moveAndClick(btn)
    _watch_videos()
    delay(1)
    closePopup()


def collectRewards():
    tv = getImagePosition(C.TV_TV)

    if exists(tv):
        moveAndClick([tv[0] + 20, tv[1]])
        openTv()
        closePopup()
    else:
        print('No TV available')
    collectTreasure()
