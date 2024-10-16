from close import check_if_ok
from move import multiple_click
from position_map import Position_Map
from utils import exists
from screen import Screen


class Gold:
    stacked_habitats_pos = Screen.get_pos([0.19947916, 0.3851851])

    @staticmethod
    def collectGold():
        if exists(Position_Map.center_map()):
            multiple_click(Gold.stacked_habitats_pos, 70, 0.01)
            check_if_ok()
