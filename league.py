from utils import ThreadWithReturnValue, checkIfCanClaim, delay, getImagePosition, exists, getImagePositionRegion, moveAndClick, closePopup, closeVideo, moveTo, video_error

def getRewards():
    ## TODO update the starting position
    thread1 = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/play_video.png', 800, 300, 1400, 800))
    thread2 = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/claim.png', 300, 500, 1000, 800))
    thread1.start()
    thread2.start()
    video = thread1.join()
    if not exists(video):
        return print('Video not found ')

    moveAndClick(video)
    delay(5)
    if not exists(video_error()): 
        checkIfCanClaim()
        closeVideo()
    else: 
        greenClaim = thread2.join()
        delay(1)
        moveAndClick(greenClaim, 'Claim button for rewards after battle not found')
    image = getImagePositionRegion('./img/battle/claim.png', 600, 600, 1000, 800)
    moveAndClick(image, 'Claim after league finished')
    delay(1)
    closePopup()

    
def sortFirst(val): return val[0]

def getStrongAttacks(avoid, attacks):
    if not exists(avoid): return attacks

    newAttacks = []
    threshold = 120
  
    for attack in attacks:
        if (abs(attack[0] - avoid[0]) > threshold):
            newAttacks.append(attack)
    return newAttacks


def goToFight():
    attack = getImagePositionRegion('./img/battle/attacks/play.png', 50, 100, 110, 210,.8, 100)
    moveAndClick(attack)

    in_progress = getImagePositionRegion('./img/battle/fight_in_progress.png', 0, 0, 120, 350)
    while exists(in_progress):
        print('Fight in progress')
        delay(3)
        in_progress = getImagePositionRegion('./img/battle/fight_in_progress.png', 0, 0, 120, 350)

def goToLeague():
    # League is positioned in the first half of the screen on the right hand side,so the rest can be skipped
    list = [ 
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/no_new_combats.png', 1200, 100, 1600, 300)),
        ThreadWithReturnValue(target=getImagePositionRegion,args=('./img/battle/refill.png', 1100, 100, 1600, 400)),
    ]
    for thread in list:
        thread.start()
    thread2 = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/league_oponent.png', 0, 300, 1600, 800))
    thread2.start()
    
    for thread in list:
        noMoreBattles = thread.join()
        if exists(noMoreBattles):
            print('No More battle available. Close the popup')
            return closePopup()

    oponent = thread2.join()

    if not exists(oponent):
        return print('League Openent not found')

    moveAndClick(oponent)
    delay(5) # wait for the battle to start
    goToFight()
    print('Battle finished since I have no attacks, go and take the rewards')
    return getRewards()


def openLeaguePanel():
    league = getImagePositionRegion('./img/battle/league.png', 350, 250, 600, 450)

    if not exists(league):
        return print('League button not found!')

    print('Start league battle...')
    moveAndClick(league)
    delay(1)
    goToLeague()

def start():
    while True:
        goToFight()
        print('fight finished')
        delay(5)

# start()