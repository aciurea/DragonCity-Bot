import time
from utils import getImagePosition, moveAndClick


def checkAndCloseIfFails():
    paths = [
        './img/app_start/back.png',
        './img/app_start/close.png',
        './img/utils/close.png',
        './img/app_start/claim_yellow.png',
        './img/app_start/lucky.png',
        './img/app_start/card.png',
        './img/app_start/tap_to_open.png',
        'img/utils/piggy_close.png',
        'img/app_start/twd_close.png',
        'img/app_start/mega_pack_close.png',
        'img/app_start/legendary_close.png',

    ]

    for path in paths:
        image = getImagePosition(path, 3, 0.6)
        if (image[0] != -1):
            moveAndClick(image)
            time.sleep(1)
            return checkAndCloseIfFails()
    return

# TODO
# Update the list with all the close icons possible
