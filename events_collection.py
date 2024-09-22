from utils import get_monitor_quarters, exists, delay
from move import moveAndClick
from popup import Popup
from close import check_if_ok
from screen import Screen

text = {
    'events': 'events',
    'collections': 'collections',
    'claimi': 'claimi',
}


class Events_Collection:
    _mon = get_monitor_quarters()
    first_event = Screen.get_pos([0.11875, 0.609259])
    forward = Screen.get_pos([0.6583, 0.07037])

    @staticmethod
    def collect_events():
        events_btn = Events_Collection._get_events_btn()

        if not exists(events_btn):
            return print('Events button not found')

        moveAndClick(events_btn)
        delay(1)

        events_collection = Events_Collection._get_events_collection()

        if not exists(events_collection): 
            return print('No event collection to click on')

        moveAndClick(events_collection)
        delay(1)
        moveAndClick(Events_Collection.first_event)
        delay(1)

        events_num = 10

        while events_num > 0:
            claim_btn = Events_Collection._get_claim_btn()

            if exists(claim_btn):
                moveAndClick(claim_btn)
                delay(1)
                Popup._enjoy()
                Popup.check_popup_chest()
            else:
                events_num -= 1
                moveAndClick(Events_Collection.forward)
            delay(.3)
        check_if_ok()

    @staticmethod
    def _get_claim_btn():
        bbox = [0.6677083, 0.85648148, 0.74635416, 0.9194]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claimi'], t['text']):
                return t['position']

        return [-1]

    @staticmethod
    def _get_events_collection():
        bbox = [0.6375, 0.15, 0.71875, 0.1935185]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['collections'], t['text']):
                return t['position']
        return [-1]

    @staticmethod
    def _get_events_btn():
        bbox = [0.921354167, 0.50648148, 0.98697916, 0.55185185]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['events'], t['text']):
                return t['position']
        return [-1]
