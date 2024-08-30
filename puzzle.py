from move import moveAndClick, multiple_click, center_map, moveTo, drag_to
from close import check_if_ok
from screen import Screen
from utils import delay
from popup import Popup
import time

class Puzzle:
    pos = [1150, 295]
    claim_btn_pos = [1635, 340, 1840, 1206]

    @staticmethod
    def open_puzzle():
        center_map()
        multiple_click(Puzzle.pos, 3, 0.01)
        delay(1)
        
        if Puzzle._is_puzzle_island():
            Puzzle._claim_moves()
            Puzzle._move()
        check_if_ok()

    @staticmethod
    def _is_puzzle_island():
        bbox = [79, 1284, 369, 1359]

        text_positions = Screen.get_text_pos(bbox)
        for t in text_positions:
            if 'NextRewards' in t['text']: return True
        return False

    @staticmethod
    def _claim_moves():
        bbox =[1647, 341, 1835, 1191]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
          if 'SKIP' not in t['text'] or 'CLAIM' in t['text']: 
            moveAndClick(t['position'])
            delay(1)
        check_if_ok()

    def _move():
        close_pos = [1976, 208]
        buy_moves_close_pos = [1982, 384]
        row = 10
        col = 9
       
        y_start = 180
        x_start = 760
        
        box_length = 130
        box_space = 10

        for i in range(2):
            for c in range(col):
                for r in range(1, row):
                    pos = [x_start + (r * box_length) - box_space, y_start + (c * box_length)]
                    drag_to(pos, [pos[0] - 250, pos[1]]) # move down
                    drag_to(pos, [pos[0] + 250, pos[1]]) # move up
                    drag_to(pos, [pos[0], pos[1] - 250]) # move left
                    drag_to(pos, [pos[0], pos[1] + 250]) # move right
                Popup.check_popup_chest()
                moveAndClick(close_pos)
                moveAndClick(buy_moves_close_pos)
    