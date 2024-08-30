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
            delay(1)
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
        bbox = [1647, 341, 1835, 1191]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
          if 'skip' not in t['text'].lower() or 'claim' in t['text'].lower(): 
            moveAndClick(t['position'])
            delay(1)
        check_if_ok()

    def _move():
        close_pos = [1976, 208]
        buy_moves_close_pos = [1982, 384]
        rows = 9
        cols = 9
       
        y_start = 175
        x_start = 825
        box_length = 135

        for i in range(2):
            for row in range(rows):
                for col in range(cols):
                    pos = [x_start + (col * box_length), y_start + (row * box_length)]
                    
                    if row != 0: drag_to(pos, [pos[0], pos[1] - 250]) # move up
                    if row != 8: drag_to(pos, [pos[0], pos[1] + 250]) # move down
                    if col != 8: drag_to(pos, [pos[0] + 250, pos[1]]) # move right
                    
                    if Puzzle._no_moves():
                        moveAndClick(buy_moves_close_pos)
                        check_if_ok()
                        return print('There are no moves left. Stop the Puzzle')
                Popup.check_popup_chest()
                moveAndClick(close_pos)
                moveAndClick(buy_moves_close_pos)
    
    @staticmethod
    def _no_moves():
        st = time.time()
        bbox = [1300, 315, 1545, 395]
        text_positions = Screen.get_text_pos(bbox)

        return len(text_positions) > 0
