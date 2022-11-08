import ctypes
from mem_edit import Process

from utils import delay, exists, get_text, getImagePositionRegion, moveAndClick

def get_addresses(value):
    pid = Process.get_pid_by_name('DragonCity.exe')
    addrs = []
    with Process.open_process(pid) as p:
        addrs = p.search_all_memory(ctypes.c_int32(value))
        return [addrs, p]

def nothing():
    print()

def keep_frozen(p, list, i = 0):
    in_progress = getImagePositionRegion('./img/battle/fight_in_progress.png', 0, 100, 190, 300, .8, 5)
    
    if not exists(in_progress): return print('Arena fight finished')
    
    if(i > len(list) -1):
        delay(.5)
        return keep_frozen(p, list, 0)
    p.write_memory(list[i], ctypes.c_int32(900000))
    delay(.5)
    return keep_frozen(p, list, i+1)

def freeze_dragons(start_fighting):
    pid = Process.get_pid_by_name('DragonCity.exe')
    addrs = []
    with Process.open_process(pid) as p:
        addrs = p.search_all_memory(ctypes.c_int32(255854))
        seal_values(p, addrs, 0)
        start_fighting()
        keep_frozen(p, addrs, 0)

def seal_values(p, addrs, i = 0):
    if(i > len(addrs) -1): return
    p.write_memory(addrs[i], ctypes.c_int32(900000))
    return seal_values(p, addrs, i+1)
