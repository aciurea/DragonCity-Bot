from screeninfo import get_monitors
from close import check_if_ok
from move import center_map, fast_click, drag_map_to_the_bottom, drag_map_to_the_left, drag_map_to_the_right, drag_map_to_the_top, is_artifact_at_pos, moveAndClick
from utils import ThreadWithValue, exists, get_int, getImagePositionRegion
import constants as C
import time
import concurrent.futures

def _get_gold_position():
    [res] = get_monitors()
    y_start = get_int(0.12 * res.height) # do not search on the top. usually the top bar is 12% of the entire height
    y_end = get_int(0.77 * res.height) # do not go over 77& of the height as it might click on a habitat and gold icon will be displayed
    x_start = get_int(0.08 * res.width) # do not go over this width since we have the left bar
    x_end = get_int(0.89 * res.width) # do not go over this width since we have the right bar

    list = [
        [C.GOLD_1, x_start, y_start, x_end, y_end, .8, 1],
        [C.GOLD_2, x_start, y_start, x_end, y_end, .8, 1]
    ]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        btns = executor.map(lambda args: getImagePositionRegion(*args), list) 
        for btn in btns:
            if exists(btn): return btn
    return [-1]

def _inner_collect():
    start = time.time()
    gold_pos =_get_gold_position()

    while(exists(gold_pos) and time.time() - start < 15):
        print('Gold pos is', gold_pos)
        moveAndClick(gold_pos)
        gold_pos = _get_gold_position()
    check_if_ok()

def collectGold():
    # custom implementation. There are one over another habitats at this position. just click 50 times to improve collection of gold
    if is_artifact_at_pos([1280, 800]):
        for _ in range(50): fast_click([452, 643])

    actions = [drag_map_to_the_bottom, drag_map_to_the_top, drag_map_to_the_left, drag_map_to_the_right]
    for action in actions:
        action()
        _inner_collect()
        center_map()

# collectGold()