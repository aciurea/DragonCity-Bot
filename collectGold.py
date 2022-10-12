import mouse
import pyautogui
from utils import getImagePosition, moveAndClick

# check close button


def moveMap(down):
    # Move from center Position
    # Get Center Image Position
    # center of the screen is 1920/ 2 = 960, 900 /2 = 450
    # Drag centet Image Position to center screen position
    # from here Move up, left, right, down, left, right
    mousePos = mouse.get_position()

    if (down == True):
        print('Move down')
        pyautogui.dragTo(mousePos[0], mousePos[1] + 100)
    else:
        pyautogui.dragTo(mousePos[0], mousePos[1] - 100)
        print('Move up')


def getGoldPosition():
    paths = [
        './img/gold/gold.png',
        './img/gold/gold2.png'
    ]

    for path in paths:
        image = getImagePosition(path)

        if (image[0] != -1):
            return image
    return [-1, -1]


def collectGold():
    gold = getGoldPosition()

    print('Gold position', gold)
    if (gold[0] == -1):
        print('Gold not found')
        return

    moveAndClick(gold)
    collectGold()
