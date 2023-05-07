from utils import (check_if_not_ok,
                    delay,
                    exists, get_json_file,
                    getImagePositionRegion,
                    moveAndClick,
                    ThreadWithValue)
import constants as C
import concurrent.futures

from utilss.drag_map import dragMapToCenter, move_to_top

jsonPos = get_json_file('breed.json')

def handle_full_hatchery():
    moveAndClick(jsonPos['closeHatcheryBtnPos'])
    dragMapToCenter()
    moveAndClick(jsonPos['hatcheryPos'])
    click_on_terra_egg()
    sell_egg_from_hatchery()

def place_egg():
    delay(.5)
    moveAndClick(jsonPos['placeBtnPos'])
    dragMapToCenter()
    moveAndClick(jsonPos['terraHabitatPos'])
    delay(.5)
    moveAndClick(getImagePositionRegion(C.BREED_DRAGON, *jsonPos['terraDragonPos']))

def sell_egg_from_habitat():
    delay(1)
    moveAndClick(jsonPos['sellDragonBtnHabitatPos'])
    delay(1)
    moveAndClick(jsonPos['sellBtnConfirmPos'])

def sell_egg_from_hatchery():
    delay(1)
    moveAndClick(jsonPos['sellBtnPos'])
    delay(1)
    moveAndClick(jsonPos['sellBtnConfirmPos'])

def feed_dragon():
    for _ in range(9):
     moveAndClick(jsonPos['feedBtnPos'])
     delay(.1)

def click_on_terra_egg():
    terra_egg_pos = getImagePositionRegion(C.BREED_TERRA_EGG, *jsonPos['terraEggPos'])
    if exists(terra_egg_pos):
        moveAndClick([terra_egg_pos[0], terra_egg_pos[1]+50])

def get_rebreed_or_hatchery():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return executor.map(lambda args: getImagePositionRegion(*args), [
            [C.BREED_RE_BREED_BTN, *jsonPos['rebreedPos']],
            [C.BREED_HATCHERY_FULL, *jsonPos['fullHatcheryPos']],
            [C.BREED_HATCHERY_TEXT, *jsonPos['hatcheryText']]
        ])

def _breed(pos, priority):
    moveAndClick(pos)
    [rebreed_btn, full_hatchery, in_hatchery] = get_rebreed_or_hatchery()
    if exists(rebreed_btn):
        moveAndClick(rebreed_btn)
        delay(1) # it is slow opening the rebreed panel.
        moveAndClick(getImagePositionRegion(C.BREED_BREED_BTN, *jsonPos['breedBtnPos']))
        moveAndClick(jsonPos['closeBtnPos'])
        return False
    if exists(full_hatchery):
        handle_full_hatchery()
    elif in_hatchery or exists(getImagePositionRegion(C.BREED_HATCHERY_TEXT, *jsonPos['hatcheryText'])):
        click_on_terra_egg()
        if priority == 'hatch':
            place_egg()
            sell_egg_from_habitat()
        elif priority == 'breed':
            sell_egg_from_hatchery()
        elif priority == 'feed':
            place_egg()
            feed_dragon()
            sell_egg_from_habitat()
    dragMapToCenter()
    # check_if_not_ok()
    return True

# terra_egg breed takes 12s
# terra_egg hatch takes 15s
# if in hatchery, rebreed_immediatelly
def fast_breed(priority='breed'):
    dragMapToCenter()
    hasHatched = _breed(jsonPos['treePos'], priority)
    if(hasHatched): _breed(jsonPos['treePos'], priority)
    delay(.5)
    _breed(jsonPos['rockPos'], priority)
    delay(.5)
    move_to_top()
    _breed(jsonPos['mountainPos'], priority)
   
    # delay(time_to_delay if time_to_delay > 0 else 0)

def start_clean():
    for _ in range(2):
        dragMapToCenter()
        egg = getImagePositionRegion(C.BREED_FINISH_BREED, *jsonPos['finishBreedPos'])
        if not exists(egg): continue
        _breed(egg, 'breed')

def start():
    start_clean()
    while 1:
        fast_breed(priority='feed')
    

start()
