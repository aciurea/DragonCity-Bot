import time
from close import check_if_ok
from popup import Popup
from utils import (
                delay,
                exists,
                get_monitor_quarters,
                getImagePositionRegion,
                moveAndClick)
import constants as C
import concurrent.futures

class Battle:
    
    @staticmethod
    def is_fight_in_progress():
        if exists(Battle.get_play_button()): return True

        return exists(Battle.get_new_dragon_btn())

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
      
        while (time.time() - start < 10  # wait for 10 seconds and stop
               and 
               not exists(getImagePositionRegion(C.FIGHT_SWAP, *Arena.mon_quarters['bottom_left'], .8, 1))):
            delay(1)
    
    @staticmethod
    def change_dragon():
        swap_btn = Battle.get_swap_button()
        if not exists(swap_btn): return print('Swap button not found')
        moveAndClick(swap_btn)

        delay(1)

        moveAndClick(Battle.get_new_dragon_btn())
        print('Dragon was changed')

    @staticmethod
    def fight():
        while Battle.is_fight_in_progress():
            # prepare to fight
            last_dragon = False
            attacks_per_dragon = 3

            if last_dragon:
                delay(3)
                continue # go to next iteration

            while attacks_per_dragon > 0 and not last_dragon:
                attacks_per_dragon -= 1

                # dragon is defetead
                new_dragon_button = Battle.get_new_dragon_btn()
                if exists(new_dragon_button):
                    moveAndClick(new_dragon_button)
                    print('Dragon was defetead')
                    break

                # dragon is the last one
                swap_btn = Battle.get_swap_button()
                if not exists(swap_btn):
                    last_dragon = True
                    print('Dragon is the last one')
                    attacks_per_dragon = 0
                    break # exit the loop since is the last dragon

                # attack is ok, play and pause
                play = Battle.get_play_button()
                moveAndClick(play)
                delay(1)
                moveAndClick(play) # pause

                # wait for opponent to attack
                Battle.wait_for_oponent_to_attack()

            # check if is last dragon and just hit the play button
            if last_dragon: moveAndClick(Battle.get_play_button())

            # swap the dragon
            Battle.change_dragon()

        print('Fight is over')
                

class Arena:
    mon_quarters = get_monitor_quarters()

    @staticmethod
    def _check_attack_report():
        accept = getImagePositionRegion(C.ARENA_REPORT_ACCEPT, *Arena.mon_quarters['3rdRow'], .8, 1)
        if not exists(accept): 
            return print('No report found')
            # not working because it will close the popup
            #check_if_ok()  # there is a change that the report to be positive and we need to close the popup.

        moveAndClick(accept)

        #TODO improvement: check if we have a video to close

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
        check_if_ok()

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

            Arena.close_buying_dragon_powers()

            delay(1)

            start_fight = getImagePositionRegion(C.ARENA_FIGHT, *Arena.mon_quarters['4thRow'], 0.8, 1)
        
        print('Fight is not ready yet or finished.')
        check_if_ok()
       
    @staticmethod
    def close_buying_dragon_powers():
        check_if_ok() # first we hit the close button
        check_if_ok() # then we check if we have the loose button and close it.

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