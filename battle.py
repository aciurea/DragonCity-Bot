import time
from popup import Popup
from utils import (
                delay,
                exists,
                get_json_file,
                get_monitor_quarters,
                getImagePositionRegion,
                moveAndClick)
import constants as C
import concurrent.futures


jsonPos = get_json_file('arena.json')

class Battle:
    mon_quarters = get_monitor_quarters()
    
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
        btns = [
            [C.FIGHT_SELECT_DRAGON, *Battle.mon_quarters['2ndHorHalf']],
            [C.ARENA_SELECT_DRAGON, *Battle.mon_quarters['2ndHorHalf']]
        ]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), btns)
            for btn in result_list:
                if exists(btn):
                    return btn
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
        while Battle.is_fight_in_progress() and (time.time() - start) < 180: # minutes is more than enough
            if is_last_dragon: # to not try to change it, just continue checking if fight is in progress until it ends
                delay(2)
                continue 

            # This flow is specifically for arena where you want to use all the dragons power and not wait for a dragon to get defeated in order to change it.
            # This flow might save the dragon for a next fight.
            # Arena battles have very strong dragons.
            attacks_per_dragon = 3
            while attacks_per_dragon > 0:
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

                # attack is ok, play and pause
                play = Battle.get_play_button()
                moveAndClick(play)
                delay(.5)
                moveAndClick(play) # pause

                # wait for opponent to attack
                Battle.wait_for_oponent_to_attack()

            # check if is last dragon and just hit the play button
            if is_last_dragon: 
                moveAndClick(Battle.get_play_button())
            else:
                Battle.change_dragon()
        print('Fight is over!')
