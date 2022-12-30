import ctypes
from mem_edit import Process
from constants import FIGHT_PLAY
from utils import (
    delay,
    exists,
    get_in_progress,
    get_text,
    getImagePositionRegion,
    moveAndClick,
    moveTo
    )

_VALUE = 99999999

def get_addresses(value):
    pid = Process.get_pid_by_name('DragonCity.exe')
    addrs = []
    with Process.open_process(pid) as p:
        addrs = p.search_all_memory(ctypes.c_int32(value))
        return [addrs, p]

def keep_frozen(p, list, i = 0):
    moveAndClick([500, 500])
    if(i > len(list) -1): return
    p.write_memory(list[i], ctypes.c_int32(_VALUE))
    return keep_frozen(p, list, i+1)

def freeze_dragons():
    pid = Process.get_pid_by_name('DragonCity.exe')
    addrs = []
    delay(1)
    with Process.open_process(pid) as p:
        value = get_text()
        print('Arena text is', value)
        if value > 100000:
            addrs = p.search_all_memory(ctypes.c_int32(value))
            seal_values(p, addrs, 0)

        attack = getImagePositionRegion(FIGHT_PLAY, 50, 100, 110, 210, .8, 100)
        moveAndClick(attack)
        i = 50
        while exists(get_in_progress()):
            i += 10
            moveTo([i, i]) # move mouse because of long battle that can turn off the display and the game will stop
            delay(3)

def seal_values(p, addrs, i = 0):
    if(i > len(addrs) -1): return
    p.write_memory(addrs[i], ctypes.c_int32(_VALUE))
    return seal_values(p, addrs, i+1)
