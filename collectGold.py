from screeninfo import get_monitors
from move import center_map, fast_click, move_to_bottom, move_to_left, move_to_right, move_to_top, moveAndClick
from utils import ThreadWithValue, check_if_not_ok, exists, get_int, getImagePositionRegion
import constants as C
import time

def _get_gold_position():
    [res] = get_monitors()
    y_start = get_int(0.12 * res.height) # do not search on the top. usually the top bar is 12% of the entire height
    y_end = get_int(0.77 * res.height) # do not go over 77& of the height as it might click on a habitat and gold icon will be displayed
    x_start = get_int(0.08 * res.width) # do not go over this width since we have the left bar
    x_end = get_int(0.89 * res.width) # do not go over this width since we have the right bar

    list = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.GOLD_1, x_start, y_start, x_end, y_end, .8, 1)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.GOLD_2, x_start, y_start, x_end, y_end, .8, 1)).start()
    ]
    for thread in list:
        img = thread.join()
        if exists(img): return img
    return [-1]

def _inner_collect():
    start = time.time()
    gold_pos =_get_gold_position()

    while(exists(gold_pos) and time.time() - start < 15):
        print('Gold pos is', gold_pos)
        moveAndClick(gold_pos)
        gold_pos = _get_gold_position()
    check_if_not_ok()

def collectGold():
    center_map()
    # custom implementation. There are one over another habitats at this position. just click 50 times to improve collection of gold
    for _ in range(35): fast_click([452, 643])

    actions = [move_to_bottom, move_to_top, move_to_left, move_to_right]
    for action in actions:
        action()
        _inner_collect()
        center_map()