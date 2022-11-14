from utils import (ThreadWithReturnValue, 
                    check_if_not_ok,
                    closePopup,
                    delay,
                    exists,
                    getImagePosition,
                    getImagePositionRegion,
                    moveAndClick)
import constants as C

def feed():
    feedBtn = getImagePositionRegion(C.BREED_FEED_BTN, 300, 700, 600, 850, 0.8, 3)
    if not exists(feedBtn): return print('No Feed button available')
    times = 8
    while(times > 0):
        times -= 1
        moveAndClick(feedBtn)
        delay(.1)
           

def sellEgg():
    sell = getImagePositionRegion(C.BREED_SELL_BTN, 1099, 590, 1500, 850, .8, 2)
    if not exists(sell): return print('Sell btn not found')

    moveAndClick(sell)
    delay(.5)
    confirm_sell = getImagePositionRegion(C.BREED_CONFIRM_SELL_BTN, 800, 550, 1000, 700, 0.8, 3)

    if not exists(confirm_sell):
        return print('Confirm sell not found')
    moveAndClick(confirm_sell)


def placeEgg():
    place = getImagePositionRegion(C.BREED_PLACE_BTN, 700, 550, 1000, 650, 0.8, 2)
    if not exists(place):
        return print('Place btn not found')
    moveAndClick(place)
    delay(2)
    point = getImagePosition(C.BREED_DRAGON_PLACE_POINT, 2)
    if not exists(point):
        return print('Point to place the egg not found')
    habitat_distance = 40
    moveAndClick([point[0] - habitat_distance, point[1] - habitat_distance])
    dragon = getImagePositionRegion(C.BREED_DRAGON, 300, 700, 1400, 850, 0.8, 2)
    if not exists(dragon):
        return print('Dragon not found ')
    moveAndClick(dragon)


def placeAndFeed():
    placeEgg()
    feed()
    sellEgg()

def hatchery(priority):
    delay(.5)
    egg = getImagePositionRegion(C.BREED_TERRA_EGG, 300, 700, 1500, 850, .8, 3)

    if not exists(egg):
        check_if_not_ok()
        return print('Egg not found')

    moveAndClick(egg)
    if (priority == 'breed'):
        return sellEgg()
    if (priority == 'hatch'):
        placeEgg()
        sellEgg()
    else:
        placeAndFeed()


def breed():
    re_breed = getImagePositionRegion(C.BREED_RE_BREED_BTN, 1100, 700, 1400, 900, .8, 3)

    if not exists(re_breed):
        return print('Re-breed btn icon not found')

    moveAndClick(re_breed) #[1246, 764]
    delay(1)
    breed_btn = getImagePositionRegion(C.BREED_BREED_BTN, 700, 600, 900, 750, .8, 3)
    if exists(breed_btn):
        moveAndClick(breed_btn)
        closePopup()
        delay(13)
        print('Finish breeding')
    else: print('Breed button not found')
        
def startBreeding(priority='breed'):
    print('Start breeding')
    tree_position = getImagePosition(C.BREED_TREE, 3)

    if not exists(tree_position):
        return print('Tree not found')

    moveAndClick(tree_position)
    # here double check if the egg can be place, if not delete egg from hatchery
    breed()
    moveAndClick(tree_position)
    hatchery(priority)

def start():
    while (True):
        delay(1)
        startBreeding('hatch')

# start()
