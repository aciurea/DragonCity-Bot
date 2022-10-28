from utils import check_if_not_ok, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick, moveAndClickOnIsland


def regrowFood():
    farm = getImagePositionRegion('./img/food/farm.png', 300, 200, 1000, 600)

    if not exists(farm):
        check_if_not_ok('farm')
        return print('Farm not found')

    moveAndClick(farm, 'Farm not found')

    regrow = getImagePositionRegion('./img/food/regrow_0.png',  1000, 700, 1200, 900, 0.8, 3)
    if exists(regrow):
        moveAndClick(regrow, 'Regrow not found')
        return print('Regrow successful!')

    check_if_not_ok('regrow')
    print('Regrow not found')


def getFoodPosition():
    food = getImagePosition('./img/food/food.png', 3)

    return food if exists(food) else [-1]

def collectFood():
    food = getFoodPosition()

    if exists(food):
        print('Food position is ', food)
        moveAndClick(food)
        delay(.3)
        return collectFood()

    print('Food not ready yet or not found')
    check_if_not_ok('Food')
    return regrowFood()


def start():
    while (True):
        collectFood()
        delay(30)


# start()
