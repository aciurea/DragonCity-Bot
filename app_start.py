# feeling lucky
from constants import APP_START_CLAIM_BTN_1, APP_START_CLAIM_BTN_2, APP_START_DIVINE_CLOSE
from utils import (ThreadWithReturnValue,
                    closePopup,
                    delay,
                    exists,
                    getImagePositionRegion,
                    moveAndClick,
                    openChest
                )


feeling_lucky = {
    'x1': 642,
    'x2': 955,
    'y1': 705,
    'y2': 805,
}
# delay 3s
card = {
    'x1': 500,
    'x2': 1000,
    'y1': 320,
    'y2': 440,
}

# delay 3
# close popup
# delay 1s
# claim_yellow
claim_btn = {
    'x1': 670,
    'x2': 930,
    'y1': 710,
    'y2': 795,
}
# open chest, might be
    #tap to open
    #claim
    # x1: 690, x2: 920, y1: 650, y2: 765

#delay1s
# daily claim, same as claim_yellow
# delay1s
# open chest()
# delay1s
# closePopup

def check_if_can_claim_daily():
    claim_btn_1, claim_btn2 = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(APP_START_CLAIM_BTN_1, 670, 710, 930, 795, 0.8, 2)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(APP_START_CLAIM_BTN_2, 670, 710, 930, 795, 0.8, 2)).start()
    ]
    claim_btn2 = claim_btn2.join()
    claim_btn_1 = claim_btn_1.join()
    claim_btn = claim_btn_1 if exists(claim_btn_1) else claim_btn2

    if not exists(claim_btn): return
       
    moveAndClick(claim_btn)
    delay(2)
    openChest()
    delay(2)
    openChest()
    delay(2)
    closePopup()

def check_if_can_close_divine_offer():
    divine_close = getImagePositionRegion(APP_START_DIVINE_CLOSE, 1210, 80, 1290, 160, 0.8, 2)

    if exists(divine_close):
        moveAndClick(divine_close)