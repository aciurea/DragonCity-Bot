from freeze import freeze_dragons
from utils import (ThreadWithReturnValue, checkIfCanClaim,
                closePopup,
                closeVideo, 
                delay,
                exists,
                get_path as get_path_from_utils,
                getImagePositionRegion,
                moveAndClick,
                openChest)

BASE_ARENA = './img/battle/arenas/' 

def get_path(path):
    return get_path_from_utils(BASE_ARENA+path)

def check_attack_report():
    threads = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_path('attack_report'), 780, 180, 940, 270, .8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_path('close_attack_report'), 1190, 180, 1270, 280, .8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_path('attack_report_accept'), 550, 550, 1000, 670, .8, 3)).start()
    ]

    repeal = ThreadWithReturnValue(target=getImagePositionRegion,args=(get_path('repeal'), 550, 550, 1100, 750, .8, 3)).start()
    repeal = repeal.join()

    if exists(repeal):
        moveAndClick(repeal)
        checkIfCanClaim()
        closeVideo()
        return
    
    for thread in threads:
        img = thread.join()
        print(img)
        if exists(img):
            moveAndClick(img)

def check_if_can_fight():
    cannot_fight = getImagePositionRegion(get_path('wait_time'),180, 380, 790, 490, .8, 3)

    if not exists(cannot_fight):
        return print('Battle can start')
    delay(.5)
    change = getImagePositionRegion(get_path('change_dragon'), 375, 670, 590 ,760, .8, 3)

    if not exists(change):
        return print('Change button not found.')
    moveAndClick(change)
    delay(1)
    
    # try 3 times for 3 dragons
    list = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_path('speed'), 280, 620, 680, 720, .8, 20)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_path('speed'), 800, 620, 1020, 720, .8, 20)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_path('speed'), 1300, 620, 1530, 720, .8, 20)).start(),
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
    collect= getImagePositionRegion(get_path('collect'), 1015, 125, 1200, 200, .8, 3)

    if exists(collect):
        moveAndClick(collect)
        openChest()

def arena():
    delay(1)
    if not exists(getImagePositionRegion(get_path('arenas_quest'), 1000, 120, 1200, 220)): 
        return print('No arena found')
   
    arena_btn = [1100, 400]; # We should calculate in percentages
    moveAndClick(arena_btn)
    delay(2)
    check_attack_report()
    check_if_can_fight()
    check_and_collect()

    # skip = getImagePositionRegion(get_path('gold'), 1000, 665, 1250, 760)
    # if exists(skip):
    #     moveAndClick(skip)
    #     delay(1)
    fight = getImagePositionRegion(get_path('fight'), 740, 730, 870, 800)

    if not exists(fight): 
        closePopup()
        return print('No fight button found')
    moveAndClick(fight)

    def start_figthing():
        swap = getImagePositionRegion(get_path('swap'), 80, 650, 305, 740, .8, 10)

        moveAndClick(swap)

        delay(1)
        select_new_dragon = getImagePositionRegion(get_path('new_dragon'), 600, 730, 1520, 830, .8, 10)
        if not exists(select_new_dragon): return print('Select new Dragon Btn not found')
        moveAndClick(select_new_dragon)
    
        attack = getImagePositionRegion('./img/battle/attacks/play.png', 50, 100, 110, 210,.8, 100)
        moveAndClick(attack)

    delay(.5)
    freeze_dragons(start_figthing)

    claim_btn = getImagePositionRegion(get_path('claim'), 740, 750, 890, 850)
    print(claim_btn)
    if(exists(claim_btn)):
        moveAndClick(claim_btn)
    delay(1)
    closePopup()
