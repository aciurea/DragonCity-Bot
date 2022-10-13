

import time
from utils import checkIfCanClaim, closePopup, closeVideo, getImagePosition, moveAndClick

def claim():
    image = getImagePosition('./img/video/claim.png')

    # TODO fix it this is wrong fix it once the tv is available
    return

    if (image[0] != -1):
        moveAndClick(image)
        rewardsBtn = getImagePosition('./img/video/get_rewards_btn.png')
        if (rewardsBtn[0] == -1):
            moveAndClick([960, 450])
            time.sleep(5)
            closeVideo()

    else:
        print('Nothing to claim')


def openTv():
    rewardsBtn = getImagePosition('./img/video/get_rewards_btn.png')

    if (rewardsBtn[0] == -1):
        print('No videos available')
        return closePopup()
    else:
        moveAndClick(rewardsBtn)
        checkIfCanClaim()
        claim()
        closePopup()


def collectRewards():
    tv = getImagePosition('./img/video/tv.png')

    if(tv[0] == -1):
        return print('No TV available')

    moveAndClick(tv)
    openTv()

