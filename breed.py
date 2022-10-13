import time
from utils import closePopup, getImagePosition, moveAndClick


def removeEgg():
    egg = getImagePosition('./img/breed/terra_egg.png')

    if (egg[0] == -1):
        return print('Egg not found')
    moveAndClick(egg)
    sell = getImagePosition('./img/breed/sell.png')

    if (sell[0] == -1):
        return print('Sell btn not found')
    moveAndClick(sell)
    confirmSell = getImagePosition('./img/breed/sell_confirmation.png')

    if (confirmSell[0] == -1):
        return print('Confirm sell not found')
    moveAndClick(confirmSell)


def hatch():
    hatchery = getImagePosition('./img/breed/hatchery.png')

    if (hatchery[0] == -1):
        return print('Hatchery not found')
    moveAndClick(hatchery)
    time.sleep(3)
    removeEgg()


def finishBreed():
    icon = getImagePosition('./img/breed/finish_breed.png')

    if (icon == -1):
        return print('Breed not ready yet')
    moveAndClick(icon)
    removeEgg()


def startBreeding():
    print('Start breeding')
    tree = getImagePosition('./img/breed/tree.png')

    if (tree[0] == -1):
        return print('Tree not found')
    moveAndClick(tree)

    rebreed = getImagePosition('./img/breed/rebreed.png')

    if (rebreed[0] == -1):
        return print('Rebreed icon not found')
    moveAndClick(rebreed)

    breedBtn = getImagePosition('./img/breed/breed_btn.png')

    if (breedBtn[0] == -1):
        return print('Breed btn not found')
    moveAndClick(breedBtn)
    closePopup()
    time.sleep(10)
    finishBreed()
    print('finish breeding')
    startBreeding()


startBreeding()
# TODO
# remove the start breeding recursive call in order to start the global script
