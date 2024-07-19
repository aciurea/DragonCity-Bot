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

        if not exists(play_btn):
            check_if_ok()
            return print('Wizard Already played')

        moveAndClick(play_btn)
        delay(10)
        Wizard._play_wizard()
        check_if_ok()
    
    @staticmethod
    def _play_wizard():
        times = 2
    
        balls = [[842, 665],
                [1126, 777],
                [1470, 781],
                [1737, 646]
        ]
        
        while times >= 0:
            if not exists(Wizard._get_claim_btn()):
                check_if_ok()
                delay(1)
                moveAndClick(Wizard._quit_pos)
                return
            
            times -= 1
            ball = random.choice(balls)
            multiple_click(ball)
            delay(2)
            
            claim_btn = Wizard._get_claim_btn()
            
            if not exists(claim_btn):
                check_if_ok()
            
            moveAndClick(claim_btn)
            delay(1)
            claim_and_quit = Wizard._get_claim_and_quit()
            
            if not exists(claim_and_quit):
                moveAndClick([955, 1181])
                
            moveAndClick(Wizard._get_claim_and_quit())
            claim_all = Wizard._get_claim_all_btn()
            
            if not exists(claim_all):
                moveAndClick([1150, 1129])
            moveAndClick(claim_all)
        
    @staticmethod
    def _get_claim_all_btn():
        return getImagePositionRegion(C.WIZARD_YELLOW_CLAIM, *Wizard._mon_quarters['4thRow'], .8, 2)
    
    @staticmethod
    def _get_claim_and_quit():
        return getImagePositionRegion(C.WIZARD_RED_CLAIM, *Wizard._mon_quarters['4thRow'], .8, 2)
        
    @staticmethod
    def _get_claim_btn():
        return getImagePositionRegion(C.WIZARD_CLAIM_BTN, *Wizard._mon_quarters['4thRow'], .8, 2)
            
    # @staticmethod
    # def _get_wizard_gem():
    #     return getImagePositionRegion(C.WIZARD_GEMS_BTN, *Wizard._mon_quarters['2ndHorHalf'], .8, 2)
    
    @staticmethod
    def _get_play_btn():
        return getImagePositionRegion(C.WIZARD_PLAY_BTN, *Wizard._mon_quarters['2ndHorHalf'], .8, 2)