
from utils import (ThreadWithReturnValue,
                   checkIfCanClaim,
                   closePopup,
                   closeVideo,
                   delay,
                   exists,
                   get_path as get_path_from_utils,
                   getImagePosition,
                   getImagePositionRegion,
                   moveAndClick,
                   video_error,
                   openChest)

BASE_REWARDS = './img/rewards/'
def get_path(path):
    return get_path_from_utils(BASE_REWARDS+path)

def collectTreasure():
    print('Looking to collec the treasure')
    treasure = getImagePositionRegion(get_path('daily_chest'), 1300, 700, 1500, 850, .8, 3)
    if exists(treasure):
        moveAndClick(treasure)
        delay(1)
    collect = getImagePositionRegion(get_path('collect'), 0, 700, 300, 800, 0.8, 3)

    if exists(collect):
        moveAndClick(collect)
        openChest()
   
    closePopup()

def claim():
    print('Go to claim')
    claim_btn = getImagePositionRegion('./img/tv/claim.png', 200, 400, 1400, 800)

    if exists(claim_btn):
        moveAndClick(claim_btn)
        openChest()

def openTv():
    delay(1)
    rewards_thread,prizes_thread = [
        ThreadWithReturnValue(target=getImagePositionRegion, 
        args=('./img/tv/get_rewards_btn.png', 200, 700, 500, 850, 0.8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion,
                                    args=('./img/tv/prizes.png', 600, 700, 900, 850, 0.8, 3)).start()
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
        moveAndClick([802, 352]) # position to play the video
        checkIfCanClaim()
        closeVideo()
        claim()
    delay(1)
    closePopup()


def collectRewards():
    tv = getImagePosition('./img/tv/tv.png')

    if exists(tv):
        moveAndClick([tv[0] + 20, tv[1]])
        openTv()
    else:
        print('No TV available')
    collectTreasure()
