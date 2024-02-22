from close import check_if_ok
from move import fast_click, moveAndClick
from timers import delay
from utils import  dragMapToCenter, exists, get_int, get_json_file, getImagePositionRegion
import constants as C

jsonPos = get_json_file('collectGold.json')

class Gold:
    @staticmethod
    def collectGold():
        dragMapToCenter()
        times = 70
        while times > 0:
            fast_click(jsonPos["STACKED_HABITTATS"])
            times -= 1
            delay(.2)
        check_if_ok()

Gold.collectGold()