from utils import ThreadWithReturnValue, checkIfCanClaim, delay, exists, getImagePositionRegion, moveAndClick, closePopup, closeVideo, video_error

def getRewards():
    ## TODO update the starting position
    thread1 = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/play_video.png', 800, 300, 1400, 800)).start()
    thread2 = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/claim.png', 300, 500, 1000, 800)).start()
    video = thread1.join()
    greenClaim = thread2.join()
    if not exists(video):
        return print('Video not found ')

    moveAndClick(video)
    delay(1)
    if not exists(video_error()): 
        moveAndClick([802, 352]) # position to play the video
        checkIfCanClaim()
        closeVideo()
    else: 
        delay(1)
        moveAndClick(greenClaim, 'Claim button for rewards after battle not found')
    claim_btn_league_finished = getImagePositionRegion('./img/battle/claim.png', 600, 600, 1000, 800, .8, 5)
    if exists(claim_btn_league_finished):
        moveAndClick(claim_btn_league_finished)
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


def goToFight(pos=[-1]):
    attack = getImagePositionRegion('./img/battle/attacks/play.png', 50, 100, 110, 210,.8, 100)
    moveAndClick(attack)
    if exists(pos):
        moveAndClick(pos)

    in_progress = getImagePositionRegion('./img/battle/fight_in_progress.png', 0, 100, 190, 300, .8, 5)
    while exists(in_progress):
        print('Fight in progress')
        in_progress = getImagePositionRegion('./img/battle/fight_in_progress.png', 0, 100, 190, 300, .8, 5)
        delay(1)

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
    delay(1)
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