from screeninfo import get_monitors
from move import moveAndClick
from utils import exists, get_int, get_monitor_quarters, getImagePositionRegion
import constants as C
import concurrent.futures

def _close_user_settings():
    mon = get_monitor_quarters()
    (2247, 187)
    [res] = get_monitors()

    if exists(getImagePositionRegion(C.LOGOUT_POPUP, *mon['top_right'], .8, 1)):
        x = get_int(.877 * res.width)
        y = get_int(.1168 * res.height)
        return [x, y]
    
def check_if_ok():
    mon = get_monitor_quarters()
    btns_pos = [
        [C.DIVINE_PASS_CLOSE_BTN, *mon['top_right'], .8, 1],
        ['./img/app_start/back.png', *mon['top_left'], .8, 1],
        [C.HALLOW_CLOSE_BTN, *mon['top_right'], .8, 1],
        [C.SETTINGS_CLOSE_BTN, *mon['top_right'], .8, 1],
        [C.BIG_CLOSE_BTN, *mon['top_right'], .8, 1],
        [C.BIG_CLOSE_BTN, *mon['top_right'], .8, 1],
        [C.GOALS_CLOSE_BTN, *mon['top_right'], .8, 1],
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        btns = executor.map(lambda args: getImagePositionRegion(*args), btns_pos)

        for btn in [*btns, _close_user_settings()]:
            if exists(btn):
                print('Close btn at pos ', btn)
                return moveAndClick(btn)
                
             
