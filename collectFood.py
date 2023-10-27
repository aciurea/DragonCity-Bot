from move import move_to_bottom, moveAndClick
from timers import delay
from utils import ( check_if_not_ok,
                    exists,
                    getImagePositionRegion,
                    get_json_file,
                    )
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

def _regrow():
    regrow = _get_regrow_button()
    if exists(regrow):
        moveAndClick(regrow)
        return print('Regrow successful!')
    check_if_not_ok()
    
def regrowFood():
    farm = get_farm_position()
    if not exists(farm):
        check_if_not_ok()
        print('Farm not found')
    else:
        moveAndClick(farm)
        _regrow()

def collectFood(isHeroicRace = False, regrow = regrowFood):
    move_to_bottom()
    start = time.time()
    food = getImagePositionRegion(C.FOOD_IMG, *jsonPos['foodImg'])
    while(exists(food) and (time.time() - start) < 10): 
        print('Food position is ', food)
        moveAndClick(food)
        food = getImagePositionRegion(C.FOOD_IMG, *jsonPos['foodImg'])
        delay(.2)
    check_if_not_ok()
    regrow()

    if isHeroicRace != False: # it is in heroic race so delay a little bit to collect the food again
        time_to_collect = 28
        delay(time_to_collect)

# while 1:
#   collectFood(True)  