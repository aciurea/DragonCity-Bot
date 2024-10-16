from close import check_if_ok
from popup import Popup
from utils import delay
from move import moveAndClick
from screen import Screen
from position_map import Position_Map


class Daily_Treasure:
    treasure_pos = Screen.get_pos([0.8614583, 0.86574])
    chest_pos = Screen.get_pos([0.1135416, 0.84])

    @staticmethod
    def collect_daily_treasure():
        actions = [
            Position_Map.center_map,
            lambda: delay(.5),
            lambda: moveAndClick(Daily_Treasure.treasure_pos),
            lambda: moveAndClick(Daily_Treasure.chest_pos),
            Popup.check_popup_chest,
            check_if_ok,
        ]

        for action in actions:
            action()
            delay(.5)
