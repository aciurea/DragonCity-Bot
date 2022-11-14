from freeze import freeze_dragons
from utils import (ThreadWithReturnValue, checkIfCanClaim,
                closePopup,
                closeVideo, 
                delay,
                exists,
                getImagePositionRegion,
                moveAndClick,
                openChest)
import constants as C

def check_attack_report():
    threads = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.ARENA_ATTACK_REPORT, 780, 180, 940, 270, .8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.ARENA_CLOSE_ATTACK_REPORT, 1190, 180, 1270, 280, .8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.ARENA_ATTACK_REPORT_ACCEPT, 550, 550, 1000, 670, .8, 3)).start()
    ]

    repeal = ThreadWithReturnValue(target=getImagePositionRegion,args=(C.ARENA_REPEAL, 550, 550, 1100, 750, .8, 3)).start()
    repeal = repeal.join()

    if exists(repeal):
        moveAndClick(repeal)
        checkIfCanClaim()
        closeVideo()
        delay(1)
        return
    
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
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.ARENA_SPEED_UP, 280, 620, 680, 720, .8, 20)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.ARENA_SPEED_UP, 800, 620, 1020, 720, .8, 20)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(C.ARENA_SPEED_UP, 1300, 620, 1530, 720, .8, 20)).start(),
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
    check_attack_report()
    check_if_can_fight()
    check_and_collect()
    delay(1)

    fight = getImagePositionRegion(C.ARENA_FIGHT, 740, 730, 870, 800)

    if not exists(fight): 
        closePopup()
        return print('No fight button found')
    moveAndClick(fight)

    def start_fighting():
        print('start to fight in arena')
        swap = getImagePositionRegion(C.FIGHT_SWAP_DRAGON, 80, 650, 305, 740, .8, 10)

        moveAndClick(swap)

        delay(1)
        select_new_dragon = getImagePositionRegion(C.ARENA_SELECT_NEW_DRAGON_BTN, 600, 730, 1520, 830, .8, 20)
        if not exists(select_new_dragon): return print('Select new Dragon Btn not found')
        moveAndClick(select_new_dragon)
    
        attack = getImagePositionRegion(C.FIGHT_PLAY, 50, 100, 110, 210,.8, 100)
        moveAndClick(attack)

    delay(.5)
    freeze_dragons(start_fighting)
    delay(3)
    claim_btn = getImagePositionRegion(C.ARENA_CLAIM_BTN, 700, 750, 900, 850, .8, 20)
    moveAndClick(claim_btn, 'No arena claim button')
    delay(3)
    closePopup()
