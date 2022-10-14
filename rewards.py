

from utils import checkIfCanClaim, closePopup, closeVideo, commonClaim, delay, exists, getImagePosition, moveAndClick

#TODO when tv video storage, close that and close again
def claim():
    print('Go to claim')
    claimBtn = getImagePosition('./img/tv/claim.png')

    if not exists(claimBtn):
        commonClaim()
    else:
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
        print('Watching videos')
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
