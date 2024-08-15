from breed import Breed
from close import check_if_ok
from collectFood import heroic_collect
from move import center_map, moveAndClick, multiple_click, multiple_fn
import constants as C
from utils import delay, exists, get_grid_monitor, getImagePositionRegion, getImagePositonCount


class Runner:
    runner_pos = [1138, 305]
    expand_pos = [975, 1225]
    collapse_pos = [1280, 385]
    work = [
            lambda: Breed.breed('feed', 10),
            lambda: heroic_collect(times=5),
            ]

    def is_runner():
        grid = get_grid_monitor()
        pos = [grid['x0'], grid['y0'], grid['x1'], grid['y2']]

        return exists(getImagePositionRegion(C.RUNNER_ICO, *pos, 0.8, 1))

    def get_claim():
        grid = get_grid_monitor()
        pos = [grid['x5'], grid['y2'], grid['x7'], grid['y5']]

        return getImagePositionRegion(C.RUNNER_CLAIM, *pos, 0.8, 1)
    
    def is_expanded():
        grid = get_grid_monitor()
        pos = [grid['x2'], grid['y1'], grid['x3'], grid['y2']]

        return exists(getImagePositionRegion(C.RUNNER_EXPANDED, *pos, 0.8, 1))

    def is_claimed():
        count = getImagePositonCount(C.RUNNER_CLAIMED)
        
        return count >= 3
    
    def run(times=0):
        if not exists(center_map()): check_if_ok()
        multiple_click(Runner.runner_pos, 5)
        delay(1)
        if Runner.is_runner():
            if not Runner.is_expanded(): multiple_click(Runner.expand_pos, 2, 0.01)
            delay(1)
            
            multiple_fn(times=3, fn=Runner.get_claim, time_between_clicks=0.5)

            if Runner.is_claimed() or times == 1: return check_if_ok()

            moveAndClick(Runner.collapse_pos)
            delay(1)
            check_if_ok()
            delay(1)
            for work in Runner.work: work()
            Runner.run(times=1)
