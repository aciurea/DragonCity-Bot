

from utils import checkIfCanClaim, closePopup, closeVideo, commonClaim, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick

def collectTreasure():
    treasure = getImagePositionRegion('./img/rewards/daily_chest.png', 600, 500, 1600, 900)
    if exists(treasure):
        moveAndClick(treasure)
        delay(1)
    collect = getImagePositionRegion('./img/rewards/collect.png', 0, 500, 500, 900)

    if not exists(collect): return closePopup()
    moveAndClick(collect)
    openChest()
    closePopup()

def openChest():
    tap = getImagePositionRegion('./img/tv/tap.png', 300, 300, 1600, 800)
    moveAndClick(tap, 'No tap button found')
    delay(3)
    claim = getImagePositionRegion('./img/tv/yellow_claim.png', 200, 300, 1600, 800)
    moveAndClick(claim, 'No claim button after opening chest found')
    delay(.5)
    if not exists(claim):
        closePopup()

def claim():
    print('Go to claim')
    claimBtn = getImagePositionRegion('./img/tv/claim.png', 200, 400, 1400, 800)

    print('claimBtn ', claimBtn)
    moveAndClick(claimBtn)
    openChest()
    closePopup()


def openTv(tv):
    moveAndClick(tv)
    delay(1)
    path = './img/tv/get_rewards_btn.png'
    rewardsBtn = [-1]

    rewardsBtn = getImagePositionRegion(path, 100, 500, 1200, 900)
    if exists(rewardsBtn):
        print('Watching videos')
        moveAndClick(rewardsBtn)
        checkIfCanClaim()
        closeVideo()
        claim()
        closePopup()
    
    else:
        print('No videos available')
        return closePopup()
  

def collectRewards():
    tv = getImagePositionRegion('./img/tv/tv.png', 300, 200, 1200, 800)

    if exists(tv):
        openTv(tv)
    else:
        print('No TV available')
    collectTreasure()
