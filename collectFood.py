from utils import (ThreadWithReturnValue,
                    check_if_not_ok,
                    delay, exists,
                    getImagePosition,
                    getImagePositionRegion,
                    move_to_bottom,
                    moveAndClick)
import constants as C


def get_farm_position():
    farms = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.FOOD_FARM_WINTER,  200, 200, 1000, 700, 0.8, 10)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.FOOD_FARM,  200, 200, 1000, 700, 0.8, 10)).start(),
    ]

    for farm_pos in farms:
        farm = farm_pos.join()
        print(1)
        if exists(farm): return farm
    return [-1]

def regrowFood():
    farm = get_farm_position()

    print('Farm positon is', farm)

    if not exists(farm):
        check_if_not_ok()
        return print('Farm not found')

    moveAndClick([farm[0] + 5, farm[1] + 5])

    regrow_all = ThreadWithReturnValue(target=getImagePositionRegion, args=(C.FOOD_REGROW_ALL,  900, 700, 1100, 900, 0.8, 3)).start()
    regrow_single = ThreadWithReturnValue(target=getImagePositionRegion, args=(C.FOOD_REGROW_SINGLE,  1000, 700, 1200, 900, 0.8, 3)).start()
    regrow_all = regrow_all.join()
    regrow_single = regrow_single.join()
    regrow = regrow_all if exists(regrow_all) else regrow_single

    if exists(regrow):
        moveAndClick(regrow)
        return print('Regrow successful!')

    check_if_not_ok()

def collectFood(priority = False):
    def inner_collect(times = 0):
        if times > 10:
            return print('Too many farms to collect. Safe exit')
        food = getImagePosition(C.FOOD_IMG, 2, 0.8, 0.1)

        if exists(food):
            print('Food position is ', food)
            moveAndClick(food)
            return inner_collect(times +1)

        print('Food not ready yet or not found')
        check_if_not_ok()
      
    inner_collect()
    move_to_bottom()
    inner_collect(5)
    regrowFood()

    if priority != False: # it is in heroic race so delay a little bit to collect the food again
        time_to_collect = 25
        delay(time_to_collect)

def start():
    while (True):
        collectFood()
        delay(30)


# start()
