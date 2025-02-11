from move import moveAndClick, multiple_click
from timers import delay
from utils import exists, getImagePositionRegion, get_screen_resolution
from position_map import Position_Map
from screen import Screen


class Farm:
    screen_pos = get_screen_resolution()

    # relative to the center point.
    farm_pos = Screen.get_pos([0.5520834, 0.48])
    multiple_food_pos = Screen.get_pos([0.4864583, 0.71296296])
    regrow_pos = Screen.get_pos([0.602604167, 0.85740])
    food_bbox = [*Screen.get_pos([0.366145834, 0.2574]), *Screen.get_pos([0.7364583, 0.951851852])]

    @staticmethod
    def collect_food():
        if exists(Position_Map.center_map()):
            Farm._collect_each_farm()
            Farm._regrow_food()

    @staticmethod
    def fast_collect(times=30):
        if times > 0 and exists(Position_Map.center_map()):
            multiple_click(Farm.multiple_food_pos, 4, 0.01)
            Farm._regrow_food()
            delay(30)
            return Farm.fast_collect(times - 1)

    @staticmethod
    def _collect_each_farm():
        farm_num = 20
        base = './img/food'
        path = f'{base}/{Farm.screen_pos}_food.png'

        food_pos = getImagePositionRegion(path, *Farm.food_bbox, 0.8, 1)
        while exists(food_pos) and farm_num > 0:
            farm_num -= 1
            moveAndClick(food_pos)
            delay(.5)
            food_pos = getImagePositionRegion(path, *Farm.food_bbox, 0.8, 1)

    @staticmethod
    def _regrow_food():
        multiple_click(Farm.farm_pos, 3, 0.1)
        delay(.7)
        moveAndClick(Farm.regrow_pos)
