import constants as C
import random

from close import check_if_ok
from position_map import Position_Map
from utils import delay, get_monitor_quarters, get_int, getImagePositionRegion, exists
from move import moveAndClick, multiple_click, moveTo

from screeninfo import get_monitors

class Wizard:
    _mon_quarters = get_monitor_quarters()
    res = get_monitors()[0]
    _quit_pos = [get_int(0.30585 * res.width), get_int(0.81 * res.height)]
    wizard_static_pos = [get_int(res.width * .82929) , get_int(res.height * .334027)]

    @staticmethod
    def open_wizard():
        Position_Map.drag_map_to_the_bottom()
        delay(1)
        moveAndClick(Wizard.wizard_static_pos)
        delay(1)
        play_btn = Wizard._get_play_btn()

        if not exists(play_btn): return print('Wizard Play button not found')
        moveAndClick(play_btn)
        delay(10)
        Wizard._play_wizard()
    
    @staticmethod
    def _play_wizard():
        times = 5
    
        balls = [[842, 665],
                [1126, 777],
                [1470, 781],
                [1737, 646]
        ]
        
        while times >= 0:
            if exists(Wizard._get_wizard_gem()):
                check_if_ok()
                delay(1)
                moveAndClick(Wizard._quit_pos)
                return
            times -= 1
            ball = random.choice(balls)
            multiple_click(ball)

        # TODO claim the current rewards if any
                
    @staticmethod
    def _get_wizard_gem():
        return getImagePositionRegion(C.WIZARD_GEMS_BTN, *Wizard._mon_quarters['2ndHorHalf'], .8, 2)
    
    @staticmethod
    def _get_play_btn():
        return getImagePositionRegion(C.WIZARD_PLAY_BTN, *Wizard._mon_quarters['2ndHorHalf'], .8, 2)