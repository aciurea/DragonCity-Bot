
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
                   video_error)


def collectTreasure():
    treasure = getImagePositionRegion(
        './img/rewards/daily_chest.png', 600, 500, 1600, 900)
    if exists(treasure):
        moveAndClick(treasure)
        delay(1)
    collect = getImagePositionRegion(
        './img/rewards/collect.png', 0, 500, 500, 900)

    if not exists(collect):
        return closePopup()
    moveAndClick(collect)
    openChest()
    closePopup()


def openChest():
    tap = getImagePositionRegion('./img/tv/tap.png', 300, 300, 1600, 800)
    moveAndClick(tap, 'No tap button found')
    delay(3)
    claim = getImagePositionRegion(
        './img/tv/yellow_claim.png', 200, 300, 1600, 800)
    moveAndClick(claim, 'No claim button after opening chest found')
    delay(.5)
    if not exists(claim):
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
    rewards_thread = ThreadWithReturnValue(target=getImagePositionRegion, args=(
        './img/tv/get_rewards_btn.png',
        100, 500, 1400, 900, 0.8, 20
    ))
    prizes_thread = ThreadWithReturnValue(target=getImagePositionRegion,
                                    args=('./img/tv/prizes.png', 200, 500, 1400, 800, 0.8, 20))
    close_btn_thread = ThreadWithReturnValue(target=get_close_btn)
    prizes_thread.start()
    rewards_thread.start()
    close_btn_thread.start()
    rewardsBtn = rewards_thread.join()
    prizesBtn = prizes_thread.join()

    print('buttons are ', rewardsBtn, prizesBtn)
    btn = rewardsBtn if exists(rewardsBtn) else prizesBtn
    closeBtn = close_btn_thread.join()

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
        moveAndClick(tv)
        openTv()
    else:
        print('No TV available')
    collectTreasure()
