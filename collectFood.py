from utils import check_if_not_ok, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick, moveAndClickOnIsland


def regrowFood():
    farm = getImagePosition('./img/food/farm.png')

    if not exists(farm):
        check_if_not_ok()
        return print('Farm not found')

    moveAndClick(farm, 'Farm not found')

    regrow = getImagePositionRegion('./img/food/regrow_0.png',  1000, 700, 1200, 900, 0.8, 3)
    if exists(regrow):
        moveAndClick(regrow, 'Regrow not found')
        return print('Regrow successful!')

    check_if_not_ok()
    return print('Regrow not found')


def getFoodPosition():
    food = getImagePosition('./img/food/food.png', 3)

    return food if exists(food) else [-1]

def collectFood():
    food = getFoodPosition()

    if not exists(food):
        print('Food not ready yet or not found')
        return regrowFood()

    moveAndClick(food)
    collectFood()


def start():
    while (True):
        collectFood()
        delay(30)


# start()
