import time
from utils import getImagePosition, moveAndClick


def checkAndCloseIfFails():
    paths = [
        './img/fails/back.png',
        './img/fails/close.png',
        './img/utils/close.png',
        './img/fails/claim_yellow.png',
        './img/fails/lucky.png',
        './img/fails/card.png',
        './img/fails/tap_to_open.png',
        'img/utils/piggy_close.png',
        'img/fails/twd_close.png',
        'img/fails/mega_pack_close.png',
        'img/fails/legendary_close.png',

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
