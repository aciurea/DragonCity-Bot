from league import goToFight
from utils import ThreadWithReturnValue, closePopup, delay, exists, getImagePositionRegion, go_back, moveAndClick, getImagePosition, openChest


def exit_heroic():
    go_back()
    delay(.5)
    closePopup()


def fight_heroic(fight):
    moveAndClick(fight)
    select = getImagePosition('./img/heroic/select.png')
    moveAndClick(select)
    dragon = getImagePosition('./img/heroic/dragon.png')
    moveAndClick(dragon)
    ok = getImagePosition('./img/heroic/ok.png', 3)
    moveAndClick(ok)
    delay(5)
    goToFight()


def find_missions():
    threads = [
        [ThreadWithReturnValue(target=getImagePositionRegion, 
        args=('./img/heroic/food.png', 1090, 225, 1270, 725, .8, 3)).start(), 'food'],
        [ThreadWithReturnValue(target=getImagePositionRegion, 
        args=('./img/heroic/breed.png', 1090, 225, 1270, 725, .8, 3)).start(), 'breed'],
        [ThreadWithReturnValue(target=getImagePositionRegion, 
        args=('./img/heroic/hatch.png', 1090, 225, 1270, 725, .8, 3)).start(), 'hatch'],
        [ThreadWithReturnValue(target=getImagePositionRegion,args=('./img/heroic/feed.png', 1090, 225, 1270, 725, .8, 3)).start(), 'feed']
        ]

    missions = []
    for mission_thread in threads:
        thread, mission_type = mission_thread
        mission = thread.join()
        if exists(mission):
            missions.append(mission_type)
    return missions


def check_if_can_claim():
    no_claim_threads = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/heroic/no_claim2.png', 1100,690, 1430, 760, 0.8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/heroic/no_claim.png', 1100,690, 1430, 760, 0.8, 3)).start()
    ]

    for thread in no_claim_threads:
        no_claim_img = thread.join()
        if exists(no_claim_img):
            return print('Nothing to claim')

    claim = getImagePositionRegion('./img/heroic/claim.png', 652, 700, 950, 800, .8, 3)
    if exists(claim):
        moveAndClick(claim)
        openChest()

def heroic_race():
    island = getImagePosition('./img/heroic/heroic_arena.png', 3)
    enter_fight_thread = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/heroic/fight.png', 1260, 285, 1435, 735, .8, 3)).start()

    if not exists(island):
        print('No Heroic Island found')
        return []

    delay(.5)
    moveAndClick(island)
    check_if_can_claim()
    missions = find_missions()

    enter_fight = enter_fight_thread.join()

    if not exists(enter_fight):
        print('No fight')
        closePopup()
        return missions

    moveAndClick(enter_fight)
    delay(1)
    no_fight, start_fight = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/heroic/not_ready_yet.png', 0, 580, 1600, 740, .8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/heroic/start_fight.png', 0, 640, 1600, 760, .8, 3)).start(),
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
