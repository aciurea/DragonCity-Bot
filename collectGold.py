from utils import ThreadWithValue, check_if_not_ok, exists, getImagePositionRegion, move_to_top, moveAndClick
import constants as C
import time

def _get_gold_position():
    list = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.GOLD_1, 50, 50, 1500, 900, .8, 1)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.GOLD_2, 50, 50, 1500, 900, .8, 1)).start()
    ]
    for thread in list:
        img = thread.join()
        if exists(img):
            return img
    return [-1]

def _inner_collect():
    start = time.time()

    while(time.time() - start < 25):
        gold = _get_gold_position()
        if exists(gold): moveAndClick(gold)
    check_if_not_ok()

def collectGold():
    _inner_collect()
    move_to_top()
    _inner_collect()
