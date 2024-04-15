from breed import Breed
from close import check_if_ok
from collectFood import heroic_collect
from move import center_map, moveAndClick, multiple_click
import constants as C
from utils import delay, exists, get_grid_monitor, getImagePositionRegion


class Runner:
    runner_pos = [1138, 305]
    expand_pos = [1188, 1252]
    collapse_pos = [1221, 426]
    work = [
            lambda: Breed.breed('feed', 15),
            heroic_collect
            ]

    def is_runner():
        grid = get_grid_monitor()
        pos = [grid['x0'], grid['y0'], grid['x1'], grid['y2']]

        return exists(getImagePositionRegion(C.RUNNER_ICO, *pos, 0.8, 1))

    def get_claim():
        grid = get_grid_monitor()
        pos = [grid['x5'], grid['y2'], grid['x7'], grid['y5']]

        return getImagePositionRegion(C.RUNNER_CLAIM, *pos, 0.8, 1)

    def run():
        center_map()
        multiple_click(Runner.runner_pos, 5)
        delay(1)
        if Runner.is_runner():
            multiple_click(Runner.expand_pos, 20)
            delay(1)

            times = 3
            while times > 0:
                times -= 1
                moveAndClick(Runner.get_claim())
            moveAndClick(Runner.collapse_pos)
            delay(1)
            check_if_ok()
            delay(1)
            for work in Runner.work:
                work()


# Runner.run()