from utils import delay, exists, getImagePosition, moveAndClick


def regrowFood():
    farm = getImagePosition('./img/food/farm.png')

    if (farm[0] == -1):
        return print('Farm not found')
    moveAndClick(farm)

    paths = ['./img/food/regrow.png', './img/food/regrow2.png']

    for path in paths:
        regrow = getImagePosition(path)
        if (regrow[0] != -1):
            moveAndClick(regrow)
            return print('Regrow successful!')

    return print('Regrow not found')


def getFoodPosition():
    paths = ['./img/food/food.png']

    for path in paths:
        image = getImagePosition(path, 5)
        if (image[0] != -1):
           return image
    return [-1, -1]


def collectFood(priority=-1):
    print('collecting food')
    food = getFoodPosition()

    if exists(food):
        moveAndClick(food)
        return collectFood(priority)

    print('Food not ready yet')
    regrowFood()
    if (priority == -1):
        return
    delay(30)
