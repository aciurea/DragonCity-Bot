from utils import (check_if_not_ok,
                    delay, exists,
                    getImagePositionRegion,
                    get_json_file,
                    moveAndClick)
import constants as C
from utilss.drag_map import move_to_bottom

jsonPos = get_json_file('collectFood.json')

def get_farm_position():
   return getImagePositionRegion(C.FOOD_FARM,  *jsonPos['foodFarm'])

def _get_regrow_button():
    return getImagePositionRegion(C.FOOD_REGROW_ALL,  *jsonPos['foodRegrowAll'])

def regrowFood():
    print('inside regrowFood....')
    regrow = _get_regrow_button()
    if exists(regrow): return moveAndClick(regrow)

    farm = get_farm_position()
    if not exists(farm):
        check_if_not_ok()
        return print('Farm not found')
    moveAndClick([farm[0], farm[1] + 5])

    regrow = _get_regrow_button()
    if exists(regrow):
        moveAndClick(regrow)
        return print('Regrow successful!')
    check_if_not_ok()

def collectFood(priority = False, regrow = regrowFood):
    move_to_bottom()
    food = getImagePositionRegion(C.FOOD_IMG, *jsonPos['foodImg'])
    while(exists(food)): 
        print('Food position is ', food)
        moveAndClick(food)
        food = getImagePositionRegion(C.FOOD_IMG, *jsonPos['foodImg'])
        delay(.1)
    check_if_not_ok()
    regrow()

    if priority != False: # it is in heroic race so delay a little bit to collect the food again
        time_to_collect = 28
        delay(time_to_collect)

while 1:
  collectFood(True)  