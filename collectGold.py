from close import check_if_ok
from move import fast_click
from timers import delay
from utils import  dragMapToCenter, get_json_file

jsonPos = get_json_file('collectGold.json')

class Gold:
    @staticmethod
    def collectGold():
        dragMapToCenter()
        times = 50
        while times > 0:
            fast_click(jsonPos["STACKED_HABITTATS"])
            times -= 1
            delay(.2)
        check_if_ok()

def collectGold():
    Gold.collectGold()
