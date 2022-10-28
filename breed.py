from asyncio import threads
from utils import ThreadWithReturnValue, closePopup, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick

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
    point = getImagePosition('./img/breed/dragon_place_point.png', 3)
    moveAndClick([point[0] - 40, point[1] - 40])
    dragon = getImagePositionRegion('./img/breed/dragon.png', 300, 700, 1400, 850)
    if not exists(dragon):
        return print('Dragon not found ')
    moveAndClick(dragon)


def placeAndFeed():
    placeEgg()
    feed()
    sellEgg()


def hatchery(priority):
    egg = getImagePosition('./img/breed/terra_egg.png', 50)

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


def startBreeding(priority='breed'):
    print('Start breeding')
    tree_position = getImagePosition('./img/breed/tree.png')

    if not exists(tree_position):
        return print('Tree not found')

    moveAndClick(tree_position)
    breed()
    delay(13)
    moveAndClick(tree_position)
    hatchery(priority)

def breed():
    rebreed = getImagePositionRegion('./img/breed/rebreed.png', 1100, 700, 1400, 900, .8, 3)

    if not exists(rebreed):
        return print('Rebreed btn icon not found')

    moveAndClick(rebreed)
    delay(.5)
    breedBtn = getImagePositionRegion('./img/breed/breed_btn.png', 700, 600, 900, 750, .8, 3)
    moveAndClick(breedBtn)
    closePopup()


def fastHatch():
    while True:
        print('Start hatching')
        list = [
            ThreadWithReturnValue(target=getImagePosition, args=('./img/breed/tree.png', 3,)),
            ThreadWithReturnValue(target=getImagePosition, args=('./img/breed/rock.png', 3)),
        ]
        for thread in list:
            thread.start()
        for thread in list:
            img = thread.join()
            if exists(img):
                moveAndClick(img)
                delay(.5)
                breed()
            else: closePopup()
        pos1 = getImagePosition('./img/breed/finish_breed.png', 3)
        if exists(pos1):
            moveAndClick(pos1)
            delay(.5)
            hatchery('hatch')
    

def fastBreed():
    print('Start fast breeding')
    pos1 = getImagePosition('./img/breed/finish_breed.png',10)
    pos1 = [pos1[0] + 40, pos1[1]+100]
    moveAndClick(pos1)
    delay(1)
    pos2 = getImagePosition('./img/breed/finish_breed.png',10)
    pos2 = [pos2[0] + 40, pos2[1]+100]
    delay(3)
    hatchery('breed')
    delay(1)
    moveAndClick(pos1)
    delay(1)
    breed()
    delay(1)
    direction = True
    
    while True:
        btn = pos2 if direction else pos1 
        direction = not direction
        moveAndClick(btn)
        delay(.5)
        hatchery('breed')
        delay(.5)
        moveAndClick(btn)
        delay(.5)
        breed()
        delay(5)
       
    

def start():
    while (True):
        fastBreed()


# start()
