from utils import ThreadWithReturnValue, check_if_not_ok, exists, getImagePosition, move_to_top, moveAndClick
import constants as C

def getGoldPosition():
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
    def inner_collect(times):
        if(times < 0):
            return print('Called too many times. Exists and try again')
        gold = getGoldPosition()
        if exists(gold):
            print('gold pos is ', gold)
            moveAndClick(gold)
            return inner_collect(times - 1)
        check_if_not_ok()
        return print('Gold not found')
        
    inner_collect(15)
    move_to_top()
    inner_collect(10)
# collectGold()
