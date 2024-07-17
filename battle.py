import random
import time
import pyautogui as pyt

from screeninfo import get_monitors
from utils import (
                _get_int,
                delay,
                exists,
                get_grid_monitor,
                get_monitor_quarters,
                getImagePositionRegion,
                is_in_time,
                moveAndClick)
import constants as C
import concurrent.futures
from close import check_if_ok


class Battle:
    grid = get_grid_monitor()
    mon_quarters = get_monitor_quarters()
    res = get_monitors()[0]
    one_third = _get_int(res.width / 3)
    
    def get_speed_btn():
        grid = Battle.grid
        position = [grid['x0'], grid['y1'], grid['x1'], grid['y2']]

        return getImagePositionRegion(C.FIGHT_X3, *position, .8, 1)
    
    def get_select_btn():
        grid = Battle.grid
        position = [grid['x0'], grid['y4'], grid['x8'], grid['y6']]

        return getImagePositionRegion(C.FIGHT_SELECT_DRAGON, *position, .8, 1)        

    def get_play_button():
        grid = Battle.grid
        position = [grid['x0'], grid['y0'], grid['x1'], grid['y2']]

        return getImagePositionRegion(C.FIGHT_PLAY, *position, .8, 1)
    
    def _get_attack_ready():
        grid = Battle.grid
        position = [grid['x6'], grid['y5'], grid['x8'], grid['y6']]

        return getImagePositionRegion(C.FIGHT_ATTACK_READY, *position, .8, 1)
    
    def get_no_btn():
        return getImagePositionRegion(C.ARENA_NO, *Battle.mon_quarters['full'], .8, 1) # TODO update it with grid to be faster 
    
    def is_in_battle():
        work = [Battle.get_play_button, Battle.get_speed_btn, Battle.get_select_btn]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            btns = executor.map(lambda func: func(), work)
            for btn in btns:
                if exists(btn): return True
        return False
    
    def wait_for_battle_to_start():
        start = time.time()
        time_limit = 15
        while time.time() - start < time_limit:
            if Battle.is_in_battle(): return print('Ready for fighting')
            else: print('Fight not ready')
            delay(1)
        raise Exception('Time limit exceded on arena. Closing the app....')
        
    @staticmethod
    def get_new_dragon_btn():
        grid = Battle.grid
        y0 = grid['y4']
        y1 = grid['y6']
        pos = [
                [grid['x0'], y0, grid['x2'], y1], 
                [grid['x3'], y0, grid['x4'], y1],
                [grid['x5'], y0, grid['x7'], y1]
            ]

        btns = [
            [C.FIGHT_SELECT_DRAGON, *pos[0]],
            [C.FIGHT_SELECT_DRAGON, *pos[1]], # start from 1 third.
            [C.FIGHT_SELECT_DRAGON, *pos[2]], # start from 2nd third.
        ]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), btns)
            lst = [btn for btn in result_list if exists(btn)]

        return random.choice(lst) if lst else [-1]
    
    @staticmethod
    def get_swap_button():
        grid = Battle.grid
        pos = [grid['x0'], grid['y4'], grid['x1'], grid['y5']]

        return getImagePositionRegion(C.FIGHT_SWAP, *pos, .8, 1)

    @staticmethod
    def wait_for_oponent_to_attack():
        start = time.time()
        work = [Battle._get_attack_ready, Battle.get_select_btn]
        while time.time() - start < 10:  # wait for 10 seconds for opponent to finish attack: (avoid infinite loop, app crashed or wrong flow/popup/app freeze)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                btns = executor.map(lambda func: func(), work)
                for btn in btns:
                    if exists(btn): return
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

    def _battle_with_no_change_dragon():
        start = time.time()
        moveAndClick(Battle.get_play_button())
        while is_in_time(start, limit = 120):
            if not Battle.is_in_battle(): return 
            delay(3)

    @staticmethod
    def fight(change_dragon=True):
        Battle._save_oponent_dragon()
        Battle.wait_for_battle_to_start()

        if not change_dragon: return Battle._battle_with_no_change_dragon()
        start = time.time()
        is_last_dragon = False
        first_time_checking_oponent = True
        
        while is_in_time(start, limit = 300): # 3 minutes is more than enough
            if not Battle.is_in_battle(): return 
            if is_last_dragon: # do not try to change it, just continue checking if fight is in progress until it ends
                delay(2)
                continue 
            attacks_per_dragon = 3
            while attacks_per_dragon > 0:
                attacks_per_dragon -= 1
                if not Battle.is_in_battle(): 
                    print('Not in battle....')
                    return 
                Battle.wait_for_oponent_to_attack()

                # dragon is defetead
                if exists(Battle.get_select_btn()): break
                # dragon is the last one
                if not exists(Battle.get_swap_button()):
                    is_last_dragon = True
                    print('Dragon is the last one')
                    no = Battle.get_no_btn()
                    if exists(no): moveAndClick(no)
                    break # exit the loop since is the last dragon and no need for play and pause

                play = Battle.get_play_button()
                
                # try to select dragon with double damage
                if first_time_checking_oponent == True or Battle._is_openent_dragon_defeated():
                    Battle._check_and_select_dragon_with_double_damage()
                    first_time_checking_oponent = False
                
                moveAndClick(play)
                delay(.25)
                moveAndClick(play) # pause
                delay(1.5)

            if is_last_dragon:
                play_btn = Battle.get_play_button()
                if exists(play_btn): moveAndClick(play_btn)
                else: 
                    if not Battle.is_in_battle(): return print('Dragon was the last one but I am not in the battle anymore!')
                    raise Exception('Dragon is the last one but couldnt continue the battle.')
            else:
                Battle.wait_for_oponent_to_attack()
                Battle.change_dragon()
        
        Battle._clean_image()
        print('Fight is over!')
        
        
    @staticmethod
    def _save_oponent_dragon():
        try:
            screenshot = pyt.screenshot(region=(2020, 104, 200, 140))
            screenshot.save('oponent_dragon.png')
        except: print('Failed to save the screenshot')
    
    @staticmethod
    def _clean_image():
        try: os.remove('oponent_dragon.png')
        except: print('Failed to remove the image')

    @staticmethod
    def _is_openent_dragon_defeated():
        image = getImagePositionRegion('oponent_dragon.png', 2020, 104, 2220, 245, .8, 1)
        if exists(image): return False
        else:
            Battle._save_oponent_dragon()
            return True
    
    @staticmethod
    def _check_and_select_dragon_with_double_damage():
        tries = 2
        swap_btn = Battle.get_swap_button()
        if not exists(swap_btn): 
            print('Check select double attack Swap button not found')
            return False
        
        while tries >= 0:
            inside_double_damage = Battle._get_inside_double_damage()
        
            if exists(inside_double_damage):
                print('Dragon already has critical damage') 
                return True
            
            moveAndClick(swap_btn)
            delay(1)
            double_damage = Battle._get_double_damage_btn()
            
            if not exists(double_damage): 
                print('No critical damage button found')
                return False
            Battle.change_dragon()
            delay(1)
            tries -= 1
        
    @staticmethod
    def _get_inside_double_damage():
        return getImagePositionRegion(C.FIGHT_INSIDE_DOUBLE_DAMAGE, *Battle.mon_quarters['4thRow'], .8, 2)
        
    @staticmethod 
    def _get_double_damage_btn():
        return getImagePositionRegion(C.FIGHT_DOUBLE_DAMAGE, *Battle.mon_quarters['2ndHorHalf'], .8, 2)
