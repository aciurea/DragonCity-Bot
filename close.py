from screeninfo import get_monitors
from move import moveAndClick, moveTo
from screen import Screen
from utils import delay, exists, get_grid_monitor, get_int, get_monitor_quarters, getImagePositionRegion, get_screen_resolution
import constants as C
import concurrent.futures
import time

class Close:
    
    @staticmethod
    def check_if_ok():
        btns = Close._get_btn()

        for btn in btns:
            moveAndClick(btn)
            delay(.5)
        
        return btns

    @staticmethod
    def get_lose_text():
        lose_pos = [0.344140625, 0.667361, 0.397265625, 0.725]
        text_positions = Screen.get_text_pos(lose_pos)

        for t in text_positions:
            if Screen.is_match_with_one_difference('lose', t['text']):  moveAndClick(t['position'])
    
    @staticmethod
    def _get_btn():
        grid = get_monitor_quarters()
        screen_pos = get_screen_resolution()
        base = './img/wrong_popups'

        paths = [
            f'{base}/{screen_pos}_right_corner.png',
            f'{base}/{screen_pos}_red_close.png',
            f'{base}/{screen_pos}_goals.png',
            f'{base}/{screen_pos}_settings_close.png',
            f'{base}/{screen_pos}_piggy.png',
        ]

        btns = []
        st = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(args, *grid['top_right'], .8, 1), paths)
            for close_btn in result_list:
                if exists(close_btn): btns.append(close_btn)
        print('Time to find button with Thread', btns, time.time() - st)
        
        btns = sorted(btns, key=lambda x: x[0])
        if len(btns) > 1: return Close._filter_corrupted_imgs(btns)
        return btns
    
    @staticmethod
    def _filter_corrupted_imgs(imgs):
        img_distance_threshold = 10
        filtered_data = [imgs[0]]

        for item in imgs[1:]:
            if(abs(item[0] - filtered_data[-1][0]) > img_distance_threshold):
                filtered_data.append(item)
        return filtered_data

def check_if_ok():
    return Close.check_if_ok()
