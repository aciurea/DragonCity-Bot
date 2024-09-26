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
        delay(3)

        retries = 10
        while retries > 0:
            retries -= 1
            work = Alliance._get_work()
            if work:
                check_if_ok()
                return work()
            claim = Alliance._get_claim_btn()
            if claim:
                moveAndClick(claim)
                delay(2)
                return Alliance._claim_alliance()

    @staticmethod
    def _get_work():
        bbox = [0.5265625, 0.7481481, 0.5854167, 0.787962962962963]
        work = {
            'Breed': lambda: Breed.breed('breed', 20),
        }
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if t['text'] in work:
                return work[t['text']]
        return None

    @staticmethod
    def _claim_alliance():
        Popup.check_popup_chest()
        delay(10)
        check_if_ok()

    @staticmethod
    def _alliance_filled():
        continue_btn = Alliance.get_continue_btn()
        if exists(continue_btn):
            moveAndClick(continue_btn)
            delay(1)
            check_if_ok()
            return

    def get_continue_btn():
        # TODO to be implemented when alliance ready.
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
