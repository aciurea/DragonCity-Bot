
from utils import (ThreadWithReturnValue,
                   checkIfCanClaim,
                   closePopup,
                   closeVideo,
                   delay,
                   exists,
                   get_close_btn,
                   getImagePosition,
                   getImagePositionRegion,
                   moveAndClick,
                   video_error,
                   openChest)


def collectTreasure():
    treasure = getImagePositionRegion(
        './img/rewards/daily_chest.png', 1300, 700, 1500, 850, .8, 3)
    if exists(treasure):
        moveAndClick(treasure)
        delay(1)
    collect = getImagePositionRegion(
        './img/rewards/collect.png', 0, 700, 300, 800, 0.8, 3)

    if not exists(collect):
        return closePopup()
    moveAndClick(collect)
    openChest()
    closePopup()

def claim():
    print('Go to claim')
    claimBtn = getImagePositionRegion(
        './img/tv/claim.png', 200, 400, 1400, 800)

    print('claimBtn ', claimBtn)
    moveAndClick(claimBtn)
    openChest()
    closePopup()


def openTv():
    delay(1)
    rewards_thread = ThreadWithReturnValue(target=getImagePositionRegion, 
        args=('./img/tv/get_rewards_btn.png', 200, 700, 500, 850, 0.8, 3))
    prizes_thread = ThreadWithReturnValue(target=getImagePositionRegion,
                                    args=('./img/tv/prizes.png', 600, 700, 900, 850, 0.8, 3))
    close_btn_thread = ThreadWithReturnValue(target=get_close_btn)
    prizes_thread.start()
    rewards_thread.start()
    close_btn_thread.start()
    rewardsBtn = rewards_thread.join()
    prizesBtn = prizes_thread.join()
    closeBtn = close_btn_thread.join()
    
    print('buttons are ', rewardsBtn, prizesBtn)
    btn = rewardsBtn if exists(rewardsBtn) else prizesBtn

    if exists(btn):
        print('Watching videos')
        moveAndClick(btn)
        if not exists(video_error()):
            checkIfCanClaim()
            closeVideo()
            claim()
        closePopup(closeBtn)

    else:
        print('No videos available')
        return closePopup(closeBtn)


def collectRewards():
    tv = getImagePosition('./img/tv/tv.png')

    if exists(tv):
        moveAndClick([tv[0] + 20, tv[1]])
        openTv()
    else:
        print('No TV available')
    collectTreasure()
