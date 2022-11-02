from utils import check_if_not_ok, closePopup, getImagePositionRegion, exists, moveAndClick, delay, scroll
import mouse


def buy():
    gold = getImagePositionRegion('./img/orbs/gold.png', 1300, 300, 1600, 900)

    if not exists(gold): return print('Nothing to buy')
    i = 5
    while i > 0:
        i-=1
        moveAndClick(gold)
        delay(.5)


def shop():
    sh = getImagePositionRegion('./img/orbs/shop.png', 1300, 700, 1600, 900)

    if not exists(sh):
        print('Shop not found')
        return check_if_not_ok()

    moveAndClick(sh)
    delay(1)
    orbs = getImagePositionRegion('./img/orbs/orbs.png', 400, 600, 1400, 900)
    if not exists(orbs):
        print('No orbs')
        return closePopup()
    moveAndClick(orbs)
    delay(1)
    scroll([1550, 550], [0, 550])
    delay(1)
    buy()
    closePopup()