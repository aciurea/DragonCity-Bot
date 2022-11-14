
from utils import (ThreadWithReturnValue,
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

def claim():
    print('Go to claim')
    claim_btn = getImagePositionRegion(C.TV_CLAIM, 200, 400, 1400, 800)

    if exists(claim_btn):
        moveAndClick(claim_btn)
        openChest()

def openTv():
    delay(1)
    rewards_thread,prizes_thread = [
        ThreadWithReturnValue(target=getImagePositionRegion, 
        args=(C.TV_GET_REWARDS_BTN, 200, 700, 500, 850, 0.8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion,
                                    args=(C.TV_PRIZES, 600, 700, 900, 850, 0.8, 3)).start()
    ]
    rewardsBtn = rewards_thread.join()
    prizesBtn = prizes_thread.join()
    
    if not exists(rewardsBtn) and not exists(prizesBtn):
        closePopup()
        return print('Nothing to watch for getting rewards...')

    btn = rewardsBtn if exists(rewardsBtn) else prizesBtn
    moveAndClick(btn)
    print('Watching videos...')
    if not exists(video_error()):
        play_video_pos = [802, 352]
        moveAndClick(play_video_pos)
        checkIfCanClaim()
        closeVideo()
        claim()
    delay(1)
    closePopup()


def collectRewards():
    tv = getImagePosition(C.TV_TV)

    if exists(tv):
        moveAndClick([tv[0] + 20, tv[1]])
        openTv()
    else:
        print('No TV available')
    collectTreasure()
