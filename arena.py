import time
from battle import Battle
from close import check_if_ok
from move import moveTo
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

class Arena:
    mon_quarters = get_monitor_quarters()
    dump_screenshot_for_rewards = "dump_for_rewards.png"

    @staticmethod
    def _check_attack_report():
        accept = getImagePositionRegion(C.ARENA_REPORT_ACCEPT, *Arena.mon_quarters['3rdRow'], .8, 1)
        if exists(accept): 
            moveAndClick(accept)
            return print("Attack report accepted")

        moveAndClick(jsonPos["CLOSE_ATTACK"])
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
        if exists(getImagePositionRegion(C.ARENA_SPEED, *Arena.mon_quarters['bottom_left'], .8, 1)):
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
        start =  time.time()
        # is_no_durian = True

        while time.time() - start < 60: # 1 minute
            defeated_dragon_btn = getImagePositionRegion(C.ARENA_DEFETEAD_DRAGON, *Arena.mon_quarters['3rdRow'], .8, 1)
            select_new_dragon_btn = getImagePositionRegion(C.ARENA_SELECT_DRAGON, *Arena.mon_quarters['full'], .8, 1)

            if not exists(defeated_dragon_btn) and not exists(select_new_dragon_btn):
                check_if_ok()
                # if is_no_durian:
                #     print('No at least one durian available. Raising exception to stop the script.')
                #     raise Exception('No at least one durian available. Raising exception to stop the script.')
                return print('Dragons are ready for fight')

            if exists(defeated_dragon_btn):
                new_pos = [defeated_dragon_btn[0] - 20, defeated_dragon_btn[1] + 150]
                moveAndClick(new_pos)
                delay(1)
            elif exists(select_new_dragon_btn):
                moveAndClick(select_new_dragon_btn)
                delay(1)

            filter_dragons = getImagePositionRegion(C.ARENA_FILTER_DRAGONS, *Arena.mon_quarters['4thRow'], .8, 1)
            
            if not exists(filter_dragons): return print('Filter dragons button not found')
            moveAndClick(filter_dragons)
            delay(1)
            Arena.order_by_power()
            delay(1)

            # Dragons are too strong. For 10 category, raise exception if durian is not available.
            # durian = getImagePositionRegion(C.ARENA_DURIAN, *Arena.mon_quarters['2ndRow'], .8, 1)
            # if exists(durian): is_no_durian = False

            new_dragon = getImagePositionRegion(C.ARENA_NEW_DRAGON, *Arena.mon_quarters['2ndRow'], .8, 1)
            if not exists(new_dragon): raise Exception('No dragons available')
            moveAndClick(new_dragon)
            # TODO remove it
            temp = [1812, 969]
            delay(.1)
            moveAndClick(temp)
            delay(1)
        raise Exception('No more dragons to fight. Exit immediatelly')

    @staticmethod
    def get_fight_btn():
        return getImagePositionRegion(C.ARENA_FIGHT, *Arena.mon_quarters['4thRow'], .8, 2)

    def get_screenshot_for_rewards_collection():
        return getImagePositionRegion(Arena.dump_screenshot_for_rewards, 1000, 350, 1500, 550, .8, 1)
    
    def save_screenshot_for_rewards_collection():
        screenshot = pyautogui.screenshot(region=(1000, 350, 500, 200))
        screenshot.save(Arena.dump_screenshot_for_rewards)

    def remove_screenshot_for_rewards_collection():
        try:
            os.remove(Arena.dump_screenshot_for_rewards)
        except:
            print('No screenshot to remove')

    def wait_for_the_fight_tab():
        start = time.time()
        fight_tab = getImagePositionRegion(C.FIGHT_TAB, *Arena.mon_quarters['top_left'], .8, 1)    

        while time.time() - start < 10 and not exists(fight_tab):
            fight_tab = getImagePositionRegion(C.FIGHT_TAB, *Arena.mon_quarters['top_left'], .8, 1)
            delay(1)
        moveAndClick(fight_tab)

    def get_fight_spin():
        return getImagePositionRegion(C.ARENA_FIGHT_SPIN, *Arena.mon_quarters['4thRow'], .8, 1)

    def do_free_spin():
        free_spin = getImagePositionRegion(C.ARENA_FREE_SPIN, *Arena.mon_quarters['4thRow'], .8, 1)
        if exists(free_spin):
            moveAndClick(free_spin)
            delay(5)

    @staticmethod
    def enter_battle():
        arena = getImagePositionRegion(C.ARENA, *Arena.mon_quarters['1stCol'], .8, 1)
        if not exists(arena): return print('Arena not found')
        moveAndClick(arena)

        delay(2)
        Arena._check_attack_report()
        delay(1)
        Arena.claim_rush()
        delay(1)
        Arena.wait_for_the_fight_tab()
        delay(1)

        start_fight = Arena.get_fight_btn()
        time_limit = 300 # if doesn't end in 5 minutes, we stop the script.
        start_time = time.time()

        while exists(start_fight):
            if (time.time() - start_time) > time_limit: 
                Arena.remove_screenshot_for_rewards_collection()
                raise Exception('Time limit exceded on arena. Closing the app....')

            Arena.skip_strong_dragons()
            try: Arena.prepare_fight()
            except: return
            Arena.save_screenshot_for_rewards_collection()
            Arena.check_and_collect_rewards()

            moveAndClick(start_fight)
            delay(1)
            Arena.do_free_spin()
            moveAndClick(Arena.get_fight_spin())

            Arena.wait_for_tabble_to_start()
            Battle.fight()
            
            delay(3)

            Arena.collect_arena_battle_rewards()
            delay(1)
            Arena.close_buying_dragon_powers()
            start_fight = Arena.get_fight_btn()
        check_if_ok()
        print('Arena battle is over')

    def wait_for_tabble_to_start():
        start = time.time()
        # wait for 25 seconds to start fight. If not, then the application crashes so throw an exception

        while time.time() - start < 25:
            if Battle.is_fight_in_progress(): return
            delay(1)
        raise Exception('Time limit exceded on arena. Closing the app....')

    def claim_rush():
        rush = getImagePositionRegion(C.ARENA_CLAIM_RUSH, *Arena.mon_quarters['4thRow'], .8, 1)

        if not exists(rush): return 
        moveAndClick(rush)
        delay(2)
        moveAndClick([1250, 1215])
        delay(2)

        times = 5
        while times > 0:
            times -= 1
            Popup.check_popup_chest
            delay(2)

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
        Arena.remove_screenshot_for_rewards_collection()

    @staticmethod
    def close_buying_dragon_powers():
        if exists(Arena.get_fight_btn()): return 

        check_if_ok() # first we hit the close button

    @staticmethod
    def skip_strong_dragons():
        strong_dragons = [
            [C.ARENA_HIGH_ARCANA, *Arena.mon_quarters['bottom_right']],
            [C.ARENA_HAXED_VAMPIRE, *Arena.mon_quarters['bottom_right']],
            [C.ARENA_DUAL_PERFECEPTION, *Arena.mon_quarters['bottom_right']],
            [C.ARENA_DUAL_PARLIAMENT, *Arena.mon_quarters['bottom_right']],
        ]
        
        times = 2
        while times > 0:
            times -= 1
            with concurrent.futures.ThreadPoolExecutor() as executor:
                result_list = executor.map(lambda args: getImagePositionRegion(*args, .8, 1), strong_dragons)
            
                for is_strong_dragon in result_list:
                    if exists(is_strong_dragon):
                        moveAndClick(getImagePositionRegion(C.ARENA_SKIP, *Arena.mon_quarters['4thRow'], .8, 1))
                        break
                delay(3)
