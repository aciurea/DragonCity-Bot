import ctypes
from mem_edit import Process

from utils import delay, exists, get_inprogress, moveTo

def get_addresses(value):
    pid = Process.get_pid_by_name('DragonCity.exe')
    addrs = []
    with Process.open_process(pid) as p:
        addrs = p.search_all_memory(ctypes.c_int32(value))
        return [addrs, p]

def nothing():
    print()

def keep_frozen(p, list, i = 0):
    in_progress = get_inprogress()
    
    if not exists(in_progress): return print('Arena fight finished')
    moveTo([100*i, 100*i])
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
        addrs = p.search_all_memory(ctypes.c_int32(106724))
        seal_values(p, addrs, 0)
        start_fighting()
        keep_frozen(p, addrs, 0)

def seal_values(p, addrs, i = 0):
    if(i > len(addrs) -1): return
    p.write_memory(addrs[i], ctypes.c_int32(900000))
    return seal_values(p, addrs, i+1)
