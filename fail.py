from utils import getImagePosition, moveAndClick


def checkAndCloseIfFails():
    paths = [
        './img/fails/back.png',
        './img/fails/close.png',
        './img/utils/close.png',
        'img/utils/piggy_close.png'
    ]

    for path in paths:
        image = getImagePosition(path, 10, 0.6)
        if (image[0] != -1):
            return moveAndClick(image)

# TODO
# Update the list with all the close icons possible
