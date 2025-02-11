from close import check_if_ok
from move import moveAndClick, multiple_click
from utils import delay
from position_map import Position_Map
from screen import Screen

text = {
    'claim': 'claimi',
}


class Orbs:
    habitat_pos = Screen.get_pos([0.2828125, 0.4368056])

    def collect_orbs():
        Position_Map.center_map()

        multiple_click(Orbs.habitat_pos, times=10, time_between_clicks=0.1)
        bbox = [0.62109375, 0.82083, 0.707421875, 0.867361]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claim'], t['text']):
                moveAndClick(t['position'])
        delay(1)
        check_if_ok()
