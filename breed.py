from utils import ( ThreadWithValue, check_if_not_ok,
                    closePopup,
                    delay, dragMapToCenter,
                    exists,
                    getImagePositionRegion,
                    moveAndClick)
import constants as C
import time
import math
import concurrent.futures

def feed():
    feedBtn = getImagePositionRegion(C.BREED_FEED_BTN, 300, 700, 600, 850, 0.8, 3)
    if not exists(feedBtn): return print('No Feed button available')
    times = 8
    while(times > 0):
        times -= 1
        moveAndClick(feedBtn)
        delay(.2)
           

def sellEgg():
    sell_1, sell_2 = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.BREED_SELL_BTN, 800, 470, 1300, 700, .8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.BREED_SELL_BTN, 1300, 700, 1530, 850, .8, 3)).start(),
    ]
    sell_1 = sell_1.join()
    sell_2 = sell_2.join()
    sell = sell_1 if exists(sell_1) else sell_2
    if not exists(sell): return print('Sell btn not found')
    
    moveAndClick(sell)
    delay(1)
    confirm_sell = getImagePositionRegion(C.BREED_CONFIRM_SELL_BTN, 800, 550, 1000, 700, 0.8, 3)

    if not exists(confirm_sell):
        return print('Confirm sell not found')
    moveAndClick(confirm_sell)
    delay(1)

def _place_egg():
    place = getImagePositionRegion(C.BREED_PLACE_BTN, 700, 550, 1000, 650, 0.8, 2)
    if not exists(place):
        return print('Place btn not found')
    moveAndClick(place)
    delay(2)

    point = _get_breeding_tree_pos()

    if not exists(point):
        return print('Point to place the egg not found')
    moveAndClick([point[0] + 65, point[1] + 32])
    dragon = getImagePositionRegion(C.BREED_DRAGON, 300, 700, 1400, 850, 0.8, 2)
    if not exists(dragon):
        return print('Dragon not found ')
    moveAndClick(dragon)


def placeAndFeed():
    _place_egg()
    feed()
    sellEgg()

def _hatch_terra_egg(priority='breed'):
    delay(.5)
    egg = getImagePositionRegion(C.BREED_TERRA_EGG, 100, 600, 1500, 900, 0.8, 3)

    if not exists(egg):
        check_if_not_ok()
        print('Egg not found')
        return [-1]

    moveAndClick(egg)
    if (priority == 'breed'):
        sellEgg()
        return [1]
    if (priority == 'hatch'):
        _place_egg()
        sellEgg()
    else:
        placeAndFeed()
    return [1]

def _re_breed():
    re_breed_btn = getImagePositionRegion(C.BREED_RE_BREED_BTN, 1100, 700, 1400, 900, .8, 3)

    if not exists(re_breed_btn): return [-1]

    moveAndClick(re_breed_btn) #[1246, 764]
    delay(1)
    breed_btn = getImagePositionRegion(C.BREED_BREED_BTN, 700, 600, 900, 750, .8, 3)
    if exists(breed_btn):
        moveAndClick(breed_btn)
        closePopup()
        print('Finish breeding')
    return [1]
        
def startBreeding(priority='breed'):
    print('Start breeding')
    fast_breed(priority)

def start():
    while (True):
        delay(3)
        fast_breed('breed')

def _get_breeding_tree_pos():
    dragMapToCenter()
    lst = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.BREED_TREE, 400, 400, 550, 700, 0.8, 2)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.BREED_WINTER_TREE, 400, 400, 550, 700, 0.8, 2)).start()
    ]

    for tree_pos in lst:
        tree_pos = tree_pos.join()
        if exists(tree_pos): return tree_pos
    return [-1]

def _get_breeding_rock_pos():
    dragMapToCenter()
    summer, winter = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.BREED_ROCK, 100, 100, 1200, 700, 0.8, 2)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.BREED_WINTER_ROCK, 100, 100, 1200, 700, 0.8, 2)).start()
    ]
    summer = summer.join()
    winter = winter.join()
    return [winter[0]+ 20, winter[1]] if exists(winter) else summer

def _is_hachery_displayed():
    return getImagePositionRegion(C.BREED_EGG, 400, 790, 1600, 860, 0.8, 2)

def _do_breed(breedFn = _get_breeding_tree_pos):
    # scenario 1, there is an egg and hatchery full message displayed
    # scenario 2, there is an egg and hatchery is displayed
    # scenario 3, rebreed btn is displayed
    breeding_place = breedFn()
    if not exists(breeding_place): return [-1]
      
    moveAndClick(breeding_place)
    delay(.5)
    # scenario 1
    if exists(_is_hatchery_full()):
        print('Scenario 1')
        handle_full_hatchery()
        delay(.3)
        moveAndClick(breedFn())  # the egg was not placed in hatchery. click it to place it
        delay(1)
        moveAndClick(breedFn()) # click on the breeding place in order to rebreed 
        delay(.3)
        return _re_breed()
     
    # scenario 2
    if exists(_is_hachery_displayed()):
        print('Scenario 2')
        delay(.3)
        moveAndClick( breedFn())
        delay(.3)
        return _re_breed()
   
   # scenario 3
    print('scenario 3')
    return _re_breed()

def _is_hatchery_full():
    return getImagePositionRegion(C.BREED_HATCHERY_FULL, 900, 370, 1200, 500,0.8, 2)

def _place_egg_in_hatchery(breedFn, priority):
    position = breedFn()
    print('to place egg in hatchery pos ', position)
    moveAndClick(position)
    
    if exists(_is_hatchery_full()): return handle_full_hatchery()
     
    return _hatch_terra_egg(priority)

def _get_all_egg_positions():
    #486 + 140, 6 times
    i = 6
    lst = []
    st = 486
    step = 140
    while( i >= 0):
        egg = getImagePositionRegion(C.BREED_EGG, st, 790, st + step, 860, 0.8, 2)
        st += step
        i -= 1
        if exists(egg):
            lst.append(egg)
    return lst

def _place_egg_in_dragonarium():
    delay(2)
    dragMapToCenter()
    delay(1)
    moveAndClick([738, 627])
    return [1]

def handle_full_hatchery():
    closePopup()
    hatchery = getImagePositionRegion(C.BREED_HATCHERY, 200, 100, 1100, 800, 0.8, 2)
    if not exists(hatchery):
        print('Hatchert could not be found')
        return [-1]
    moveAndClick(hatchery)

    while exists(_hatch_terra_egg()):
        print('terra egg found')
        delay(.3)
    
    # for egg_position in _get_all_egg_positions():
    #     moveAndClick(egg_position)
    #     place = getImagePositionRegion(C.BREED_PLACE_BTN, 700, 550, 1000, 650, 0.8, 2)
    #     if not exists(place):
    #         print('Place btn not found')
    #         closePopup()
    #         delay(1)
    #         continue
    #     moveAndClick(place)
    #     _place_egg_in_dragonarium()
      
def fast_breed(priority='breed'):
    # terra_egg breed takes 12s
    # terra_egg hatch takes 15s
    breeding_time = 11
    is_tree_breed = _do_breed(breedFn=_get_breeding_tree_pos)
    st1 = time.time()
    delay(.3)
    is_rock_breed =_do_breed(breedFn=_get_breeding_rock_pos)
    st2 = time.time()

    if exists(is_tree_breed):
        delay(math.ceil(breeding_time - (time.time() - st1)))
        _place_egg_in_hatchery(breedFn=_get_breeding_tree_pos, priority=priority)
       
    if exists(is_rock_breed):
        delay(math.ceil(breeding_time - (time.time() - st2)))
        _place_egg_in_hatchery(breedFn=_get_breeding_rock_pos, priority=priority)

# start()
