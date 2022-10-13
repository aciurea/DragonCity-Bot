from utils import getImagePosition, moveAndClick


def checkAndCloseIfFails():
    paths = [
        './img/fails/back.png',
        './img/fails/close.png',
        './img/utils/close.png',
        './img/utils/close_video.png'
    ]

    for path in paths:
        image = getImagePosition(path, 10, 0.6)
        if (image[0] != -1):
            moveAndClick(image)
