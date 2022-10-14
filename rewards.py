

from utils import checkIfCanClaim, closePopup, closeVideo, delay, exists, getImagePosition, moveAndClick


def claim():
    claimBtn = getImagePosition('./img/tv/claim.png')

    if exists(claimBtn) == False:
        greenClaim = getImagePosition('./img/tv/green_claim.png')
        moveAndClick(greenClaim)
        tap = getImagePosition('./img/tv/tap.png')
        moveAndClick(tap)
        claim = getImagePosition('./img/fails/claim_yellow.png')
        moveAndClick(claim)
        claim()
        return print('Nothing to claim')

    moveAndClick(claimBtn)


def openTv(tv):
    moveAndClick(tv)
    delay(1)
    paths = ['./img/tv/get_rewards_btn.png']
    rewardsBtn = [-1]

    for path in paths:
        rewardsBtn = getImagePosition(path)
        if exists(rewardsBtn):
            break

    if exists(rewardsBtn) == False:
        print('No videos available')
        return closePopup()
    else:
        moveAndClick(rewardsBtn)
        checkIfCanClaim()
        closeVideo()
        claim()
        closePopup()


def collectRewards():
    tv = getImagePosition('./img/tv/tv.png')

    if exists(tv):
        openTv(tv)
    else:
        print('No TV available')
