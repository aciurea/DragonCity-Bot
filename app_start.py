from constants import APP_START_CLAIM_BTN, APP_START_DIVINE_CLOSE, APP_START_RED_CLOSE
from utils import ( closePopup,
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

def get_close_btn():
    return getImagePositionRegion(APP_START_RED_CLOSE, 1430, 0, 1600, 140, 0.8, 2)

def close_calendar():
    closePopup()
    moveAndClick(get_close_btn(), 'No Daily close btn found')

def check_if_can_claim_daily():
    claim_btn = getImagePositionRegion(APP_START_CLAIM_BTN, 670, 710, 930, 795, 0.8, 2)

    if exists(claim_btn):
        print('The time has come to claim the daily reward')
        moveAndClick(claim_btn)
        delay(2)
        openChest()
        print('Open the first chest in daily reward')
        close_calendar()
        delay(2)
        openChest()
        delay(2)
        close_calendar()
    else: close_calendar()
  
def check_if_can_close_divine_offer():
    divine_close = getImagePositionRegion(APP_START_DIVINE_CLOSE, 1210, 80, 1290, 160, 0.8, 2)

    if exists(divine_close):
        moveAndClick(divine_close)