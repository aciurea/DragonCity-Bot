import time
from utils import checkIfCanClaim, getImagePosition, exists, moveAndClick, closePopup, closeVideo


def getRewards():
    print('Go to take the rewards')
    video = getImagePosition('./img/battle/play_video.png')

    if (video[0] == -1):
        return print('Video not found ')

    moveAndClick(video)
    checkIfCanClaim()
    closeVideo()
    return closePopup()


def getAttacks():
    # TODO improve attacks
    # Attacks should also be considered after the critical attack
    # Avoid no damage attacks or low damage attacks
    paths = [
        './img/battle/attacks/legend.png',
        './img/battle/attacks/pure_energy.png',
    ]

    for path in paths:
        attack = getImagePosition(path)
        if exists(attack):
            return attack

    return [-1, -1]


def goToFight():
    oponentHitTime = 5
    attack = getAttacks()

    if exists(attack):
        print('Attacked with', attack)
        moveAndClick(attack)
        time.sleep(oponentHitTime)  # wait for the oponent to hit
        return goToFight()

    selectDragonBtn = getImagePosition('./img/battle/select_new_dragon.png')
    if exists(selectDragonBtn):
        print('New Dragon Selected')
        moveAndClick(selectDragonBtn)
        time.sleep(oponentHitTime)  # wait for the new dragon to load
        return goToFight()
    return -1


def goToLeague():
    noMoreBattles = getImagePosition('./img/battle/no_new_combats.png')

    if exists(noMoreBattles):
        print('No More battle available. Close the popup')
        return closePopup()  # close the no More Battle

    oponent = getImagePosition('./img/battle/league_oponent.png')

    if (oponent[0] == -1):
        return print('League Openent not found')

    moveAndClick(oponent)
    goToFight()
    print('Battle finished since I have no attacks, go and take the rewards')
    return getRewards()


def openLeaguePanel():
    league = getImagePosition('./img/battle/league.png')

    if (league[0] == -1):
        return print('League button not found!')

    print('Start league battle...')
    moveAndClick(league)
    return goToLeague()
