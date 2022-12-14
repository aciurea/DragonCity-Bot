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



def freeze_dragons():
    attack = getImagePositionRegion(FIGHT_PLAY, 50, 100, 110, 210, .8, 100)
    _freeze_dragons(999_999)
    moveAndClick(attack) # start the fight
    delay(.2)
    moveAndClick(attack) # pause the fight in order to give the change to opponent to hit
    delay(10)
    _freeze_dragons(99_999_999)
    moveAndClick(attack) # resume fight
    _prevent_sleep()


def _freeze_dragons(lock_value):
    pid = Process.get_pid_by_name('DragonCity.exe')
    with Process.open_process(pid) as p:
        delay(1)
        value = get_text()
        print('Arena text is::', value)
        addrs = p.search_all_memory(ctypes.c_int32(value))
        for addr in addrs:
            p.write_memory(addr, ctypes.c_int32(lock_value))
        p.close()

def _prevent_sleep():
    i = 50
    while exists(get_in_progress()):
        i += 10
        moveTo([i, i]) # move mouse because of long battle that can turn off the display and the game will stop
        delay(3)

