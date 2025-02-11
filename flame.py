import mouse

from move import moveAndClick, multiple_click
from hatch import Hatch
from utils import delay
from recall import Recall
from position_map import Position_Map

import constants as C


class Flame:
    shop_pos = [2461, 1260]
    dragons_pos = [480, 560]
    filter_gold_pos = [1600, 1300]
    flame_dragon_pos = [1600, 1080]
    sea_dragon_pos = [2266, 1087]

    @staticmethod
    def buy_dragon():
        actions = [
            Position_Map.center_map,
            lambda: multiple_click(mouse.get_position(), 3, .01),
            lambda: moveAndClick(Flame.shop_pos),
            lambda: moveAndClick(Flame.dragons_pos),
            lambda: moveAndClick(Flame.filter_gold_pos),
            lambda: moveAndClick(Flame.sea_dragon_pos)
        ]

        for action in actions:
            action()
            delay(.7)

    @staticmethod
    def hatch_dragon():
        Hatch.hatch_dragon_in_dragonarium(C.BREED_SEA_EGG)

    @staticmethod
    def flame_dragon(times=200):
        if times == 0: return

        Recall.recall('Sea')

        Flame.hatch_dragon()
        Flame.hatch_dragon()

        Recall.recall('Sea')

        Flame.buy_dragon()
        Flame.buy_dragon()

        Flame.flame_dragon(times - 1)
