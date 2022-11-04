from utils import ThreadWithReturnValue, check_if_not_ok, exists, getImagePosition, move_to_top, moveAndClick


def getGoldPosition():
    thread1 = ThreadWithReturnValue(target=getImagePosition, args=('./img/gold/gold.png', 2, .7, .5))
    thread2 = ThreadWithReturnValue(target=getImagePosition, args=('./img/gold/gold3.png', 2, .7, .5))
    thread1.start()
    thread2.start()
    image1 = thread1.join()
    image2 = thread2.join()
   
    return image1 if exists(image1) else image2

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
