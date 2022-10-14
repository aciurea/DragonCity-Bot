from utils import getImagePosition, moveAndClick

def getGoldPosition():
    paths = [
        './img/gold/gold.png',
        './img/gold/gold3.png'
    ]

    for path in paths:
        image = getImagePosition(path, 5, 0.85)

        if (image[0] != -1):
            return image
    return [-1, -1]


def collectGold():
    gold = getGoldPosition()

    if (gold[0] == -1):
        print('Finished collecting the gold...')
        return print('Gold not found')

    print('Gold position', gold)
    moveAndClick(gold)
    collectGold()
