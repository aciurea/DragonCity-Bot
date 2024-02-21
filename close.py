from screeninfo import get_monitors
from move import moveAndClick
from utils import delay, exists, get_int, get_monitor_quarters, getImagePositionRegion
import constants as C
import concurrent.futures

class Close:
    [res] = get_monitors()
    mon = get_monitor_quarters()

    @staticmethod
    def _close_user_settings():
        mon = get_monitor_quarters()
        (2247, 187)

        if exists(getImagePositionRegion(C.LOGOUT_POPUP, *mon['top_right'], .8, 1)):
            x = get_int(.877 * Close.res.width)
            y = get_int(.1168 * Close.res.height)
            return [x, y]
    
    @staticmethod
    def get_btn():
        # TODO check this if it has the right icons to click on 
        # VIP buttons
        # [C.GOALS_CLOSE_BTN, *mon['top_right'], .8, 1], search for goal close btn
        
        
        mon_quarters = get_monitor_quarters()
        top_right = mon_quarters['top_right']
        high_priority_btns = [
            [C.APP_CLOSE_DIVINE, *top_right],
            [C.APP_CLOSE_GEMS, *top_right],
            [C.APP_CLOSE_PIGGY, *top_right],
            [C.APP_CLOSE_SETTINGS, *top_right],
            [C.APP_CLOSE_TOWER, *top_right],
        ]
        lower_priority_btns = [[C.APP_CLOSE_OFFERS, *top_right]]
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for b in [high_priority_btns, lower_priority_btns]:
                result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), b)
                for close_btn in result_list:
                    if exists(close_btn): return close_btn
            return [-1]
        
    @staticmethod
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

            for btn in [*btns, Close._close_user_settings()]:
                if exists(btn):
                    moveAndClick(btn)
                    return btn

        if Close._is_enjoy_popup():
            Close._close_enjoy_popup()
            delay(.5)
            return Close.check_if_ok()
        
        if Close._is_piggy_popup():
            close_btn = [get_int(0.771153846 * Close.res.width), get_int(0.1475 * Close.res.height)] 
            moveAndClick(close_btn)

    @staticmethod
    def _close_enjoy_popup():
        [res] = get_monitors()
        pos = [get_int(0.4269230769 * res.width), get_int(0.775625 * res.height)]
        moveAndClick(pos)

    @staticmethod
    def _is_enjoy_popup():
        return exists(getImagePositionRegion(C.ENJOY_POPUP, *Close.mon['top_left'], .8, 1))
    
    def _is_piggy_popup():
        return exists(getImagePositionRegion(C.PIGGY_POPUP, *Close.mon['1stRow'], .8, 1))
             
def check_if_ok():
    return Close.check_if_ok()
