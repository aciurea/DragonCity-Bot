from utils import getImagePosition, moveAndClick


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
            return

    return print('Regrow not found')


def getFoodPosition():
    paths = ['./img/food/food.png']

    for path in paths:
        image = getImagePosition(path)
        if (image[0] != -1):
           return image
    return [-1, -1]


def collectFood():
    image = getFoodPosition()

    if (image[0] == -1):
        print('Food not ready yet')
        regrowFood()
        return

    moveAndClick(image)
    collectFood()


# Schedule food Collection
