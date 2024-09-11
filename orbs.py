from close import check_if_ok
from move import moveAndClick, multiple_click
from utils import delay, exists, get_monitor_quarters, getImagePositionRegion, get_int
from position_map import Position_Map
from screen import Screen

class Orbs:
    habitat_pos = [get_int(0.2828125 * Screen.width), get_int(0.4368056 * Screen.height)]
    
    def collect_orbs():
        Position_Map.center_map()
        multiple_click(Orbs.habitat_pos, times=10, time_between_clicks=0.01)
        bbox = [0.62109375, 0.82083, 0.707421875, 0.867361]
        text_positions = Screen.get_text_pos(bbox)
        
        print(text_positions)

        for t in text_positions:
            if Screen.is_match_with_one_difference('claimi', t['text'].lower()):
                moveAndClick(t['position'])
        delay(1)
        check_if_ok()