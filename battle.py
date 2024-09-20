import random
import time
import pyautogui as pyt
import concurrent.futures

import constants as C

from screeninfo import get_monitors
from screen import Screen
from close import check_if_ok
from move import moveAndClick
from utils import (
                get_int,
                delay,
                exists,
                get_grid_monitor,
                get_monitor_quarters,
                getImagePositionRegion,
                get_screen_resolution,
                is_in_time,
                )
from screen import Screen


text = {
    'select': 'select',
    'selectdragon': 'selectdragon',
}

class Battle:
    base = './img/battle/'
    grid = get_grid_monitor()
    mon_quarters = get_monitor_quarters()
    res = get_monitors()[0]
    one_third = get_int(res.width / 3)
    screen_res = get_screen_resolution()


    def get_select_btn():
        grid = Battle.grid
        position = [grid['x0'], grid['y4'], grid['x8'], grid['y6']]

        return getImagePositionRegion(C.FIGHT_SELECT_DRAGON, *position, .8, 1)
    
    @staticmethod
    def get_speed_btn():
        position = [*Screen.get_pos([0.0197916, 0.238]), *Screen.get_pos([0.07, 0.3185185])]
       
        path = f'{Battle.base}/{Battle.screen_res}_x4.png'

        return getImagePositionRegion(path, *position, .8, 1)
    
    @staticmethod
    def _is_on_team_selection():
        bbox = [0.3947916, 0.03148148,0.472395835, 0.0935185]

        text_positions = Screen.get_text_pos(bbox)
   
        for t in text_positions:
            if Screen.is_match_with_one_difference(text['select'], t['text']): return t['position']
        return [-1]

    # 0.008 time.
    @staticmethod
    def get_play_button():
        position = [*Screen.get_pos([0.0197916, 0.15]), *Screen.get_pos([0.06979167, 0.234])]
        path = f'{Battle.base}/{Battle.screen_res}_play.png'

        return getImagePositionRegion(path, *position, .8, 1)

    @staticmethod
    def _get_attack_ready():
        path = f'{Battle.base}/{Battle.screen_res}_ico.png'
        positions = [
            [*Screen.get_pos([0.840625, 0.8537037]), *Screen.get_pos([0.8921875, 0.93])],
            [*Screen.get_pos([0.253125, 0.6759259]), *Screen.get_pos([0.9671875, 0.774074])]
        ]
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(path, *args, .8, 1), positions)
            for close_btn in result_list:
                if exists(close_btn): return True
        return False
    
    def get_no_btn():
        return getImagePositionRegion(C.ARENA_NO, *Battle.mon_quarters['full'], .8, 1) # TODO update it with grid to be faster 
    
    @staticmethod
    def is_in_battle():
        work = [Battle.get_play_button, Battle.get_speed_btn, Battle._is_on_team_selection]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            btns = executor.map(lambda func: func(), work)
            for btn in btns:
                if exists(btn): return True
        return False
    
    @staticmethod
    def wait_for_battle_to_start(times = 15):
        if times == 0:  raise Exception('Battle didn`t start in time....')

        if Battle.is_in_battle(): return print('Ready to fight!')
        else: print('Fight not ready')
        delay(1)
        return Battle.wait_for_battle_to_start(times - 1)
       
        
    @staticmethod
    def get_new_dragon_btn():
        bbox = [0.09895834, 0.83425925, 0.89375, 0.899074]
        bbox2 = [0.09895834, 0.77685185, 0.9052083,0.899074] #  takes screenshot of values.

        text_positions = Screen.get_text_pos(bbox)

        lst = []

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['selectdragon'], t['text']):
                lst.append( t['position'])
        
        return random.choice(lst) if lst else [-1]

    @staticmethod
    def _get_swap_button():
        position = [*Screen.get_pos([0.00729167, 0.7167]), *Screen.get_pos([0.0645834, 0.83518518])]
        path = f'{Battle.base}/{Battle.screen_res}_swap.png'

        return getImagePositionRegion(path, *position, .8, 1)

    @staticmethod
    def wait_for_oponent_to_attack(times = 10):
        if times == 0: return False
        if Battle._get_attack_ready(): return True
        delay(1)
        return Battle.wait_for_oponent_to_attack(times - 1)
    
    @staticmethod
    def change_dragon():
        swap_btn = Battle._get_swap_button()
        if exists(swap_btn):
            moveAndClick(swap_btn)
            delay(1)
        new_dragon = Battle.get_new_dragon_btn()
        if not exists(new_dragon): return print('Dragon not found')
        moveAndClick(new_dragon)

    # TODO is working but the threshold of 3 seconds to check if the play button exists is too high.
    # try to check for the team an return immediatelly if both criteria don't match
    @staticmethod
    def _battle_with_no_change_dragon():
        start = time.time()
        moveAndClick(Battle.get_play_button())
        while is_in_time(start, limit = 120):
            if not Battle.is_in_battle(): return 
            delay(3)

    @staticmethod
    def fight(change_dragon=True):
        # Battle._save_oponent_dragon()

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
                    return print('Not in battle....')

                Battle.wait_for_oponent_to_attack()

                # dragon is defetead
                if exists(Battle._is_on_team_selection()): break

                # dragon is the last one
                if not exists(Battle._get_swap_button()):
                    is_last_dragon = True
                    break # exit the loop since is the last dragon and no need for play and pause

                play = Battle.get_play_button()

                # try to select dragon with double damage
                ## TODO do it later
                # if first_time_checking_oponent == True or Battle._is_openent_dragon_defeated():
                #     Battle._check_and_select_dragon_with_double_damage()
                #     first_time_checking_oponent = False
                
                moveAndClick(play)
                delay(.2)
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
        
        # Battle._clean_image()
        # Battle._has_dragon_leveled_up()
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
        swap_btn = Battle._get_swap_button()
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

    @staticmethod
    def _has_dragon_leveled_up():
        bbox = [777, 1230, 1015, 1310]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if 'got' in t['text'].lower():
                moveAndClick(t['position'])
                return True
