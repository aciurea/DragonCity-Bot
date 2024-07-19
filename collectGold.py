from close import check_if_ok
from move import multiple_click
from utils import  dragMapToCenter, get_int

from screeninfo import get_monitors

res = get_monitors()[0]
jsonPos = { "STACKED_HABITTATS": [get_int(res.width * 0.2109375), get_int(res.height * 0.4027)] }

class Gold:
    @staticmethod
    def collectGold():
        dragMapToCenter()
        multiple_click(jsonPos["STACKED_HABITTATS"], times=70, time_between_clicks=0.01)
        check_if_ok()

def collectGold():
    Gold.collectGold()
