from utils import ( check_if_not_ok,
                    delay, exists,
                    getImagePositionRegion,
                    get_json_file,
                    move_to_bottom,
                    moveAndClick)
import constants as C
import time
import concurrent.futures

jsonPos = get_json_file('collectFood.json')

def get_farm_position():
   return getImagePositionRegion(C.FOOD_FARM,  *jsonPos['foodFarm'])

def _get_regrow_button():
    btns_pos = [
        [C.FOOD_REGROW_ALL,  *jsonPos['foodRegrowAll']],
        [C.FOOD_REGROW_SINGLE, *jsonPos['foodRegrowSingle']]
    ]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        btns = executor.map(lambda args: getImagePositionRegion(*args), btns_pos)
        for btn in btns:
            if exists(btn): return btn
        return [-1]

def regrowFood():
    correction = 5
    farm = get_farm_position()
    print('Farm positon is', farm)

    if not exists(farm):
        check_if_not_ok()
        return print('Farm not found')

    moveAndClick([farm[0] + correction, farm[1] + correction])

    regrow = _get_regrow_button()
    if exists(regrow):
        moveAndClick(regrow)
        return print('Regrow successful!')
    check_if_not_ok()

def collectFood(priority = False, regrow = regrowFood):
    for _ in range(2):
        start = time.time()
        food = getImagePositionRegion(C.FOOD_IMG, *jsonPos['foodImg'])
        while(exists(food) or (time.time() - start) < 10): 
            print('Food position is ', food)
            moveAndClick(food)
            food = getImagePositionRegion(C.FOOD_IMG, *jsonPos['foodImg'])
        check_if_not_ok()
        move_to_bottom()
    regrow()

    if priority != False: # it is in heroic race so delay a little bit to collect the food again
        time_to_collect = 25
        delay(time_to_collect)


collectFood()