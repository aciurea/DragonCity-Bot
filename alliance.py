from breed import Breed
from close import check_if_ok
from move import moveAndClick, multiple_click
from popup import Popup
from utils import delay, exists
from position_map import Position_Map
from screen import Screen

text = {
    'claim': 'claim',
    'new': 'new',
    'taptocontinue': 'taptocontinue',
}


class Alliance:
    alliance_pos = Screen.get_pos([0.3921875, 0.1712962])

    @staticmethod
    def open_alliance():
        if not exists(Position_Map.center_map()): return

        multiple_click(Alliance.alliance_pos, 3)
        delay(1)
        if Alliance._alliance_finished():
            print('Aliance finished!')
            return check_if_ok()
        delay(5)

        retries = 10
        while retries > 0:
            retries -= 1
            # check first the continue button. Any work will still be visible but there is no need to do work.
            continue_btn = Alliance.get_continue_btn()
            if continue_btn:
                moveAndClick(continue_btn)
                delay(1)
                check_if_ok()
                return
            work = Alliance._get_work()
            if work:
                check_if_ok()
                return work()
            claim = Alliance._get_claim_btn()
            if claim:
                moveAndClick(claim)
                delay(2)
                return Alliance._claim_alliance()
        check_if_ok()

    @staticmethod
    def _get_work():
        bbox = [0.509375, 0.69, 0.6083, 0.788]
        work = {
            'Breed': lambda: Breed.breed('breed', 10),
            'HatchEggs': lambda: Breed.breed('sell', 10),
        }
        text_positions = Screen.get_text_pos(bbox)
        print(text_positions)
        for t in text_positions:
            if t['text'] in work:
                return work[t['text']]
        return None

    @staticmethod
    def _claim_alliance():
        Popup.check_popup_chest()
        delay(10)
        check_if_ok()

    def get_continue_btn():
        bbox = [0.43125, 0.7861, 0.56, 0.83981]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match(text['taptocontinue'], t['text']):
                return t['position']
        return None

    def _get_claim_btn():
        bbox = [0.46614583, 0.84537, 0.52760416, 0.8925926]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match(text['claim'], t['text']):
                return t['position']
        return None

    @staticmethod
    def _alliance_finished():
        bbox = [0.50989583, 0.6842592, 0.564583, 0.7416]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match(text['new'], t['text']):
                return True
        return False
