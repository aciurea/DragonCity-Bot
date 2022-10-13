import time
from utils import checkIfCanClaim, getImagePosition, moveAndClick, closePopup, closeVideo


def getRewards():
    video = getImagePosition('./img/battle/play_video.png')

    if (video[0] == -1):
        return print('Video not found ', video)

    moveAndClick(video)
    checkIfCanClaim()
    closeVideo()
    closePopup()


def getAttacks():
    # TODO improve attacks
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

    return [-1, -1]


def goToFight():
    oponentHitTime = 5
    attack = getAttacks()

    if (attack[0] != -1):
        moveAndClick(attack)
        time.sleep(oponentHitTime)  # wait for the oponent to hit
        return goToFight()

    selectDragonBtn = getImagePosition('./img/battle/select_new_dragon.png')
    if (selectDragonBtn[0] != -1):
        moveAndClick()
        return goToFight()


def goToLeague():
    noMoreBattles = getImagePosition('./img/battle/no_new_combats.png')

    if (noMoreBattles[0] != -1):
        print('No More battle available. Close the popup')
        return closePopup()  # close the no More Battle

    oponent = getImagePosition('./img/battle/league_oponent.png')

    if (oponent[0] == -1):
        return print('League Openent not found')

    moveAndClick(oponent)
    goToFight()
    print('Battle finished since I have no attacks, go and take the rewards')
    getRewards()


def openLeaguePanel():
    league = getImagePosition('./img/battle/league.png')

    if (league[0] == -1):
        return print('League button not found!')

    moveAndClick(league)
    goToLeague()
