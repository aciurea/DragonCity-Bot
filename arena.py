from close import Close
from popup import Popup
from utils import (ThreadWithValue,
                checkIfCanClaim,
                closePopup,
                closeVideo, 
                delay,
                exists, get_monitor_quarters,
                getImagePositionRegion,
                moveAndClick)
import constants as C

import concurrent.futures

def _check_attack_report():
    repeal = getImagePositionRegion(C.ARENA_REPEAL, 550, 550, 1100, 750, .8, 3)

    if exists(repeal):
        moveAndClick(repeal)
        checkIfCanClaim()
        closeVideo()
        delay(1)
        accept = getImagePositionRegion(C.ARENA_ATTACK_REPORT_ACCEPT, 550, 550, 1000, 670, .8, 3)
        if exists(accept): moveAndClick(accept)
        else: closePopup()
    
    threads = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_CLOSE_ATTACK_REPORT, 1100, 160, 1320, 300, .8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_ATTACK_REPORT_ACCEPT, 550, 550, 1000, 670, .8, 3)).start()
    ]
    
    for thread in threads:
        img = thread.join()
        print(img)
        if exists(img):
            moveAndClick(img)

class Battle:
    
    @staticmethod
    def is_fight_in_progress():
        return exists(getImagePositionRegion(C.FIGHT_IN_PROGRESS, *Popup.mon_quarters['1stCol'], .8, 1))

    @staticmethod
    def select_new_dragon():
        return getImagePositionRegion(C.FIGHT_SELECT_DRAGON, *Arena.mon_quarters['4thRow'], .8, 1)

    def wait_for_dragon_to_be_ready():
        print("Waiting for my turn...")
        if not Battle.is_fight_in_progress(): return print('Dragon is not available any more')
        
        times = 5
        while times > 0:
            if exists(getImagePositionRegion(C.FIGHT_SWAP, *Arena.mon_quarters['bottom_left'], .8, 1)): return
            delay(2)
            times -= 1

    @staticmethod
    def fight():
        if not Battle.is_fight_in_progress():
            new_dragon = Battle.select_new_dragon()
            if exists(new_dragon):
                moveAndClick(new_dragon)
                delay(1)
            else: return print('Fight ended')
        
        times = 5
        while times > 0:
            times -= 1
            play = getImagePositionRegion(C.FIGHT_PLAY, *Arena.mon_quarters['1stCol'], .8, 1)
            if exists(play):
                moveAndClick(play) # start
                delay(1)
                moveAndClick(play) # stop
            print("Dragon life is ok, continue..")

            # wait for my turn
            Battle.wait_for_dragon_to_be_ready()
        
        swap_btn = getImagePositionRegion(C.FIGHT_SWAP, *Arena.mon_quarters['bottom_left'], .8, 1)
        if exists(swap_btn): moveAndClick(swap_btn)
        
        return Battle.fight() # try again

class Arena:
    mon_quarters = get_monitor_quarters()

    @staticmethod
    def check_and_collect_rewards():
        # TODO to be implemented
        collect= getImagePositionRegion(C.ARENA_CHEST_COLLECT, 1015, 125, 1200, 200, .8, 3)

        if exists(collect):
            moveAndClick(collect)
            Popup.check_popup_chest()

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
        Close.check_if_ok()

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
        
        start_fight = getImagePositionRegion(C.ARENA_FIGHT, *Arena.mon_quarters['4thRow'], 0.8, 1)
        while exists(start_fight):
            # TODO check if I can collect the chest from TOP
            #Arena.check_and_collect_rewards()

            Arena.skip_strong_dragons()
            Arena.prepare_fight()
            moveAndClick(start_fight)

            delay(5)
            Battle.fight()

            collect_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, *Arena.mon_quarters['4thRow'], .8, 1)
            if exists(collect_btn): moveAndClick(collect_btn)

            Arena.close_buying_stats()

            delay(1)

            start_fight = getImagePositionRegion(C.ARENA_FIGHT, *Arena.mon_quarters['4thRow'], 0.8, 1)
        
        print('Fight is not ready yet or finished.')
        Close.check_if_ok()
       
    @staticmethod
    def close_buying_stats():
       #TODO to be implemented
        return True
    
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

print(Arena.enter_battle())
