import time
from close import check_if_ok
from move import center_map, moveAndClick
from popup import Popup
from utils import delay

class Daily_Treasure:
    wait_time = 3600 * 3
    last_time_started = 0

    def collect_daily_treasure():
        if time.time() - Daily_Treasure.last_time_started < Daily_Treasure.wait_time: return
        print('Collecting daily treasure')
        center = center_map()
        moveAndClick(center)
        treasure_pos = [2245, 1275]
        delay(1)
        moveAndClick(treasure_pos)
        delay(2)
        moveAndClick([290, 1200])
        delay(1)
        Popup.check_popup_chest()
        check_if_ok()
        Daily_Treasure.last_time_started = time.time()

def collect_daily_treasure():
    Daily_Treasure.collect_daily_treasure()
