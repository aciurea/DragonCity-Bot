from utils import check_if_not_ok, closePopup, getImagePositionRegion, exists, moveAndClick, delay, scroll
import constants as C

def buy():
    gold = getImagePositionRegion(C.ORBS_GOLD, 1300, 300, 1600, 900, .8, 3)

    if not exists(gold): return print('Nothing to buy')
    buy_times = 5
    while buy_times > 0:
        buy_times -= 1
        moveAndClick(gold)
        delay(.5)


def shop():
    orbs_shop = getImagePositionRegion(C.ORBS_SHOP, 1300, 700, 1600, 900)

    if not exists(orbs_shop):
        print('Shop not found')
        return check_if_not_ok()

    moveAndClick(orbs_shop)
    delay(1)
    orbs = getImagePositionRegion(C.ORBS_ORBS, 400, 600, 1400, 900)
    if not exists(orbs):
        print('No orbs')
        return closePopup()

    moveAndClick(orbs)
    delay(1)
    scroll([1550, 550], [0, 550])
    delay(.5)
    buy()
    closePopup()