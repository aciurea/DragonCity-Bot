from screeninfo import get_monitors
from move import moveAndClick, moveTo
from utils import delay, exists, get_grid_monitor, get_int, get_monitor_quarters, getImagePositionRegion
import constants as C
import concurrent.futures

class Close:
    [res] = get_monitors()
    mon_quarters = get_monitor_quarters()
    grid = get_grid_monitor()
    
    def get_popup_red_btn():
        last_col = Close.mon_quarters['lastCol']
        top_right = Close.mon_quarters['top_right']
        top_right[2] = last_col[0]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), [[C.APP_CLOSE_TOWER, *top_right], [C.APP_CLOSE_ANOTHER_RED, *top_right]])
            for btn in result_list:
                if exists(btn): return btn
        return [-1]

    def get_red_btn():
        last_col = Close.mon_quarters['lastCol']
        big_red_btn = getImagePositionRegion(C.APP_CLOSE_OFFERS, *last_col, .8, 1)

        if exists(big_red_btn):
            red_btn = Close.get_popup_red_btn()
            if exists(red_btn): return red_btn
        
        red_btn = Close.get_popup_red_btn()
        return exists(red_btn) and red_btn or big_red_btn

    @staticmethod
    def get_btn():
        g = Close.grid
        red_btn = Close.get_red_btn()
        if exists(red_btn): return red_btn

        top_right = Close.mon_quarters['top_right']
        high_priority_btns = [
            [C.APP_CLOSE_DIVINE, *top_right],
            [C.APP_CLOSE_GEMS, *top_right],
            [C.APP_CLOSE_PIGGY, *[g['x5'], g['y0'], g['x7'], g['y2']]],
            [C.APP_CLOSE_SETTINGS, *[g['x6'], g['y0'], g['x7'], g['y1']]],
            [C.APP_CLOSE_BACK, *[g['x0'], g['y0'], g['x1'], g['y1']]],
        ]
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), high_priority_btns)
            for close_btn in result_list:
                if exists(close_btn): return close_btn
            return [-1]
    
    @staticmethod
    def close_empower():
        loose_btn = getImagePositionRegion(C.APP_LOOSE, *Close.mon_quarters['bottom_left'])
        if exists(loose_btn):
            moveAndClick(loose_btn)
    
    @staticmethod
    def check_if_ok():
        btn = Close.get_btn()
        if exists(btn):
            moveAndClick(btn)
            Close.close_empower()
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
