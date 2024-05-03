from datetime import datetime
import time
from screeninfo import get_monitors
from breed import Breed
from close import check_if_ok
from move import center_map, drag_map_to_the_bottom, moveAndClick, multiple_click
from popup import Popup
from utils import delay, exists, get_monitor_quarters, getImagePositionRegion
import constants as C


class Alliance:
    _width = 38.1640625 / 100
    _height = 33.33 / 100
    [res] = get_monitors()
    alliance_pos = [_width * res.width, _height * res.height]
    alliances_work = [
       { "start":'2024-05-03 19:00:00', "end": '2024-05-06 19:00:00', "work": lambda: Breed.breed('hatch', 30) },
       { "start":'2024-05-07 19:00:00', "end": '2024-05-09 19:00:00', "work": lambda: print('nothing to do on alliance. Is Arena time') },
       { "start":'2024-05-10 19:00:00', "end": '2024-05-13 19:00:00', "work": lambda: Breed.breed('breed', 30) },
       { "start": '2024-05-14 19:00:00', "end": '2024-05-17 19:00:00', "work": lambda: print('nothing to do on alliance. Is League time') },
       { "start": '2024-05-18 19:00:00', "end": '2024-05-20 19:00:00', "work": lambda: Breed.breed('breed', 30)  },
       { "start": '2024-05-30 19:00:00', "end": '2024-05-02 19:00:00', "work": lambda: Breed.breed('breed', 30) },
    ]

    def get_work():
        current_date = datetime.now()
        print(current_date)

        for alliance in Alliance.alliances_work:
            start = datetime.strptime(alliance['start'], '%Y-%m-%d %H:%M:%S')
            end = datetime.strptime(alliance['end'], '%Y-%m-%d %H:%M:%S')
            if start < current_date < end: return alliance['work']
        return lambda: print('nothing to do on alliance. Is rest time')

    def get_continue_btn():
        return getImagePositionRegion(C.ALLIANCE_CONTINUE, *get_monitor_quarters()['2ndHorHalf'], .8, 2)
    
    def get_claim_btn():
        return getImagePositionRegion(C.ALLIANCE_CLAIM, *get_monitor_quarters()['4thRow'], .8, 2)
    
    def open_alliance():
        center_map()
        drag_map_to_the_bottom()
        multiple_click(Alliance.alliance_pos, 3)
        delay(10)
        moveAndClick(Alliance.get_continue_btn())
        delay(.5)
        claim_btn = Alliance.get_claim_btn()
        if exists(claim_btn):
            moveAndClick(Alliance.get_claim_btn())
            delay(1)
            Popup.check_popup_chest()
            delay(10)
        check_if_ok()
        Alliance.last_time_started = time.time()
        Alliance.get_work()()
