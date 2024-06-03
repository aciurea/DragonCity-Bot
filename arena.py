import time
from battle import Battle
from close import check_if_ok
from move import multiple_click
from popup import Popup
from utils import (
                delay,
                exists,
                get_grid_monitor,
                get_json_file,
                get_monitor_quarters,
                getImagePositionRegion,
                moveAndClick)
import constants as C
import concurrent.futures

jsonPos = get_json_file('arena.json')

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
        #TODO improvement: check if we have a video to close

    @staticmethod
    def check_and_collect_rewards():
        collect = getImagePositionRegion(C.ARENA_CHEST_COLLECT, *Arena.mon_quarters['1stRow'], .8, 1)

        if exists(collect):
            multiple_click(collect)
            delay(1)
            Popup.check_popup_chest()
            check_if_ok()
            delay(.3)

    @staticmethod
    def prepare_fight():
        if exists(Arena.get_dragon_defeated_pos()):
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

    def get_dragon_defeated_pos():
        pos = [Arena.grid['x0'], Arena.grid['y2'], Arena.grid['x8'], Arena.grid['y5']]
        
        return getImagePositionRegion(C.ARENA_DEFETEAD_DRAGON, *pos, .8, 1)
    
    def is_defeated_dragon_in_select_team():
        pos = [Arena.grid['x0'], Arena.grid['y3'], Arena.grid['x7'], Arena.grid['y5']]
        
        return exists(getImagePositionRegion(C.ARENA_DEFETEAD_DRAGON_SELECT_TEAM, *pos, .8, 1))
    
    def get_select_dragon_btn():
        pos = [Arena.grid['x0'], Arena.grid['y4'], Arena.grid['x7'], Arena.grid['y5']]

        return getImagePositionRegion(C.ARENA_SELECT_DRAGON, *pos, .8, 1)

    @staticmethod
    def change_defetead_dragon():
        start =  time.time()

        while time.time() - start < 60: # 1 minute
            if not Arena.is_defeated_dragon_in_select_team():
                check_if_ok()
                return print('Dragons are ready for fight')
            select_new_dragon_btn = Arena.get_select_dragon_btn()
            moveAndClick(select_new_dragon_btn)
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
        Arena.claim_rush()
        delay(1)
        Arena.wait_for_the_fight_tab()
        delay(1)

        start_fight = Arena.get_fight_btn()
        time_limit = 420 # if doesn't end in 5 minutes, we stop the script.
        start_time = time.time()

        while exists(start_fight):
            if (time.time() - start_time) > time_limit: 
                raise Exception('Time limit exceded on arena. Closing the app....')
            
            print('Start new Arena battle')
            # Arena.skip_strong_dragons()
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
        rush = getImagePositionRegion(C.ARENA_CLAIM_RUSH, *Arena.mon_quarters['4thRow'], .8, 1)

        if not exists(rush): return 
        moveAndClick(rush)
        delay(2)
        moveAndClick([1250, 1215])
        delay(5)

        times = 5
        while times > 0:
            times -= 1
            Popup.check_popup_chest()
            delay(2)

    @staticmethod
    def collect_arena_battle_rewards():
        collect_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, *Arena.mon_quarters['4thRow'], .8, 1)

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
    def skip_strong_dragons():
        strong_dragons = [ 
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
