import ctypes
from mem_edit import Process
import constants as C
from utils import (
    closePopup,
    delay,
    exists,
    get_in_progress,
    get_text,
    getImagePositionRegion,
    moveAndClick,
    moveTo,
    )
import random

def _is_dragon_ready(): 
    while(not exists(getImagePositionRegion(C.BATTLE_ATTACK_IS_AVAILABLE, 1330, 750, 1425,850, .8, 1))):
        delay(.1)

def has_the_opponent_attacked():
    print('check if the opponent attacked')
    while(not exists(getImagePositionRegion(C.BATTLE_ATTACK_IS_AVAILABLE, 1330, 750, 1425,850, .8, 1))):
        new_dragon_btn = getImagePositionRegion(C.ARENA_SELECT_NEW_DRAGON_BTN, 0, 740, 1600, 830, .8, 1)
        if exists(new_dragon_btn): return moveAndClick(new_dragon_btn)
        delay(.5)
    print('The oponent finished attacking..')

def _get_new_dragon_btn(x1 = 640, x2 = 1440):
    return getImagePositionRegion(C.ARENA_SELECT_NEW_DRAGON_BTN, x1, 740, x2, 810, .8, 5)

def _prepare_best_dragon():
    pos = [[650, 920], [1170, 1440]]
    best_values = []

    try:
        if(not exists(_get_new_dragon_btn())):
            best_values.append({"value":  get_text(), "pos": [140, 380]}) # first dragon
        
        for item in pos:
            swap_btn = getImagePositionRegion(C.FIGHT_SWAP_DRAGON, 80, 645, 310, 745, .8, 1)
            moveAndClick(swap_btn, 'Swap button not available')
            delay(.2)
            new_dragon_btn = _get_new_dragon_btn(*item)
            if not exists(new_dragon_btn): return None
            moveAndClick(new_dragon_btn)
            delay(2)
            best_values.append({"value": get_text(), "pos": item})

        best_values.sort(reverse=True,key=lambda item: item["value"])
        moveAndClick(getImagePositionRegion(C.FIGHT_SWAP_DRAGON, 80, 645, 310, 745, .8, 1))
        _new_dragon_btn = _get_new_dragon_btn(*best_values[0]["pos"])
        if not exists(_new_dragon_btn): closePopup()
        else: moveAndClick(_new_dragon_btn)
    
        return best_values[0]["value"]
    except: return None

def freeze_dragons():
    attack = getImagePositionRegion(C.FIGHT_PLAY, 50, 100, 110, 210, .8, 100)
    _prepare_best_dragon()
    _freeze_dragons(777_777)
    moveAndClick(attack) # start the fight
    delay(.2)
    moveAndClick(attack) # pause the fight in order to give the change to opponent to hit
    has_the_opponent_attacked()
    _freeze_dragons(99_999_999)
    moveAndClick(attack) # resume fight
    _prevent_sleep()


def _freeze_dragons(lock_value):
    value = get_text()
    pid = Process.get_pid_by_name('DragonCity.exe')
    with Process.open_process(pid) as p:
        addrs = p.search_all_memory(ctypes.c_int32(value))
        print(f'for dragon:[{value}] found [{len(addrs)}]')
        for addr in addrs:
            p.write_memory(addr, ctypes.c_int32(lock_value))

def _prevent_sleep():
    while exists(get_in_progress()):
        # move mouse because of long battle that can turn off the display and the game will stop
        moveTo([random.randrange(100, 1600), random.randrange(0, 500)])
        delay(10)

