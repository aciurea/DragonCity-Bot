from utils import ThreadWithReturnValue, exists, getImagePosition, moveAndClickOnIsland


def getGoldPosition():
    thread1 = ThreadWithReturnValue(target=getImagePosition, args=('./img/gold/gold.png', 5, 0.85))
    thread1.start()
    thread2 = ThreadWithReturnValue(target=getImagePosition, args=('./img/gold/gold3.png', 5, 0.85))
    thread2.start()

    image1 = thread1.join()
    image2 = thread2.join()
   
    return image1 if exists(image1) else image2

def collectGold():
    gold = getGoldPosition()

    if not exists(gold):
        print('Finished collecting the gold...')
        return print('Gold not found')

    print('Gold position', gold)
    moveAndClickOnIsland(gold, 'Gold not found', 'gold')
    collectGold()


# collectGold()
