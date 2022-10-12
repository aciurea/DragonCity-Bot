import time
from utils import getImagePosition, moveAndClick, closePopup, closeVideo


def getReward():
    timeToEndTheVideo = 55
    video = getImagePosition('./img/battle/play_video.png')

    if (video[0] == -1):
        return print('Video not found ', video)

    moveAndClick(video)
    time.sleep(timeToEndTheVideo)
    closeVideo()


def getAttacks():
    # Attacks should also be considered after the critical attack
    # Avoid no damage attacks or low damage attacks
    paths = [
        './img/battle/attacks/legend.png',
        './img/battle/attacks/pure_energy.png',
        './img/battle/attacks/leech_plants.png',
        './img/battle/attacks/out_of_time.png',
    ]

    for path in paths:
        attack = getImagePosition(path)
        if (attack[0] != -1):
            return attack
        continue
    return -1


def fight():
    # Need to check the attacks
    oponentHitTime = 10
    attack = getAttacks()

    # search for multiple attacks
    if (attack[0] == -1):
        selectDragonBtn = getImagePosition(
            './img/battle/select_new_dragon.png')
        if (selectDragonBtn[0] == -1):
            print('Battle finished since I have no attacks')
            return getReward()
        else:
            moveAndClick(selectDragonBtn)
            return fight()

    moveAndClick(attack)
    time.sleep(oponentHitTime)  # wait for the oponent to hit
    fight()


def openLeague(battles=0):
    maxNumberOfBattles = 5
    if (battles == maxNumberOfBattles):
        return

    noMoreBattles = getImagePosition('./img/battle/no_new_combats.png')

    if (noMoreBattles[0] != -1):
        print('No More battle available. Close the popup')
        return closePopup()  # close the no More Battle

    league = getImagePosition('./img/battle/league_oponent.png')

    if (league[0] == -1):
        return print('League Openent not found')

    moveAndClick(league)
    fight()
    openLeague(battles + 1)  # battle again


def openBattlePanel():
    league = getImagePosition('./img/battle/league.png')

    if (league[0] == -1):
        return print('League button not found!')

    moveAndClick(league)
    openLeague()


def openBottomMenu():
    battleBtn = getImagePosition('./img/battle/battle_btn.png')
    print(123, battleBtn[0], battleBtn[1], battleBtn[0] == -1)
    if (battleBtn[0] == -1):
        return print('Battle Button not found')

    moveAndClick(battleBtn)
    openBattlePanel()


def start():
    print('Start to battle...')
    while (True):
        centerIsland = getImagePosition('./img/utils/center_island.png')
        if (centerIsland[0] == -1):
            return print('Center not found. Cannot continue')
        moveAndClick(centerIsland)
        openBottomMenu()
        time.sleep(20)


start()
