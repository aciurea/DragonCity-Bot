from close import check_if_ok
from move import moveAndClick
from popup import Popup
from utils import delay, dragMapToCenter

class Daily_Treasure:
    def collect_daily_treasure():
        print('Collecting daily treasure')
        center = dragMapToCenter()
        moveAndClick(center)
        treasure_pos = [2245, 1275]
        delay(1)
        moveAndClick(treasure_pos)
        delay(2)
        moveAndClick([290, 1200])
        delay(1)
        Popup.check_popup_chest()
        check_if_ok()

def collect_daily_treasure():
    Daily_Treasure.collect_daily_treasure()