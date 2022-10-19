from league import goToFight
from utils import closePopup, commonClaim, delay, exists, moveAndClick, getImagePosition


def exitHeroic():
    back = getImagePosition('./img/fails/back.png')
    moveAndClick(back)
    closePopup()


def fightHeroic(fight):
    moveAndClick(fight)
    select = getImagePosition('./img/heroic/select.png')
    moveAndClick(select)
    dragon = getImagePosition('./img/heroic/dragon.png')
    moveAndClick(dragon)
    ok = getImagePosition('./img/heroic/ok.png', 3)
    moveAndClick(ok)
    delay(5)
    goToFight()


def findMission():
    # update here with all the missions
    missions = [['./img/heroic/breed.png', 'breed'],
                ['./img/heroic/food.png', 'food'],
                ['./img/heroic/hatch.png', 'hatch'],
                ]
    for mission in missions:
        image = getImagePosition(mission[0], 3, 0.9)
        if exists(image):
            return mission[1]
    return -1


def checkIfCanClaim():
    paths = ['./img/heroic/no_claim2.png', './img/heroic/no_claim.png']
    for path in paths:
        noClaim = getImagePosition(path, 3)
        if exists(noClaim):
            return print('Nothing to claim')

    claim = getImagePosition('./img/heroic/claim.png', 3)

    moveAndClick(claim)
    commonClaim()


def heroic():
    island = getImagePosition('./img/heroic/heroic_arena.png', 3)

    if not exists(island):
        return print('No Heroic Island found')

    moveAndClick(island)
    checkIfCanClaim()
    mission = findMission()

    enterFightBtn = getImagePosition('./img/heroic/fight.png', 3)

    if not exists(enterFightBtn):
        print('No fight')
        closePopup()
        return mission

    moveAndClick(enterFightBtn)
    noFight = getImagePosition('./img/heroic/not_ready_yet.png')

    if exists(noFight):
        exitHeroic()
        return mission

    startFight = getImagePosition('./img/heroic/start_fight.png')

    if exists(startFight):
        fightHeroic(startFight)

    exitHeroic()
    return mission
