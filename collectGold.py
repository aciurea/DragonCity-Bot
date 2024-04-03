from close import check_if_ok
from move import multiple_click
from utils import  dragMapToCenter, get_json_file

jsonPos = get_json_file('collectGold.json')

class Gold:
    @staticmethod
    def collectGold():
        dragMapToCenter()
        multiple_click(jsonPos["STACKED_HABITTATS"], times=70, time_between_clicks=0.01)
        check_if_ok()

def collectGold():
    Gold.collectGold()
