from screen import Screen
from close import check_if_ok
from move import moveAndClick, center_map, multiple_click
from utils import delay

class ClearEvent:
    skip_bbox = [0.435546875, 0.91,  0.56640625, 0.961805]
    top_pos = [1150, 295]
    center_pos = [1457, 548]

    @staticmethod
    def skip_event():
        actions = [
            ClearEvent.top_pos,
            ClearEvent.center_pos,
        ]

        for action in actions:
            center_map()
            multiple_click(action, 5, 0.01)
            delay(1)
            text_positions = Screen.get_text_pos(ClearEvent.skip_bbox)

            for t in text_positions:
                if Screen.is_match_with_one_difference('skip', t['text'].lower()):
                    moveAndClick(Screen.get_center_of_image(ClearEvent.skip_bbox))
                elif Screen.is_match_with_one_difference('tutorial', t['text'].lower()):
                    moveAndClick(Screen.get_center_of_image(ClearEvent.skip_bbox))
            delay(.5)
            check_if_ok()
