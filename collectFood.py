from close import check_if_ok
from move import center_map, drag_map_to_the_top, is_artifact_at_pos, moveAndClick
from timers import delay
from utils import (exists, getImagePositionRegion, get_grid_monitor)
import constants as C
import time

class FoodCollector:
    grid = get_grid_monitor()
    FARM_POS = None
    FOOD_POS = []
    last_time = 0

    @staticmethod
    def _get_farm_position():
        if FoodCollector.FARM_POS is None or not exists(FoodCollector.FARM_POS):
            pos = [
                FoodCollector.grid['x4'],
                FoodCollector.grid['y1'],
                FoodCollector.grid['x6'],
                FoodCollector.grid['y3']
            ]
            FoodCollector.FARM_POS = getImagePositionRegion(C.FOOD_FARM, *pos, 0.8, 2)

            if exists(FoodCollector.FARM_POS):
                FoodCollector.FARM_POS = [FoodCollector.FARM_POS[0] + 5, FoodCollector.FARM_POS[1] + 10] # add some correction due to screenshot image.
        return FoodCollector.FARM_POS

    @staticmethod
    def _get_regrow_button():
        pos = [FoodCollector.grid['x4'], FoodCollector.grid['y4'], FoodCollector.grid['x6'], FoodCollector.grid['y6']]

        return getImagePositionRegion(C.FOOD_REGROW_ALL, *pos, 0.8, 2)

    @staticmethod
    def _regrow():
        regrow = FoodCollector._get_regrow_button()
     
        if exists(regrow): moveAndClick(regrow)
        else: check_if_ok()

    @staticmethod
    def regrowFood():
        farm = FoodCollector._get_farm_position()
        if exists(farm):
            moveAndClick(farm)
            delay(.2)
            FoodCollector._regrow()
        else: print('Farm not found')

    @staticmethod
    def collect_food_by_cached_pos():
        for food_pos in FoodCollector.FOOD_POS: moveAndClick(food_pos)

    def clear_cache():
        if time.time() - FoodCollector.last_time > 60:
            FoodCollector.FOOD_POS = []

    def collect_each_farm_and_store_pos(is_artifact_pos_correctly):
        start = time.time()
        limit_to_find_food = 15
        pos = [
            FoodCollector.grid['x2'],
            FoodCollector.grid['y0'],
            FoodCollector.grid['x6'],
            FoodCollector.grid['y5']
        ]
        food_pos = getImagePositionRegion(C.FOOD_IMG, *pos, 0.8, 2)

        while exists(food_pos) and (time.time() - start) < limit_to_find_food:
            food_pos = [food_pos[0] + 5, food_pos[1] + 15] # add some correction due to screenshot image.
            if(is_artifact_pos_correctly): FoodCollector.FOOD_POS.append(food_pos)
            else: FoodCollector.FOOD_POS = []
            moveAndClick(food_pos)
            delay(.2)
            food_pos = getImagePositionRegion(C.FOOD_IMG, *pos, 0.8, 2)

    @staticmethod
    def collectFood(isHeroicRace=False):
        if not exists(center_map()): return check_if_ok()
        is_artifact_pos_correctly = is_artifact_at_pos(drag_map_to_the_top())

        FoodCollector.clear_cache()
        if(len(FoodCollector.FOOD_POS) > 0): FoodCollector.collect_food_by_cached_pos()
        else: FoodCollector.collect_each_farm_and_store_pos(is_artifact_pos_correctly)

        # check_if_ok() TODO move it somewhere else
        FoodCollector.regrowFood()
        FoodCollector.last_time = time.time()

        if isHeroicRace:
            time_to_collect = 27
            delay(time_to_collect)
        print('Food collected')

def collect_food(isHeroicRace = False):
    return FoodCollector.collectFood(isHeroicRace)  
 
def heroic_collect(times = 15):
    while times > 0:
        times -= 1
        collect_food(isHeroicRace=True)