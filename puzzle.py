from move import moveAndClick, multiple_click, drag_to
from close import check_if_ok
from screen import Screen
from utils import delay, exists
from popup import Popup
from position_map import Position_Map


class Puzzle:
    pos = Screen.get_pos([0.4296875, 0.19537])
    claim_btn_pos = [1635, 340, 1840, 1206]

    @staticmethod
    def open_puzzle():
        if not exists(Position_Map.center_map()):
            return print('Puzzle action not in center.')
        multiple_click(Puzzle.pos, 10, 0.01)
        delay(1)

        if Puzzle._is_puzzle_island():
            Puzzle._claim_moves()
            Puzzle._move()
            delay(1)
        check_if_ok()

    @staticmethod
    def _is_puzzle_island():
        bbox = [0.028125, 0.883, 0.140625, 0.935185185]

        text_positions = Screen.get_text_pos(bbox)
        for t in text_positions:
            if Screen.is_match('NextRewards', t['text']): return True
        return False

    @staticmethod
    def _claim_moves():
        bbox = [0.6359375, 0.231481, 0.7072916, 0.8231481]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match('claim', t['text']):
                moveAndClick(t['position'])
                delay(1)

        if len(text_positions) > 0:
            check_if_ok()

    def _move():
        rows = 9
        cols = 9

        [x_start, y_start] = Screen.get_pos([0.32135416, 0.12315])
        [box_length, no_value] = Screen.get_pos([0.05104167, 1])
        drag_length = 250
        prev_moves = Puzzle._num_of_moves()

        if prev_moves < 1: return print('There are no moves left. Do not start the puzzle')

        for i in range(10):
            for row in range(rows):
                for col in range(cols):
                    pos = [x_start + (col * box_length), y_start + (row * box_length)]

                    if row != 0: drag_to(pos, [pos[0], pos[1] - drag_length]) # move up
                    if row != 8: drag_to(pos, [pos[0], pos[1] + drag_length]) # move down
                    if col != 8: drag_to(pos, [pos[0] + drag_length, pos[1]]) # move right

                    num_of_moves = Puzzle._num_of_moves()
                    if num_of_moves < 1:
                        check_if_ok()
                        return print('There are no moves left. Stop the Puzzle')
                    if num_of_moves != prev_moves:
                        prev_moves = num_of_moves
                        delay(2)
                        Popup.check_popup_chest()
                        moveAndClick(Popup._get_claim_btn(times=1), 'Checking for claim button in puzzle')
                        # TODO there is a close button that need to click when dragon is the reward.
                Popup.check_popup_chest()
                moveAndClick(Popup._get_claim_btn(times=1), 'Checking for claim button in puzzle')

    @staticmethod
    def _num_of_moves():
        bbox = [0.914583, 0.84074, 0.95677083, 0.884259259]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            return int(t['text'])
        return 0
