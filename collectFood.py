from utils import delay, exists, getImagePosition, getImagePositionRegion, moveAndClickOnIsland


def regrowFood():
    farm = getImagePosition('./img/food/farm.png')

    if not exists(farm):
        return print('Farm not found')
    moveAndClickOnIsland(farm, 'Farm not found', 'farm')

    paths = ['./img/food/regrow.png', './img/food/regrow2.png']

    for path in paths:
        regrow = getImagePositionRegion(path,  800, 600, 1600, 900)
        if exists(regrow):
            moveAndClickOnIsland(regrow, 'Regrow not found', 'regrow')
            return print('Regrow successful!')

    return print('Regrow not found')


def getFoodPosition():
    paths = ['./img/food/food.png']

    for path in paths:
        image = getImagePosition(path, 5)
        if exists(image):
           return image
    return [-1, -1]


def collectFood():
    food = getFoodPosition()

    if not exists(food):
        print('Food not ready yet or not found')
        return regrowFood()

    moveAndClickOnIsland(food, 'Food not found', 'food')
    return collectFood()


def start():
    while (True):
        collectFood()
        delay(30)


# start()
