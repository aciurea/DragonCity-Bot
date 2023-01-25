from freeze import freeze_dragons
from open import open_app
from utils import (ThreadWithValue, checkIfCanClaim,
                closePopup,
                closeVideo, 
                delay,
                exists,
                getImagePositionRegion,
                moveAndClick,
                moveTo,
                openChest)
import constants as C
import random
import time
from ahk import AHK

def check_attack_report():
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

def check_if_can_fight():
    cannot_fight = getImagePositionRegion(C.ARENA_WAIT_TIME,180, 380, 790, 490, .8, 3)

    if not exists(cannot_fight):
        return print('Battle button not found')
    delay(.5)
    change = getImagePositionRegion(C.ARENA_CHANGE_DRAGON, 375, 670, 590 ,760, .8, 3)

    if not exists(change):
        return print('Change button not found.')
    moveAndClick(change)
    
    # try 3 times for 3 dragons
    list = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_SPEED_UP, 280, 620, 680, 720, .8, 20)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_SPEED_UP, 800, 620, 1020, 720, .8, 20)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_SPEED_UP, 1300, 620, 1530, 720, .8, 20)).start(),
    ]

    for item in list:
        speed_up_btn = item.join()
        if not exists(speed_up_btn): continue
        moveAndClick([speed_up_btn[0] - 175, speed_up_btn[1]])
        delay(1)
        left_arrow = [1084, 760]
        moveAndClick(left_arrow)
        delay(.5)
        dragon = [660, 330]
        moveAndClick(dragon)
        delay(2)
    closePopup()
           

def check_and_collect():
    collect= getImagePositionRegion(C.ARENA_CHEST_COLLECT, 1015, 125, 1200, 200, .8, 3)

    if exists(collect):
        moveAndClick(collect)
        openChest()

def arena():
    delay(1)
    if not exists(getImagePositionRegion(C.ARENA_QUEST, 1000, 120, 1200, 220)): 
        return print('No arena found')
   
    arena_btn = [1100, 400]; # We should calculate in percentages
    moveAndClick(arena_btn)
    delay(2)
    inside_arena()

def  _get_select_new_dragon_btn():
    times = 0
    select_new_dragon = getImagePositionRegion(C.ARENA_SELECT_NEW_DRAGON_BTN, 640, 740, 1600, 830, .8, 1)

    while not exists(select_new_dragon):
        if (times >= 5): return [-1]
        times += 1
        delay(1)
        select_new_dragon = getImagePositionRegion(C.ARENA_SELECT_NEW_DRAGON_BTN, 640, 740, 930, 830, .8, 1)
    return select_new_dragon

##mouse pos (1003, 139)
##mouse pos (1087, 143)

def _prepare_dragons_for_fight():
    start = time.time()

    while (time.time() - start < 30):
        swap_btn, select_new_dragon_btn = [
            ThreadWithValue(target=getImagePositionRegion, args=(C.FIGHT_SWAP_DRAGON, 80, 650, 305, 740, .8, 1)).start(),
            ThreadWithValue(target=getImagePositionRegion, args=(C.ARENA_SELECT_NEW_DRAGON_BTN, 0, 740, 1600, 830, .8, 1)).start(),
        ]
        swap_btn = swap_btn.join()
        select_new_dragon_btn = select_new_dragon_btn.join()
        moveTo([random.randrange(100, 1500), random.randrange(100, 700)])
        if exists(swap_btn):
            return
            # moveAndClick(swap_btn)
            # return moveAndClick(_get_select_new_dragon_btn())
        if exists(select_new_dragon_btn):
            return moveAndClick(select_new_dragon_btn)
    
def inside_arena():
    check_attack_report()
    check_if_can_fight()
    check_and_collect()
    moveTo([random.randrange(100, 1500), random.randrange(100, 700)])

    fight = getImagePositionRegion(C.ARENA_FIGHT, 740, 730, 870, 800, 0.8, 20)

    if not exists(fight): 
        closePopup()
        return print('No fight button found')
    moveAndClick(fight)
    _prepare_dragons_for_fight()
    freeze_dragons()
    claim_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, 700, 750, 900, 850, .8, 10)
    moveAndClick(claim_btn, 'No arena claim button')
    if is_application_crashed():
        return open_app()
    return inside_arena()

def is_application_crashed():
    ahk = AHK()

    win = ahk.win_get(title='Dragon City')
    return win is None