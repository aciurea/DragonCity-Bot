from utils import checkIfCanClaim, delay, getImagePosition, exists, getImagePositionRegion, moveAndClick, closePopup, closeVideo


def getRewards():
    print('Go to take the rewards')
    video = getImagePositionRegion('./img/battle/play_video.png', 800, 300, 1400, 800) # play video it's in the middle

    if not exists(video):
        return print('Video not found ')

    moveAndClick(video)
    checkIfCanClaim()
    closeVideo()
    # TODO need to check the claim, happens when oponents are defetead
    greenClaim = getImagePosition('./img/tv/green_claim.png')
    moveAndClick(greenClaim)
    yellowClaim = getImagePosition('./img/fails/claim_yellow.png', 5)
    moveAndClick(yellowClaim)
    return closePopup()


def getAttacks():
    # TODO improve attacks, take screenshot with all the attacks and add them in order
    # Attacks should also be considered after the critical attack
    # Avoid no damage attacks or low damage attacks
    # TODO try to use multithreading to read fast the attacks and choose the best one
    paths = [
        './img/battle/attacks/legend.png',
        './img/battle/attacks/pure_energy.png',
    ]

    for path in paths:
        attack = getImagePositionRegion(path, 1000, 0, 1600, 900, 3) # attaks are at the bottom of the page, try only 2 times to find the attack
        if exists(attack):
            return attack
    return [-1]


def goToFight():
    attack = getAttacks()

    if exists(attack):
        moveAndClick(attack)
        print('Attacked with', attack)
        delay(1) # wait for the victory logo to have a chance to appear
        # TODO check if victory
        victory = getImagePositionRegion('img with victory is on top middle screen', 500, 0, 1000, 450) # img with vicotry is on top middle screen
        if exists(victory):
            return print('Victory!!!')
        return goToFight()

    selectDragonBtn = getImagePositionRegion('./img/battle/select_new_dragon.png', 400, 400, 1600, 800) # Usually is at the botttom of the screen
    if exists(selectDragonBtn):
        moveAndClick(selectDragonBtn)
        print('New Dragon Selected')
        delay(2) # wait for the dragon to have a change to appear
        return goToFight()
    return -1


def goToLeague():
    # League is positioned in the first half of the screen on the right hand side,so the rest can be skipped
    noMoreBattles = getImagePositionRegion('./img/battle/no_new_combats.png', 900, 0, 1600, 450)

    if exists(noMoreBattles):
        print('No More battle available. Close the popup')
        return closePopup()

    oponent = getImagePosition('./img/battle/league_oponent.png')

    if not exists(oponent):
        return print('League Openent not found')

    moveAndClick(oponent)
    goToFight()
    print('Battle finished since I have no attacks, go and take the rewards')
    return getRewards()


def openLeaguePanel():
    league = getImagePositionRegion('./img/battle/league.png', 0, 0, 900, 450)# end in the middle of the screen
    
    if not exists(league):
        return print('League button not found!')

    print('Start league battle...')
    moveAndClick(league)
    goToLeague()
