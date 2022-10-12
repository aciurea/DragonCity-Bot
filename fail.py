from utils import getImagePosition, moveAndClick


def checkAndCloseIfFails():
    paths = [
        './img/fails/back.png',
        './img/utils/close.png'
    ]

    for path in paths:
        image = getImagePosition(path)
        if (image[0] != -1):
            moveAndClick(image)
