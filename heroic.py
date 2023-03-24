from league import goToFight
from utils import ThreadWithValue, closePopup, delay, exists, getImagePositionRegion, go_back, moveAndClick, getImagePosition, openChest
import constants as C
import concurrent.futures

def exit_heroic():
    go_back()
    delay(.5)
    closePopup()

# TODO optimize the position to have fast searches
def fight_heroic(fight):
    moveAndClick(fight)
    select = getImagePositionRegion(C.HEROIC_SELECT_BTN, 0, 0, 700, 700, 0.8)
    moveAndClick(select)
    dragon = getImagePosition(C.HEROIC_DRAGON)
    moveAndClick(dragon)
    ok = getImagePosition(C.HEROIC_OK, 3)
    moveAndClick(ok)
    delay(5)
    goToFight()


def filter_completed(items):
    delta = 50
    if len(items) == 0: return items

    missions = []
    for item in items:
        _, height = item[0]
    
        if not exists(getImagePositionRegion(C.HEROIC_COMPLETED, 1000, height - 10, 1600, height+delta, 0.8, 2)):
            missions.append(item[1])
    return missions

def find_missions():
    items = [
        [[C.HEROIC_FOOD, 1090, 225, 1270, 725, .8, 3], 'food'],
        [[C.HEROIC_BREED, 1090, 225, 1270, 725, .8, 3], 'breed'],
        [[C.HEROIC_HATCH, 1090, 225, 1270, 725, .8, 3],'hatch'],
        [[C.HEROIC_FEED, 1090, 225, 1270, 725, .8, 3],  'feed']
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        items = executor.map(lambda args: [getImagePositionRegion(*(args[0])), args[1]], items)
        items = list(filter(lambda args: exists(args[0]), items))
 
        # items = filter_completed(items)
        # print(items)
        # return items
    # [[[1157, 402], 'food'], [[1171, 284], 'feed']]
        return list(map(lambda args: args[1], items))


def check_if_can_claim():
    no_claim_threads = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.HEROIC_NO_CLAIM_BTN_2, 1100,690, 1430, 760, 0.8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.HEROIC_NO_CLAIM_BTN_1, 1100,690, 1430, 760, 0.8, 3)).start()
    ]

    for thread in no_claim_threads:
        no_claim_img = thread.join()
        if exists(no_claim_img):
            return print('Nothing to claim')

    claim = getImagePositionRegion(C.HEROIC_GREEN_CLAIM_BTN, 652, 700, 950, 800, .8, 3)
    if exists(claim):
        moveAndClick(claim)
        openChest()

def heroic_race():
    island = getImagePosition(C.HEROIC_ARENA, 3)
    if not exists(island):
        print('No Heroic Island found')
        return []

    delay(.5)
    moveAndClick([island[0]+20, island[1]+ 10])
    check_if_can_claim()
    enter_fight_thread = ThreadWithValue(target=getImagePositionRegion, args=(C.HEROIC_FIGHT, 1260, 250, 1450, 735, .8, 3)).start()
    missions = find_missions()
    enter_fight = enter_fight_thread.join()

    if not exists(enter_fight):
        print('No fight')
        closePopup()
        return missions

    moveAndClick(enter_fight)
    delay(1)
    no_fight, start_fight = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.HEROIC_NOT_READY, 0, 580, 1600, 740, .8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.HEROIC_START_FIGHT_BTN, 0, 640, 1600, 760, .8, 3)).start(),
        ]

    no_fight = no_fight.join()
    if exists(no_fight):
        exit_heroic()
        return missions

    start_fight = start_fight.join()
    if exists(start_fight):
        fight_heroic(start_fight)
    check_if_can_claim()
    exit_heroic()
    return missions
