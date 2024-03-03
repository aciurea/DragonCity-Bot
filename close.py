from screeninfo import get_monitors
from move import moveAndClick
from utils import delay, exists, get_int, get_monitor_quarters, getImagePositionRegion
import constants as C
import concurrent.futures

class Close:
    [res] = get_monitors()
    mon_quarters = get_monitor_quarters()
    
    @staticmethod
    def get_btn():
        # TODO Close btn should be checked before last column, to check if there are popous
        # RED CLOSE ONLY. Make it separate like close empower 
        # First check if close exists on top right
        # in case it exists, check if exists before last column.
        # all the close buttons are on the second half width of the screen and 
        # in the first half of the height of the screen. 
        top_right = Close.mon_quarters['top_right']
        high_priority_btns = [
            [C.APP_CLOSE_DIVINE, *top_right],
            [C.APP_CLOSE_GEMS, *top_right],
            [C.APP_CLOSE_PIGGY, *top_right],
            [C.APP_CLOSE_SETTINGS, *top_right],
            [C.APP_CLOSE_TOWER, *top_right],
        ]
        lower_priority_btns = [[C.APP_CLOSE_OFFERS, *Close.mon_quarters['lastCol']]]
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for b in [high_priority_btns, lower_priority_btns]:
                result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), b)
                for close_btn in result_list:
                    if exists(close_btn): return close_btn
            return [-1]
    
    @staticmethod
    def close_empower():
        close_btn = getImagePositionRegion(C.APP_CLOSE_OFFERS, *Close.mon_quarters['lastCol'], .8, 1)

        if exists(close_btn):
            moveAndClick(close_btn)
            delay(1)
            loose_btn = getImagePositionRegion(C.APP_LOOSE, *Close.mon_quarters['bottom_left'])
            moveAndClick(loose_btn)
            return True
        return False
    
    @staticmethod
    def check_if_ok():
        if Close.close_empower(): return

        btn = Close.get_btn()
        if exists(btn):
            moveAndClick(btn)
            return btn

       # TODO check what enjoy popup is
        if Close._is_enjoy_popup():
            Close._close_enjoy_popup()
            delay(.5)
            return Close.check_if_ok()

    @staticmethod
    def _close_enjoy_popup():
        [res] = get_monitors()
        pos = [get_int(0.4269230769 * res.width), get_int(0.775625 * res.height)]
        moveAndClick(pos)

    @staticmethod
    def _is_enjoy_popup():
        return exists(getImagePositionRegion(C.ENJOY_POPUP, *Close.mon_quarters['top_left'], .8, 1))

def check_if_ok():
    return Close.check_if_ok()
