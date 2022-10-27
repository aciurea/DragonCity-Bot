from utils import closePopup, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick

def feed():
    feedBtn = getImagePositionRegion('./img/breed/feed.png', 300, 700, 600, 850)
    if not exists(feedBtn): return print('No Feed button available')
    times = 8
    while(times > 0):
        times -= 1
        moveAndClick(feedBtn)
        delay(.3)
           

def sellEgg(sell = [-1]):
    if not exists(sell):
        sell = getImagePositionRegion('./img/breed/sell.png', 1300, 750, 1500, 850, .8, 3)

    if not exists(sell):
        return print('Sell btn not found')
    delay(1)
    moveAndClick(sell, 'Sell btn not found')
    confirmSell = getImagePositionRegion('./img/breed/sell_confirmation.png', 800, 550, 1000, 700)

    if not exists(confirmSell):
        return print('Confirm sell not found')
    moveAndClick(confirmSell)


def placeEgg():
    place = getImagePositionRegion('./img/breed/place.png', 700, 550, 1000, 650)
    if not exists(place):
        return print('Place btn not found')
    moveAndClick(place)

    delay(2)
    tree = getImagePosition('./img/breed/tree.png')
    moveAndClick([tree[0] + 80, tree[1] + 50])
    dragon = getImagePositionRegion('./img/breed/dragon.png', 300, 700, 1400, 850)
    if not exists(dragon):
        return print('Dragon not found ')
    moveAndClick(dragon)


def placeAndFeed():
    placeEgg()
    feed()
    sellEgg()


def hatchery(priority):
    egg = getImagePositionRegion('./img/breed/terra_egg.png', 500, 700, 1400, 850)

    if not exists(egg):
        return print('Egg not found')

    moveAndClick(egg)
    print('Hatched the Terra egg')
    if (priority == 'breed' or priority == -1):
        return sellEgg([1000, 600])
    if (priority == 'hatch'):
        placeEgg()
        sellEgg()
    else:
        placeAndFeed()


def startBreeding(priority='hatch'):
    print('Start breeding')
    tree_position = getImagePosition('./img/breed/tree.png')

    if not exists(tree_position):
        return print('Tree not found')

    moveAndClick(tree_position)
    rebreed = getImagePositionRegion('./img/breed/rebreed.png', 1100, 700, 1400, 900, .8, 3)

    if not exists(rebreed):
        return print('Rebreed btn icon not found')

    moveAndClick(rebreed)
    delay(.5)
    breedBtn = getImagePositionRegion('./img/breed/breed_btn.png', 700, 600, 900, 750, .8, 3)

    if not exists(breedBtn):
        return print('Breed btn not found')

    moveAndClick(breedBtn)
    closePopup()
    delay(13)
    moveAndClick(tree_position)
    hatchery(priority)


def start():
    while (True):
        startBreeding('hatch')


# start()
