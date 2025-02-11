from pyautogui import scroll
from close import check_if_ok
from move import multiple_click, moveAndClick
from utils import delay
from position_map import Position_Map
from screen import Screen


class Shop:
    shop_pos = Screen.get_pos([0.9552083,  0.862037])
    orbs_pos = Screen.get_pos([0.49427083, 0.74])
    heroic_pos = Screen.get_pos([0.86, 0.471296])
    legendary_pos = Screen.get_pos([0.86,  0.82])

    def open_shop():
        actions = [
            Position_Map.center_map,
            lambda: delay(.5),
            lambda: moveAndClick(Shop.shop_pos),
            lambda: moveAndClick(Shop.orbs_pos),
            lambda: scroll(-10_000),
            lambda: delay(.5),
            lambda: multiple_click(Shop.heroic_pos, 7, 0.1),
            lambda: multiple_click(Shop.legendary_pos, 7, 0.1),
            check_if_ok,
        ]

        for action in actions:
            action()
            delay(.5)
