from screeninfo import get_monitors
from close import check_if_ok
from move import center_map, drag_map_to_the_top, is_artifact_at_pos, moveAndClick
from timers import delay
from utils import (exists, get_int,
                    getImagePositionRegion,
                    get_json_file)
import constants as C
import time

class FoodCollector:
    jsonPos = get_json_file('collectFood.json')
    FARM_POS = None
    REGROW_POS = None
    [res] = get_monitors()
    X_START = get_int(0.4 * res.width)
    Y_START = get_int(0.76 * res.height)
    X_END = get_int(0.82 * res.width)
    Y_END = res.height
    FOOD_POS = []
    CACHE_INVALIDATION_TIMES = 30
    _run_times = 0
    _count = 0

    @staticmethod
    def _get_farm_position():
        if FoodCollector.FARM_POS is None or not exists(FoodCollector.FARM_POS):
            FoodCollector.FARM_POS = getImagePositionRegion(C.FOOD_FARM, *FoodCollector.jsonPos['foodFarm'])
            FoodCollector.FARM_POS = [FoodCollector.FARM_POS[0] + 5, FoodCollector.FARM_POS[1] + 10] # add some correction due to screenshot image.
        return FoodCollector.FARM_POS

    @staticmethod
    def _get_regrow_button():
        return getImagePositionRegion(C.FOOD_REGROW_ALL, FoodCollector.X_START, FoodCollector.Y_START, FoodCollector.X_END, FoodCollector.Y_END, 0.8, 3)

    @staticmethod
    def _regrow():
        regrow = FoodCollector._get_regrow_button()
     
        if exists(regrow):
            moveAndClick(regrow)
            FoodCollector._count += 1
            print('Regrow successful!', FoodCollector._count)
        check_if_ok()

    @staticmethod
    def regrowFood():
        farm = FoodCollector._get_farm_position()
        if exists(farm):
            moveAndClick(farm)
            FoodCollector._regrow()
        else:
            check_if_ok()
            print('Farm not found')

    @staticmethod
    def collect_food_by_cached_pos():
        for food_pos in FoodCollector.FOOD_POS:
            moveAndClick(food_pos)

    def clear_cache():
        if FoodCollector._run_times >= FoodCollector.CACHE_INVALIDATION_TIMES:
            FoodCollector.FOOD_POS = []
            FoodCollector._run_times = 0

    def collect_each_farm_and_store_pos(is_artifact_pos_correctly):
        start = time.time()
        food_pos = getImagePositionRegion(C.FOOD_IMG, *FoodCollector.jsonPos['foodImg'])
        while exists(food_pos) and (time.time() - start) < 10:
            food_pos = [food_pos[0] + 5, food_pos[1] + 15] # add some correction due to screenshot image.
            if(is_artifact_pos_correctly): FoodCollector.FOOD_POS.append(food_pos)
            else: FoodCollector.FOOD_POS = []
            moveAndClick(food_pos)
            food_pos = getImagePositionRegion(C.FOOD_IMG, *FoodCollector.jsonPos['foodImg'])
            delay(.5)

    @staticmethod
    def collectFood(isHeroicRace=False, regrow=regrowFood):
        center_map()
        is_artifact_pos_correctly = is_artifact_at_pos(drag_map_to_the_top())

        FoodCollector.clear_cache()
        if(len(FoodCollector.FOOD_POS) > 0): FoodCollector.collect_food_by_cached_pos()
        else: FoodCollector.collect_each_farm_and_store_pos(is_artifact_pos_correctly)
        check_if_ok()
        regrow()
        FoodCollector._run_times += 1

        if isHeroicRace:
            time_to_collect = 24
            delay(time_to_collect)

def collect_food(isHeroicRace = False):
    return FoodCollector.collectFood(isHeroicRace)  
 
def heroic_collect():
    times = 15
    while times > 0:
        times -= 1
        collect_food(isHeroicRace=True)