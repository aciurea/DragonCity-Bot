from utils import (ThreadWithReturnValue,
                    check_if_not_ok,
                    delay, exists,
                    getImagePosition,
                    getImagePositionRegion,
                    move_to_bottom,
                    moveAndClick)


def regrowFood():
    farm = getImagePositionRegion('./img/food/farm.png', 300, 200, 1000, 600)

    if not exists(farm):
        check_if_not_ok()
        return print('Farm not found')

    moveAndClick(farm, 'Farm not found')

    regrow_all = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/food/regrow.png',  900, 700, 1100, 900, 0.8, 3)).start()
    regrow_single = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/food/regrow_0.png',  1000, 700, 1200, 900, 0.8, 3)).start()
    regrow_all = regrow_all.join()
    regrow_single = regrow_single.join()
    regrow = regrow_all if exists(regrow_all) else regrow_single

    if exists(regrow):
        moveAndClick(regrow, 'Regrow not found')
        return print('Regrow successful!')

    check_if_not_ok()
    print('Regrow not found')


def getFoodPosition():
    food = getImagePosition('./img/food/food.png', 3)

    return food if exists(food) else [-1]

def collectFood():
    def inner_collect(times):
        if times > 15:
            return print('Too many farms to collect. Safe exit')
        food = getFoodPosition()

        if exists(food):
            print('Food position is ', food)
            moveAndClick(food)
            return inner_collect(times +1)

        print('Food not ready yet or not found')
        check_if_not_ok()
      
    inner_collect(0)
    move_to_bottom()
    inner_collect(5)
    regrowFood()


def start():
    while (True):
        collectFood()
        delay(30)


# start()
