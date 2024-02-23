import time
from close import check_if_ok
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
import pyautogui
import os

jsonPos = get_json_file('arena.json')

class Battle:
    
    @staticmethod
    def is_fight_in_progress():
        if exists(Battle.get_speed_button()): return True

        return exists(Battle.get_new_dragon_btn())

    @staticmethod
    def get_speed_button():
        return getImagePositionRegion(C.FIGHT_IN_PROGRESS, *Popup.mon_quarters['1stCol'], .8, 1)

    @staticmethod
    def get_play_button():
        return getImagePositionRegion(C.FIGHT_PLAY, *Popup.mon_quarters['1stCol'], .8, 1)
    
    @staticmethod
    def get_new_dragon_btn():
        return getImagePositionRegion(C.FIGHT_SELECT_DRAGON, *Arena.mon_quarters['4thRow'], .8, 1)
    
    @staticmethod
    def get_swap_button():
        return getImagePositionRegion(C.FIGHT_SWAP, *Arena.mon_quarters['bottom_left'], .8, 1)

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
        is_last_dragon = False
        while Battle.is_fight_in_progress():

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

class Arena:
    mon_quarters = get_monitor_quarters()
    dump_screenshot_for_rewards = "dump_for_rewards.png"

    @staticmethod
    def _check_attack_report():
        if not exists(getImagePositionRegion(C.ARENA_REPORT, *Arena.mon_quarters['top_left'], .8, 1)): return
       
        accept = getImagePositionRegion(C.ARENA_REPORT_ACCEPT, *Arena.mon_quarters['3rdRow'], .8, 1)
        if exists(accept): 
            moveAndClick(accept)
            return print("Attack report accepted")

        check_if_ok()
        #TODO improvement: check if we have a video to close

    @staticmethod
    def check_and_collect_rewards():
        collect = getImagePositionRegion(C.ARENA_CHEST_COLLECT, *Arena.mon_quarters['1stRow'], .8, 1)

        if exists(collect):
            Popup.multiple_click(collect)
            delay(1)
            Popup.check_popup_chest()
            check_if_ok()
            delay(.3)

    @staticmethod
    def prepare_fight():
        while exists(getImagePositionRegion(C.ARENA_SPEED, *Arena.mon_quarters['bottom_left'], .8, 1)):
            change_btn = getImagePositionRegion(C.ARENA_CHANGE, *Arena.mon_quarters['bottom_left'], .8, 1)
            if not exists(change_btn): return print('Change button not found')
            moveAndClick(change_btn)
            delay(1)
            Arena.change_defetead_dragon()

    @staticmethod
    def order_by_power():
        order_by = getImagePositionRegion(C.ARENA_ORDER_BY, *Arena.mon_quarters['top_right'], .8, 1)

        if not exists(order_by): return print('Order by button not found')
        moveAndClick(order_by)
        delay(1)
        order_by_power_des = getImagePositionRegion(C.ARENA_ORDER_BY_POWER, *Arena.mon_quarters['full'], .8, 1)
        if not exists(order_by_power_des): return print('Order by power button not found')
        new_pos = [order_by_power_des[0] + 50, order_by_power_des[1] + 50]
        moveAndClick(new_pos)

    @staticmethod
    def change_defetead_dragon():
        pos = getImagePositionRegion(C.ARENA_DEFETEAD_DRAGON, *Arena.mon_quarters['3rdRow'], .8, 1)
        if not exists(pos): return print('No defetead dragon found')

        new_pos = [pos[0] - 20, pos[1] + 150]
        moveAndClick(new_pos)
        delay(1)
        filter_dragons = getImagePositionRegion(C.ARENA_FILTER_DRAGONS, *Arena.mon_quarters['4thRow'], .8, 1)
        
        if not exists(filter_dragons): return print('Filter dragons button not found')
        moveAndClick(filter_dragons)
        delay(1)
        Arena.order_by_power()
        delay(1)

        new_dragon = getImagePositionRegion(C.ARENA_NEW_DRAGON, *Arena.mon_quarters['2ndRow'], .8, 1)
        
        if not exists(new_dragon): return print('New dragon not found')
        moveAndClick(new_dragon)
        delay(1)
        check_if_ok()

    @staticmethod
    def get_fight_btn():
        return getImagePositionRegion(C.ARENA_FIGHT, *Arena.mon_quarters['4thRow'], .8, 2)

    
    def get_screenshot_for_rewards_collection():
        return getImagePositionRegion(Arena.dump_screenshot_for_rewards, 1000, 350, 1500, 550, .8, 1)
    
    def save_screenshot_for_rewards_collection():
        screenshot = pyautogui.screenshot(region=(1000, 350, 500, 200))
        screenshot.save(Arena.dump_screenshot_for_rewards)

    @staticmethod
    def enter_battle():
        arena = getImagePositionRegion(C.ARENA, *Arena.mon_quarters['1stCol'], .8, 1)
        if not exists(arena): return print('Arena not found')
        moveAndClick(arena)

        delay(1)

        fight_tab = getImagePositionRegion(C.FIGHT_TAB, *Arena.mon_quarters['top_left'], .8, 1)    
        if not exists(fight_tab): return print('Fight tab not found')
        moveAndClick(fight_tab)

        delay(1)
        Arena._check_attack_report()
        delay(1)

        start_fight = Arena.get_fight_btn()
        while exists(start_fight):
            Arena.skip_strong_dragons()
            Arena.prepare_fight()
            Arena.save_screenshot_for_rewards_collection()
            Arena.check_and_collect_rewards()

            moveAndClick(start_fight)
           
            # wait for the battle to start.
            while not Battle.is_fight_in_progress(): delay(1)

            Battle.fight()
            
            delay(3)

            Arena.collect_arena_battle_rewards()
            Arena.close_buying_dragon_powers()
            start_fight = Arena.get_fight_btn()

        print('Fight is not ready yet or finished.')
        check_if_ok()

    @staticmethod
    def collect_arena_battle_rewards():
        collect_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, *Arena.mon_quarters['4thRow'], .8, 1)

        if exists(collect_btn):
            moveAndClick(collect_btn)
        else:
            moveAndClick(jsonPos["STATIC_CLAIM_BATTLE"])
            print('Collect button not found')

        start = time.time()
        seconds_limit_to_collect_rewards = 7

        while (time.time() - start < seconds_limit_to_collect_rewards
            and not exists(Arena.get_screenshot_for_rewards_collection())):
            delay(1)
        os.remove(Arena.dump_screenshot_for_rewards)
       

    @staticmethod
    def close_buying_dragon_powers():
        if exists(Arena.get_fight_btn()): return 

        check_if_ok() # first we hit the close button
        check_if_ok() # then we check if we have the loose button and close it.
        delay(1)

    @staticmethod
    def skip_strong_dragons():
        strong_dragons = [
            [C.ARENA_HIGH_ARCANA, *Arena.mon_quarters['bottom_right']]
        ]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), strong_dragons)
            for is_strong_dragonb in result_list:
                if exists(is_strong_dragonb):
                    moveAndClick(getImagePositionRegion(C.ARENA_SKIP, *Arena.mon_quarters['4thRow'], .8, 1))
                    delay(5)
