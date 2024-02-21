from close import Close
from freeze import log_arena_fights, freeze_dragons
from open import open_app
from popup import Popup
from utils import (ThreadWithValue,
                checkIfCanClaim,
                closePopup,
                closeVideo, 
                delay,
                exists, get_monitor_quarters,
                getImagePositionRegion,
                moveAndClick,
                moveTo)
import constants as C
import random
import time
# from ahk import AHK
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

def _check_if_can_fight():
    cannot_fight = getImagePositionRegion(C.ARENA_DEFETEAD_DRAGON,180, 380, 790, 490, .8, 3)

    if not exists(cannot_fight):
        return print('Battle button not found')
    delay(.5)
    change = getImagePositionRegion(C.ARENA_CHANGE, 375, 670, 590 ,760, .8, 3)

    if not exists(change):
        return print('Change button not found.')
    moveAndClick(change)
    
    # try 3 times for 3 dragons
    btns = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_SPEED, 280, 620, 680, 720, .8, 20)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_SPEED, 800, 620, 1020, 720, .8, 20)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_SPEED, 1300, 620, 1530, 720, .8, 20)).start(),
    ]

    index = 0
    for item in btns:
        speed_up_btn = item.join()
        if not exists(speed_up_btn): 
            index += 1
            continue
        moveAndClick([speed_up_btn[0] - 175, speed_up_btn[1]])
        delay(1)
        left_arrow = [1084, 760]
        moveAndClick(left_arrow)
        delay(.5)
        dragon = [660, 330]
        moveAndClick(dragon)
        delay(2)
    if index == len(btns):
        log_arena_fights(['\n [Lost all dragons... \n BATTLE LOST] \n', "lost_fights"])
    closePopup()

def _check_and_collect():
    collect= getImagePositionRegion(C.ARENA_CHEST_COLLECT, 1015, 125, 1200, 200, .8, 3)

    if exists(collect):
        moveAndClick(collect)
        Popup.check_popup_chest

def arena():
    delay(1)
    arena_quest = getImagePositionRegion(C.ARENA_QUEST, 0, 380, 120, 530, .8, 1)
    arena_quest = arena_quest if exists(arena_quest) else [65, 435]
    moveAndClick(arena_quest)
    inside_arena()

def _ready_for_battle():
    start = time.time()
    to_execute = [
        [C.BATTLE_ATTACK_IS_AVAILABLE, 1330, 750, 1425,850, .8, 1],
        [C.ARENA_NEW_DRAGON, 0, 600, 1600, 850, .8, 1]
    ]

    while (time.time() - start < 20):
        moveTo([random.randrange(0, 1600), random.randrange(0, 800)])
        with concurrent.futures.ThreadPoolExecutor() as executor:
            items = executor.map(lambda args: getImagePositionRegion(*args), to_execute)
            for item in items:
                if (exists(item)): return
        delay(.5)

def inside_arena():
    _check_attack_report()
    _check_if_can_fight()
    _check_and_collect()
    moveTo([random.randrange(100, 1500), random.randrange(100, 700)])

    fight = getImagePositionRegion(C.ARENA_FIGHT, 740, 730, 870, 800, 0.8, 20)

    if not exists(fight): 
        closePopup()
        return print('No fight button found')
    moveAndClick(fight)
    _ready_for_battle()
    freeze_dragons()
    print('battle finished')
    claim_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, 700, 750, 900, 850, .8, 10)
    moveAndClick(claim_btn, 'No arena claim button')
    return inside_arena()


class Arena:
    mon_quarters = get_monitor_quarters()
    
    @staticmethod
    def is_fight_in_progress():
        return exists(getImagePositionRegion(C.FIGHT_IN_PROGRESS, *Popup.mon_quarters['1stCol'], .8, 1))

    @staticmethod
    def select_new_dragon():
        return getImagePositionRegion(C.FIGHT_SELECT_DRAGON, *Arena.mon_quarters['4thRow'], .8, 1)

    @staticmethod
    def fight():
        if not Arena.is_fight_in_progress():
            new_dragon = Arena.select_new_dragon()
            if exists(new_dragon):
                moveAndClick(new_dragon)
                delay(1)
                return Arena.fight()
            return print('Fight ended')

        # TODO not able to know when the dragon has low life.
        while exists(getImagePositionRegion(C.FIGHT_GOOD_LIFE, *Arena.mon_quarters['top_left'], .8, 1)):
            play = getImagePositionRegion(C.FIGHT_PLAY, *Arena.mon_quarters['1stCol'], .8, 1)
            if exists(play):
                moveAndClick(play) # start
                delay(1)
                moveAndClick(play) # stop
            print("Dragon life is ok, continue..")
            
            # wait for my turn
            while not exists(getImagePositionRegion(C.FIGHT_SWAP, *Arena.mon_quarters['bottom_left'], .8, 1)):
                delay(2)
                if not Arena.is_fight_in_progress(): return Arena.fight()
                print("Waiting for my turn...")
        
        swap_btn = getImagePositionRegion(C.FIGHT_SWAP, *Arena.mon_quarters['bottom_left'], .8, 1)
        if exists(swap_btn): moveAndClick(swap_btn)
        
        return Arena.fight() # try again

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

        if exists(arena):
            moveAndClick(arena)
            delay(1)
            fight_tab = getImagePositionRegion(C.FIGHT_TAB, *Arena.mon_quarters['top_left'], .8, 1)    
            if exists(fight_tab):
                moveAndClick(fight_tab)
                delay(1)
            # Arena.prepare_fight()
            fight = getImagePositionRegion(C.ARENA_FIGHT, *Arena.mon_quarters['4thRow'], 0.8, 20)
            if not exists(fight): print('Fight is not ready yet')
            # moveAndClick(fight)
            moveTo(fight)
            # delay(5)
            # Arena.fight()

            # try to hit the collect button
            # check for the annoying popup of buying with gems after losing a fight

        else: print('Arena button not found')

# print(Arena.enter_battle())