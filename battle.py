import random
import time

from screeninfo import get_monitors
from popup import Popup
from utils import (
                _get_int,
                delay,
                exists,
                get_json_file,
                get_monitor_quarters,
                getImagePositionRegion,
                is_in_time,
                moveAndClick)
import constants as C
import concurrent.futures


jsonPos = get_json_file('arena.json')

class Battle:
    mon_quarters = get_monitor_quarters()
    [ res ] = get_monitors()
    one_third = _get_int(res.width / 3)
    
    @staticmethod
    def is_fight_in_progress():
        if exists(getImagePositionRegion(C.FIGHT_IN_PROGRESS, *Popup.mon_quarters['1stCol'], .8, 1)):
            return True

        return exists(Battle.get_new_dragon_btn())

    @staticmethod
    def get_play_button():
        return getImagePositionRegion(C.FIGHT_PLAY, *Popup.mon_quarters['1stCol'], .8, 1)
    
    @staticmethod
    def get_new_dragon_btn():
        lst = []
        pos = Battle.mon_quarters['4thRow']
        second = pos[:]
        second[0] = Battle.one_third
        third =  pos[:]
        third[0] = Battle.one_third * 2

        btns = [
            [C.FIGHT_SELECT_DRAGON, *pos],
            [C.FIGHT_SELECT_DRAGON, *second], # start from 1 third.
            [C.FIGHT_SELECT_DRAGON, *third], # start from 2nd third.
        ]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 6), btns)
            lst = [btn for btn in result_list if exists(btn)]

        if lst:
            return random.choice(lst)

        return [-1]
    
    @staticmethod
    def get_swap_button():
        return getImagePositionRegion(C.FIGHT_SWAP, *Battle.mon_quarters['bottom_left'], .8, 1)

    @staticmethod
    def wait_for_oponent_to_attack():
        start = time.time()
      
        while time.time() - start < 7:  # wait for 7 seconds for opponent to finish attack: (avoid infinite loop, app crashed or wrong flow/popup/app freeze)
            if exists(Battle.get_swap_button()): return # oponend finished attacking
            if exists(Battle.get_new_dragon_btn()): return # dragon is defetead.
            delay(1)
    
    @staticmethod
    def change_dragon():
        swap_btn = Battle.get_swap_button()
        if exists(swap_btn):
            moveAndClick(swap_btn)
            delay(1)

        new_dragon = Battle.get_new_dragon_btn()
        if not exists(new_dragon): return print('Dragon not found')

        moveAndClick(new_dragon)
        print('Dragon was changed')

    @staticmethod
    def fight():
        start = time.time()
        is_last_dragon = False
        delay(3)

        while is_in_time(start, limit=180) < 180: # 3 minutes is more than enough
            if not Battle.is_fight_in_progress(): return 
            if is_last_dragon: # to not try to change it, just continue checking if fight is in progress until it ends
                delay(2)
                continue 

            # This flow is specifically for arena where you want to use all the dragons power and not wait for a dragon to get defeated in order to change it.
            # This flow might save the dragon for a next fight.
            # Arena battles have very strong dragons.
            attacks_per_dragon = 3
            while attacks_per_dragon > 0:
                if not Battle.is_fight_in_progress(): return 
                attacks_per_dragon -= 1

                # dragon is defetead
                if exists(Battle.get_new_dragon_btn()):
                    print('Dragon is defeated')
                    break

                # dragon is the last one
                if not exists(Battle.get_swap_button()):
                    is_last_dragon = True
                    print('Dragon is the last one')
                    break # exit the loop since is the last dragon and no need for play and pause

                play = Battle.get_play_button()
                moveAndClick(play)
                delay(.5)
                moveAndClick(play) # pause

                Battle.wait_for_oponent_to_attack()

            if is_last_dragon:
                play_btn = Battle.get_play_button()
                if exists(play_btn): moveAndClick(play_btn)
                # Try again to find the select btn
                else:
                    select_btn = Battle.get_new_dragon_btn()
                    if not exists(select_btn): raise 'Select button not found! Exit'
                    moveAndClick(select_btn)
                    delay(2)
                    moveAndClick(Battle.get_play_button())
            else:
                Battle.change_dragon()
        print('Fight is over!')
