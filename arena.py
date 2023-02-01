from freeze import freeze_dragons
from open import open_app
from utils import (ThreadWithValue,
                checkIfCanClaim,
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

def _check_and_collect():
    collect= getImagePositionRegion(C.ARENA_CHEST_COLLECT, 1015, 125, 1200, 200, .8, 3)

    if exists(collect):
        moveAndClick(collect)
        openChest()

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
        [C.ARENA_SELECT_NEW_DRAGON_BTN, 0, 740, 1600, 830, .8, 1]
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
    claim_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, 700, 750, 900, 850, .8, 10)
    moveAndClick(claim_btn, 'No arena claim button')
    if is_application_crashed():
        return open_app()
    return inside_arena()

def is_application_crashed():
    ahk = AHK()

    win = ahk.win_get(title='Dragon City')
    return win is None