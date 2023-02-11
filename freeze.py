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
import time
import datetime

def log_arena_fights(messages, fileName = "arena"):
    try:
        f = open(f"temp/{fileName}.txt", "a")
        for message in [f'At: {datetime.datetime.now().strftime("%X")}', *messages]:
            f.write(f'{message} \n')
        f.close()
    except: print('Failed to write to file')

def has_the_opponent_attacked():
    st = time.time()
    print('check if the opponent attacked')
    while(time.time() - st < 10 or not exists(getImagePositionRegion(C.BATTLE_ATTACK_IS_AVAILABLE, 1330, 750, 1425,850, .8, 1))):
        new_dragon_btn = getImagePositionRegion(C.ARENA_SELECT_NEW_DRAGON_BTN, 0, 700, 1600, 850, .8, 1)
        if exists(new_dragon_btn):
            print('The oponent finished attacking..')
            return moveAndClick(new_dragon_btn)
        delay(.5)
    print('No oponent to attack: Might need to check_if_I_Can_close??')

def _get_new_dragon_btn(x1 = 640, x2 = 1440):
    return getImagePositionRegion(C.ARENA_SELECT_NEW_DRAGON_BTN, x1, 740, x2, 810, .8, 5)

def _prepare_best_dragon():
    pos = [[640, 920], [1170, 1440]]
    best_values = []

    try:
        if(not exists(_get_new_dragon_btn())):
            best_values.append({"value":  get_text(), "pos": [140, 380]}) # first dragon
        
        for item in pos:
            swap_btn = getImagePositionRegion(C.FIGHT_SWAP_DRAGON, 80, 645, 310, 745, .8, 1)
            moveAndClick(swap_btn, 'Swap button not available')
            delay(.2)
            new_dragon_btn = _get_new_dragon_btn(*item)
            if not exists(new_dragon_btn): continue
            moveAndClick(new_dragon_btn)
            delay(2)
            best_values.append({"value": get_text(), "pos": item})

        best_values.sort(reverse=True,key=lambda item: item["value"])
        log_arena_fights([
            f'Dragon values are: {repr(best_values)} \n'
        ])
        moveAndClick(getImagePositionRegion(C.FIGHT_SWAP_DRAGON, 80, 645, 310, 745, .8, 1))
        _new_dragon_btn = _get_new_dragon_btn(*best_values[0]["pos"])
        if not exists(_new_dragon_btn): closePopup()
        else: moveAndClick(_new_dragon_btn)
    
        return best_values[0]["value"]
    except: return None

def _swap_dragon():
    moveAndClick(getImagePositionRegion(C.FIGHT_SWAP_DRAGON, 80, 645, 310, 745, .8, 1), 'Swap button not available')
    moveAndClick(_get_new_dragon_btn(0, 1600), 'New Dragon button not available')

def freeze_dragons():
    print('Freeze_dragons')
    attack = getImagePositionRegion(C.FIGHT_PLAY, 50, 100, 110, 210, .8, 100)
    attack = attack if (exists(attack)) else [78, 170]
    text = _prepare_best_dragon()
    _freeze_dragons(777_777, text)
    # Some dragons don't do damage and the value doesn't get updated.
    # _swap_dragon() 
    # _prepare_best_dragon()
    for _ in range(2):
        moveAndClick(attack) # start the fight
        delay(.2)
        moveAndClick(attack) # pause the fight in order to give the change to opponent to hit
        has_the_opponent_attacked()
    _freeze_dragons(99_999_999)
    moveAndClick(attack) # resume fight
    _prevent_sleep()


def _freeze_dragons(lock_value, text = None):
    print('Trying to freeze the dragons')
    value = get_text() if text == None else text
    pid = Process.get_pid_by_name('DragonCity.exe')
    with Process.open_process(pid) as p:
        addrs = p.search_all_memory(ctypes.c_int32(value))
        print(f'for dragon:[{value}] found [{len(addrs)}]  lock_value [{lock_value}]')
        for addr in addrs:
            p.write_memory(addr, ctypes.c_int32(lock_value))

def _prevent_sleep():
    st = time.time()
    while exists(get_in_progress()) and time.time() - st < 300:
        # move mouse because of long battle that can turn off the display and the game will stop
        moveTo([random.randrange(100, 1600), random.randrange(0, 500)])
        delay(10)

