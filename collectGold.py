from utils import ThreadWithReturnValue, check_if_not_ok, exists, getImagePosition, moveAndClick


def getGoldPosition():
    thread1 = ThreadWithReturnValue(target=getImagePosition, args=('./img/gold/gold.png', 2, .7, .5))
    thread2 = ThreadWithReturnValue(target=getImagePosition, args=('./img/gold/gold3.png', 2, .7, .5))
    thread1.start()
    thread2.start()
    image1 = thread1.join()
    image2 = thread2.join()
   
    return image1 if exists(image1) else image2

def collectGold(center):
    if not exists(center): return print('No Center....')
    edge = 300
    gold = getGoldPosition()
    if exists(gold):
        print('gold pos is ', gold, center)
        if (center[0] + edge) < gold[0]: return print('Wrong position')
        moveAndClick(gold)
        return collectGold(center)
    check_if_not_ok()
    return print('Gold not found')

# collectGold()
