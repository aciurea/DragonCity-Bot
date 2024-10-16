from screen import Screen
from close import check_if_ok
from move import moveAndClick, multiple_click
from position_map import Position_Map
from utils import delay


class ClearEvent:
    skip_bbox = [0.435546875, 0.91, 0.56640625, 0.961805]
    top_pos = Screen.get_pos([0.4296875, 0.19537])
    center_pos = Screen.get_pos([0.5625, 0.3435185])

    @staticmethod
    def skip_event():
        positions = [
            ClearEvent.top_pos,
            ClearEvent.center_pos,
        ]

        for pos in positions:
            if not Position_Map.center_map():
                return print('ClearEvent action not in center.')
            multiple_click(pos, 5, 0.01)
            delay(10)
            text_positions = Screen.get_text_pos(ClearEvent.skip_bbox)

            # TODO if clicked, store the item in .txt file and read the duration of event from current date
            # TODO when multiple click on position if the name of the event matches with the one saved, 
            # TODO return immediatelly

            for t in text_positions:
                if Screen.is_match('SkipTutorial', t['text']):
                    moveAndClick(t['center'])
            delay(.5)
            check_if_ok()
            delay(2)
