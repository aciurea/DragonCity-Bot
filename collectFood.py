from utils import (ThreadWithValue,
                    check_if_not_ok,
                    delay, exists,
                    getImagePositionRegion,
                    move_to_bottom,
                    moveAndClick)
import constants as C
import time


def get_farm_position():
    farms = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.FOOD_FARM_WINTER,  200, 200, 1000, 700, 0.8, 10)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.FOOD_FARM,  200, 200, 1000, 700, 0.8, 10)).start(),
    ]

    for farm_pos in farms:
        farm = farm_pos.join()
        print(1)
        if exists(farm): return farm
    return [-1]

def _get_regrow_button():
    btns =  [
        ThreadWithValue(target=getImagePositionRegion, args=(C.FOOD_REGROW_ALL,  900, 700, 1100, 900, 0.8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.FOOD_REGROW_SINGLE,  1000, 700, 1200, 900, 0.8, 3)).start()
    ]
    for btn in btns:
        btn = btn.join()
        if exists(btn): return btn
    return [-1]

def regrowFood():
    farm = get_farm_position()

    print('Farm positon is', farm)

    if not exists(farm):
        check_if_not_ok()
        return print('Farm not found')

    moveAndClick([farm[0] + 5, farm[1] + 5])

    regrow = _get_regrow_button()
    if exists(regrow):
        moveAndClick(regrow)
        return print('Regrow successful!')
    check_if_not_ok()

def collectFood(priority = False):
    def inner_collect():
        start = time.time()

        while((time.time() - start) < 10): 
            food = getImagePositionRegion(C.FOOD_IMG, 300, 100, 1500, 900, 0.8, 1)

            if exists(food):
                print('Food position is ', food)
                moveAndClick(food)
        check_if_not_ok()
      
    inner_collect()
    move_to_bottom()
    inner_collect()
    regrowFood()

    if priority != False: # it is in heroic race so delay a little bit to collect the food again
        time_to_collect = 25
        delay(time_to_collect)

def start():
    while (True):
        collectFood()
        delay(30)


# start()
