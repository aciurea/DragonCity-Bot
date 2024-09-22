from move import moveAndClick, multiple_click
from utils import exists
from timers import delay
from screen import Screen

text = {
    'tap': 'tap',
    'claim': 'claimi',
    'enjoy': 'enjoyi',
}


class Popup:
    @staticmethod
    def check_popup_chest():
        chest_pos = Popup._get_chest()

        if not exists(chest_pos): return
       
        multiple_click(chest_pos, 5, 0.01)
        delay(2)
        moveAndClick(Popup._get_claim_btn())
            
    @staticmethod
    def _get_chest():
        bbox = [0.40078125, 0.6451389, 0.4734375, 0.7548612]

        for t in Screen.get_text_pos(bbox):
            if Screen.is_match_with_one_difference(text['tap'], t['text']): return t['position']
        return [-1]

    @staticmethod
    def _get_claim_btn(times = 3):
        if times < 1:  return Screen.get_pos([0.487890625, 0.79723])# static pos
        bbox = [0.444140625, 0.754861, 0.550390625, 0.834]

        text_positions = Screen.get_text_pos(bbox, gray_mode=True)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claim'], t['text']): return t['position']
        delay(1)
        return Popup._get_claim_btn(times - 1)
    
    @staticmethod
    def _enjoy():
        bbox = [0.4578125, 0.8074074, 0.53854167, 0.8574074]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['enjoy'], t['text']):
                moveAndClick(t['position'])
                delay(1)
                Popup.check_popup_chest()
