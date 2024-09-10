import time
import datetime
import concurrent.futures

import constants as C

from battle import Battle
from close import check_if_ok
from move import multiple_click
from popup import Popup
from utils import (
                delay,
                exists,
                get_grid_monitor,
                get_monitor_quarters,
                getImagePositionRegion,
                get_int,
                moveAndClick)
from screen import Screen

jsonPos = {
    "STATIC_CLAIM_BATTLE": [1265, 1295],
    "CLOSE_ATTACK": [1980, 370]
}

class Arena:
    mon_quarters = get_monitor_quarters()
    grid = get_grid_monitor()
    dump_screenshot_for_rewards = "dump_for_rewards.png"

    @staticmethod
    def _check_attack_report():
        accept = getImagePositionRegion(C.ARENA_REPORT_ACCEPT, *Arena.mon_quarters['3rdRow'], .8, 1)
        if exists(accept): 
            moveAndClick(accept)
            return print("Attack report accepted")

        moveAndClick(jsonPos["CLOSE_ATTACK"])

    @staticmethod
    def check_and_collect_rewards():
        bbox = [0.462890625, 0.146527, 0.527734375, 0.195834]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference('collect', t['text'].lower()):
                multiple_click(t['position'])
                delay(1)
                Popup.check_popup_chest()
                check_if_ok()
                delay(.3)

    @staticmethod
    def prepare_fight():
        bbox = [0.118359375, 0.679167, 0.411328125, 0.731945]
        text_positions = Screen.get_text_pos(bbox)
        if len(text_positions) == 3: return

        bbox = [0.25390625, 0.7916, 0.337890625, 0.861]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if 'change' in t['text'].lower():
                moveAndClick(t['position'])
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
        bboxes = [
            [510, 1040, 710, 1110],
            [1330, 1040, 1530, 1110],
            [2155, 1040, 2345, 1110],
        ]

        for bbox in bboxes:
            text_positions = Screen.get_text_pos(bbox)
            if  len(text_positions) > 0 and 'enhance' in text_positions[0]['text'].lower(): continue

            moveAndClick([bbox[0], bbox[1]])
            delay(1)
            filter_dragons = getImagePositionRegion(C.ARENA_FILTER_DRAGONS, *Arena.mon_quarters['4thRow'], .8, 1)
            
            if not exists(filter_dragons): return print('Filter dragons button not found')
            moveAndClick(filter_dragons)
            delay(1)
            Arena.order_by_power()
            delay(1)

            new_dragon = getImagePositionRegion(C.ARENA_NEW_DRAGON, *Arena.mon_quarters['2ndRow'], .8, 1)
            if not exists(new_dragon): raise Exception('No dragons available')
            moveAndClick(new_dragon)
            delay(1)
        check_if_ok()

    @staticmethod
    def get_fight_btn():
        return getImagePositionRegion(C.ARENA_FIGHT, *Arena.mon_quarters['4thRow'], .8, 2)

    def get_screenshot_for_rewards_collection():
        return getImagePositionRegion(Arena.dump_screenshot_for_rewards, 1000, 350, 1500, 550, .8, 1)

    def wait_for_the_fight_tab():
        start = time.time()
        fight_tab = Arena._get_fight_tab()

        while time.time() - start < 10 and not exists(fight_tab):
            fight_tab = Arena._get_fight_tab()
            delay(1)
        moveAndClick(fight_tab)


    def get_fight_spin():
        return getImagePositionRegion(C.ARENA_FIGHT_SPIN, *Arena.mon_quarters['4thRow'], .8, 1)

    def do_free_spin():
        free_spin = getImagePositionRegion(C.ARENA_FREE_SPIN, *Arena.mon_quarters['4thRow'], .8, 1)
        if exists(free_spin):
            moveAndClick(free_spin)
            delay(10)
        fight_spin = Arena.get_fight_spin()
        if exists(fight_spin): moveAndClick(fight_spin)
            
    @staticmethod
    def enter_battle():
        arena = getImagePositionRegion(C.ARENA, *Arena.mon_quarters['1stCol'], .8, 1)
        if not exists(arena): return print('Arena not found')
        moveAndClick(arena)

        delay(2)
        Arena._check_attack_report()
        delay(1)
        Arena._check_season_end()
        Arena.claim_rush()
        delay(1)
        Arena.wait_for_the_fight_tab()
        delay(1)

        start_fight = Arena.get_fight_btn()
        time_limit = 600 # if doesn't end in 10 minutes, we stop the script.
        start_time = time.time()

        while exists(start_fight):
            if (time.time() - start_time) > time_limit: 
                raise Exception('Time limit exceded on arena. Closing the app....')
            
            print('Start new Arena battle')
            try: Arena.prepare_fight()
            except: return
            Arena.check_and_collect_rewards()

            moveAndClick(start_fight)
            delay(1)
            Arena.do_free_spin()
            Battle.fight()
            
            delay(3)

            Arena.collect_arena_battle_rewards()
            delay(1)
            Arena.close_buying_dragon_powers()
            start_fight = Arena.get_fight_btn()
        check_if_ok()
        print('Arena battle is over')

    def claim_rush():
        bbox = [0.622265625, 0.854861, 0.71875, 0.9305]
        text_positions = Screen.get_text_pos(bbox)
        for t in text_positions:
            if Screen.is_match_with_one_difference('CLAIMI', t['text'].lower()):
                moveAndClick(t['position'])
                delay(2)
                moveAndClick([1250, 1215])
                delay(5)
                times = 5
                while times > 0:
                    times -= 1
                    Popup.check_popup_chest()
                    delay(1)

    @staticmethod
    def collect_arena_battle_rewards():
        collect_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, *Arena.mon_quarters['full'], .8, 2)

        if exists(collect_btn):
            moveAndClick(collect_btn)
        else:
            moveAndClick(jsonPos["STATIC_CLAIM_BATTLE"])
            print('Collect button not found')
        delay(3)

    @staticmethod
    def close_buying_dragon_powers():
        if exists(Arena.get_fight_btn()): return 

        check_if_ok() # first we hit the close button

    @staticmethod
    def _get_fight_tab():
        bbox = [0.28984375, 0.232, 0.35078125, 0.278]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference('fight', t['text'].lower()):  return t['position']
              
        return [-1]

    @staticmethod
    def _check_season_end():
        if exists(Arena._get_fight_tab()): return print('Season is over. No need to check if ended.')
        thursday = 3
        # On Thursday the season ends, therefore we need to check if the season ended
        # due to changes on position of the screen, enlarge the search are.
        # Larger search area, takes more time, therefore, run the search on larger area only on Thursday

        bbox = [0.2, 0.2, .9, .9] if datetime.datetime.now().weekday() == thursday else [0.41015625, 0.7638, 0.578125, 0.850694]
        st = time.time()
        text_positions = Screen.get_text_pos(bbox)
        print(f"Time to get text positions: {time.time() - st}")
        for t in text_positions:
            if Screen.is_match_with_one_difference('start', t['text'].lower()):
                moveAndClick(t['position'])
        