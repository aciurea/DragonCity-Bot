import keyboard

from move import moveAndClick, multiple_click
from utils import delay
from screen import Screen
from close import check_if_ok
from position_map import Position_Map


class Recall:
    tree_pos = [810, 300]
    recall_pos = [1530, 1280]
    search_box_pos = [620, 300]
    recall_dragon_pos = [1100, 620]
    yes_pos = [1065, 1130]

    @staticmethod
    def recall(dragon_name):
        actions = [
            Recall._go_to_tree,
            Recall._finish_recall,
            lambda: Recall._select_dragon_to_recall(dragon_name),
            Recall._recall_dragon
        ]

        for action in actions:
            try: action()
            except Exception as e: print('not ready', e)
        check_if_ok()


    @staticmethod
    def _go_to_tree():
        Position_Map.center_map()
        multiple_click(Recall.tree_pos, 3, 0.01)
        delay(1)
        moveAndClick(Recall.recall_pos)
        delay(1)

    @staticmethod
    def _finish_recall():
        bbox = [1775, 1240, 1980, 1340]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference('finish', t['text'].lower()):
                moveAndClick(t['position'])
                delay(7)

    @staticmethod
    def _select_dragon_to_recall(dragon_name):
        bbox = [1562, 629, 1713, 716]
        text_positions = Screen.get_text_pos(bbox)

        if len(text_positions) == 0: raise Exception('no dragon to recall')

        moveAndClick(Recall.search_box_pos)
        delay(.5)
        keyboard.write(dragon_name, delay=0.1)
        keyboard.press_and_release('enter')
        moveAndClick(Recall.recall_dragon_pos)
        delay(1)

    @staticmethod
    def _recall_dragon():
        bbox = [1562, 629, 1713, 716]
        text_positions = Screen.get_text_pos(bbox)

        if len(text_positions) > 0: return print('dragon was not selected')
        bbox = [1775, 1240, 1980, 1340]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if 'recall' in t['text'].lower():
                moveAndClick(t['position'])
                delay(.5)
                moveAndClick(Recall.yes_pos)
        check_if_ok()
