from utils import ThreadWithReturnValue, check_if_not_ok, exists, getImagePosition, move_to_top, moveAndClick
import constants as C
import time

def _get_gold_position():
    list = [
        ThreadWithReturnValue(target=getImagePosition, args=(C.GOLD_1, 2, .8, .1)).start(),
        ThreadWithReturnValue(target=getImagePosition, args=(C.GOLD_2, 2, .8, .1)).start()
    ]
    for thread in list:
        img = thread.join()
        if exists(img):
            return img
    return [-1]

def collectGold():
    start = time.time()
    def _inner_collect():
        if(time.time() - start > 60):
            return print('Called too many times. Exists and try again')
        gold = _get_gold_position()
        if exists(gold):
            print('gold pos is ', gold)
            moveAndClick(gold)
            return _inner_collect()
        check_if_not_ok()
        return print('Gold not found')
        
    _inner_collect()
    move_to_top()
    start = time.time()
    _inner_collect()
# collectGold()
