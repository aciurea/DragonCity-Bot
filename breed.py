from utils import (check_if_not_ok,
                    closePopup,
                    delay,
                    exists,
                    getImagePositionRegion,
                    moveAndClick)
import constants as C
import time
import math
import concurrent.futures

from utilss.drag_map import dragMapToCenter

def feed():
    feedBtn = getImagePositionRegion(C.BREED_FEED_BTN, 300, 700, 600, 850, 0.8, 3)
    if not exists(feedBtn): return print('No Feed button available')
    times = 8
    while(times > 0):
        times -= 1
        moveAndClick(feedBtn)
        delay(.2)

def get_sell_btn():
    _lst = [
        [C.BREED_SELL_BTN, 1300, 700, 1550, 860, .8, 5],
        [C.BREED_SELL_BTN_CENTER, 670, 550, 1200, 700, 0.8, 5]
    ]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        lst = executor.map(lambda args: getImagePositionRegion(*args), _lst)
        for btn in lst:
            if exists(btn): 
                print('sell btn is ', btn)
                return btn

    return [-1] 

def sellEgg():
    sell_btn = get_sell_btn()
    if not exists(sell_btn): return print('Sell btn not found')
    moveAndClick(sell_btn)
    delay(1)
    confirm_sell = getImagePositionRegion(C.BREED_CONFIRM_SELL_BTN, 795, 600, 1000, 700, 0.8, 5)
    moveAndClick(confirm_sell, 'Confirm sell not found')

def _place_egg():
    place = getImagePositionRegion(C.BREED_PLACE_BTN, 700, 550, 1000, 650, 0.8, 2)
    if not exists(place):
        return print('Place btn not found')
    moveAndClick(place)
    delay(2)

    point = _get_breeding_tree_pos()

    if not exists(point):
        return print('Point to place the egg not found')
    moveAndClick([point[0] + 70, point[1] + 32])
    dragon = getImagePositionRegion(C.BREED_DRAGON, 300, 700, 1400, 850, 0.8, 2)
    moveAndClick(dragon, 'Dragon not found ')

def placeAndFeed():
    _place_egg()
    feed()
    sellEgg()

def _hatch_terra_egg(priority='breed'):
    egg = getImagePositionRegion(C.BREED_TERRA_EGG, 100, 600, 1500, 900, 0.8, 10, 0.2)

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
    re_breed_btn = getImagePositionRegion(C.BREED_RE_BREED_BTN, 900, 600, 1400, 900, .8, 5)
    if not exists(re_breed_btn): return [-1]
    moveAndClick(re_breed_btn)
    rebreed_lst = [
        [C.BREED_BREED_BTN, 700, 600, 900, 750, .8, 5],
        [C.UTILS_CLOSE_BTN, 1400, 0, 1600, 150, 0.8, 5]
    ]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        lst = executor.map(lambda args: getImagePositionRegion(*args), rebreed_lst)
        ok = False
        for btn in lst:
            if exists(btn): 
                moveAndClick(btn)
                ok = True
        print('Finished breeding')
        return [1] if ok else [-1]

def startBreeding(priority='breed'):
    print('Start breeding')
    fast_breed(priority)

def _get_breeding_tree_pos():
    dragMapToCenter()
    return getImagePositionRegion(C.BREED_TREE, 200, 300, 700, 750, 0.8, 3)
  
def _get_breeding_rock_pos():
    dragMapToCenter()
    rock = getImagePositionRegion(C.BREED_ROCK, 100, 100, 1200, 700, 0.8, 1)
    return rock if exists(rock) else [667, 656]

def _is_hachery_displayed():
    return getImagePositionRegion(C.BREED_EGG, 400, 790, 1600, 860, 0.8, 3)

def _do_breed(breedFn = _get_breeding_tree_pos):
    breeding_place = breedFn()
    if not exists(breeding_place): return [-1]

    moveAndClick(breeding_place)
    delay(.3)
    if exists(_is_hatchery_full()):
        print('Hatchery is full, need to clean it first')
        handle_full_hatchery()
        moveAndClick(breedFn())  # the egg was not placed in hatchery. click it to place it
        # hatchery was cleaned
        delay(1)
        moveAndClick(breedFn()) # click on the breeding place in order to rebreed 
        return _re_breed()

    if exists(getImagePositionRegion(C.BREED_RE_BREED_BTN, 1170, 650, 1350, 860, .8, 5)):
        print('Normal flow')
        return _re_breed()

    if exists(_is_hachery_displayed()):
        print('Egg displayed, dispose of it')
        moveAndClick(breedFn())
        return _re_breed()
    return [-1]

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
    st = time.time()
    while exists(_hatch_terra_egg() or time.time() - st < 15):
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

    print('Tree is', is_tree_breed)
    if exists(is_tree_breed):
        delay(math.ceil(breeding_time - (time.time() - st1)))
        _place_egg_in_hatchery(breedFn=_get_breeding_tree_pos, priority=priority)
        # MAybe we can rebreeed since that sell is taking time
    print('Rock is', is_rock_breed)
    if exists(is_rock_breed):
        delay(math.ceil(breeding_time - (time.time() - st2)))
        _place_egg_in_hatchery(breedFn=_get_breeding_rock_pos, priority=priority)
        # MAybe we can rebreeed since that sell is taking time

# while 1:
#     fast_breed()

