from utils import (ThreadWithReturnValue, 
                    check_if_not_ok,
                    closePopup,
                    delay,
                    exists,
                    getImagePosition,
                    getImagePositionRegion,
                    moveAndClick)

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
    place = getImagePositionRegion('./img/breed/place.png', 700, 550, 1000, 650, 0.8, 2)
    if not exists(place):
        return print('Place btn not found')
    moveAndClick(place)

    delay(2)
    point = getImagePosition('./img/breed/dragon_place_point.png', 2)
    moveAndClick([point[0] - 40, point[1] - 40])
    dragon = getImagePositionRegion('./img/breed/dragon.png', 300, 700, 1400, 850, 0.8, 2)
    if not exists(dragon):
        return print('Dragon not found ')
    moveAndClick(dragon)


def placeAndFeed():
    placeEgg()
    feed()
    sellEgg()


def hatchery(priority, pos=[-1]):
    egg = pos if exists(pos) else getImagePositionRegion('./img/breed/terra_egg.png', 300, 700, 1500, 850, .8, 5)

    if not exists(egg):
        check_if_not_ok()
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
    # here double check if the egg can be place, if not delete egg from hatchery
    breed()
    delay(13)
    moveAndClick(tree_position)
    hatchery(priority)

def breed():
    rebreed = getImagePositionRegion('./img/breed/rebreed.png', 1100, 700, 1400, 900, .8, 3)

    if not exists(rebreed):
        return print('Rebreed btn icon not found')

    moveAndClick(rebreed) #[1246, 764]
    delay(1)
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
    print('Start fast breeding....')
    # take egg and hatch first place
    pos1 = getImagePositionRegion('./img/breed/finish_breed.png', 100, 200, 1100, 700, .8, 5)
    pos1 = [pos1[0] + 40, pos1[1]+100]
    print('pos1  is ', pos1)
    moveAndClick(pos1)
    delay(1)
    hatchery('breed')

    # take egg and hatch and rebreed second place
    print('start looking for the second egg...')
    pos2 = getImagePositionRegion('./img/breed/finish_breed.png', 100, 200, 1100, 700, .8, 5)
    pos2 = [pos2[0] + 40, pos2[1]+100]
    print('pos2 is ', pos2)
    moveAndClick(pos2)
    delay(1)
    hatchery('breed')
    delay(1)
    moveAndClick(pos2)
    delay(1)
    breed()
    delay(1)
    # rebreed first place
    moveAndClick(pos1)
    delay(1)
    breed()

    delay(7) # wait for the egg to be ready for heatching
    time = 2
    while 1:
        moveAndClick(pos2)
        delay(time)
        hatchery('breed', [828, 772]) # 2s
        delay(time)
        moveAndClick(pos2)
        delay(time)
        breed() # 2s 
        delay(time)
        check_if_not_ok()
        
        ## total min 9s

        moveAndClick(pos1)
        delay(time)
        hatchery('breed', [828, 772]) # min 2s
        delay(time)
        moveAndClick(pos1)
        delay(time) 
        breed()# min 2s
        delay(time)
        check_if_not_ok()
        ## tatal 9s

def start():
    while (True):
        delay(1)
        startBreeding('hatch')


# start()
