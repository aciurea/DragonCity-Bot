

import time
from utils import closePopup, closeVideo, getImagePosition, moveAndClick


def playVideo():
    time.sleep(60)
    closeVideo()


def claim():
    image = getImagePosition('./img/video/claim.png')

    if (image[0] != -1):
        moveAndClick(image)
        rewardsBtn = getImagePosition('./img/video/get_rewards_btn.png')
        if (rewardsBtn[0] == -1):
            moveAndClick([960, 450])
            time.sleep(5)
            closePopup()

    else:
        print('Nothing to claim')


def openTv():
    rewardsBtn = getImagePosition('./img/video/get_rewards_btn.png')

    if (rewardsBtn[0] == -1):
        print('No videos available')
        closePopup()
    else:
        moveAndClick(rewardsBtn)
        playVideo()
        claim()
        closePopup()


def collectRewards():
    tv = getImagePosition('./img/video/tv.png', 10, 0.5)

    if (tv[0] != -1):
        moveAndClick(tv)
        openTv()
    else:
        print('Tv not available')
        closePopup()
