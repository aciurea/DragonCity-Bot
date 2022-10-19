import time
from utils import closePopup, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick

# TODO improve the search of sell when the egg is placed
# try to use the moveAndClickOnIsland
def feed():
    feedBtn = getImagePosition('./img/breed/feed.png')
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    if exists(feedBtn):
        for a in arr:
            moveAndClick(feedBtn)
            time.sleep(0.5)
    return

def sellEgg():
    sell = getImagePosition('./img/breed/sell.png')

    if (sell[0] == -1):
        return print('Sell btn not found')
    moveAndClick(sell)
    confirmSell = getImagePosition('./img/breed/sell_confirmation.png')

    if (confirmSell[0] == -1):
        return print('Confirm sell not found')
    moveAndClick(confirmSell)


def placeEgg():
    place = getImagePosition('./img/breed/place.png')

    if not exists(place):
        return print('Place btn not found')
    print('found place', place)
    moveAndClick(place)

    delay(2)
    tree = getImagePosition('./img/breed/tree.png')
    moveAndClick([tree[0] + 80, tree[1] + 50])
    dragon = getImagePositionRegion('./img/breed/dragon.png', 300, 500, 1200, 900)
    if not exists(dragon):
        return print('Dragon not found ')
    moveAndClick(dragon)


def placeAndFeed():
    placeEgg()
    feed()
    sellEgg()


def hatchery(priority):
    egg = getImagePosition('./img/breed/terra_egg.png')

    if not exists(egg):
        return print('Egg not found')
    moveAndClick(egg)
    print('Hatched the egg')
    if (priority == 'breed' or priority == -1):
        return sellEgg()
    if (priority == 'hatch'):
        placeEgg()
        sellEgg()
    else:
        placeAndFeed()


def finishBreed(priority):
    icon = getImagePosition('./img/breed/finish_breed.png')

    if (icon == -1):
        return print('Breed not ready yet')
    moveAndClick(icon)
    print('Finished breeding, go to hatchery')
    hatchery(priority)


def startBreeding(priority='hatch'):
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
    delay(12)
    finishBreed(priority)
    print('Finish breeding, hatching and feeding')


def start():
    while (True):
        startBreeding('hatch')


# start()
