from utils import ThreadWithReturnValue, checkIfCanClaim, delay, getImagePosition, exists, getImagePositionRegion, moveAndClick, closePopup, closeVideo, moveTo, video_error

def getRewards():
    print('Go to take the rewards')
    thread1 = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/play_video.png', 800, 300, 1400, 800))
    thread2 = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/claim.png', 300, 200, 1200, 700, 0.9, 20))
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
        closePopup()
    else: 
        greenClaim = thread2.join()
        moveAndClick(greenClaim, 'Claim button for rewards after battle not found')
    
    # TODO when the use claims the gems
   # yellowClaim = getImagePosition('./img/fails/claim_yellow.png', 5)
   # moveAndClick(yellowClaim)

    
def sortFirst(val): return val[0]

def getStrongAttacks(avoid, attacks):
    if not exists(avoid): return attacks

    newAttacks = []
    threshold = 120
  
    for attack in attacks:
        if (abs(attack[0] - avoid[0]) > threshold):
            newAttacks.append(attack)
    return newAttacks


def getAttacks():
    common = './img/battle/attacks/'
    paths = [
        {'path': common + 'super.png', 'check': 'critical'},
        {'path': common + 'avoid.png', 'check': 'avoid'},
        {'path': common + 'no_damage.png', 'check': 'avoid'},
        {'path': common + 'legend.png', 'check': 'no'},
        {'path': common + 'deus_attack.png', 'check': 'no'},
        {'path': common + 'archaic_roar.png', 'check': 'no'},
        {'path': common + 'leech_plants.png', 'check': 'no'},
        {'path': common + 'pure_energy.png', 'check': 'no'},
        {'path': common + 'fire_plus.png', 'check': 'no'},
        {'path': common + 'berserk.png', 'check': 'no'},
        {'path': common + 'explosion.png', 'check': 'no'},
        {'path': common + 'gambit.png', 'check': 'no'},
        {'path': common + 'giant_claw.png', 'check': 'no'},
        {'path': common + 'grim_reaper.png', 'check': 'no'},
        {'path': common + 'meteor_fall.png', 'check': 'no'},
        {'path': common + 'out_of_time.png', 'check': 'no'},
        {'path': common + 'purge.png', 'check': 'no'},
        {'path': common + 'slash.png', 'check': 'no'},
        {'path': common + 'ghost.png', 'check': 'no'},
        {'path': common + 'leaf_beast.png', 'check': 'no'},
        {'path': common + 'leech.png', 'check': 'no'},
        {'path': common + 'magneto.png', 'check': 'no'},
        {'path': common + 'electric_shock.png', 'check': 'no'},
        {'path': common + 'lava.png', 'check': 'no'},

    ]

    threads = [None] * len(paths)
    attacks = []

    def fn(path, x1, y1, x2, y2, check):
        return {'img': getImagePositionRegion(path, x1, y1, x2, y2, 0.8, 2), 'check': check}

    for i in range(len(threads)):
        path = paths[i]
        threads[i] = ThreadWithReturnValue(
            target=fn, args=(path['path'], 0, 500, 1600, 900, path['check']))
        threads[i].start()

    avoidAttack = [[-1]]
    for i in range(len(threads)):
        img = threads[i].join()
        attack = img['img']
        if exists(attack):
            if(img['check'] =='critical'):
                attacks.insert(0, [attack[0]+ 150, attack[1] + 50])
    
            if(img['check'] == 'avoid'):
                avoidAttack.insert(0, attack)
            else:   
                attacks.append(attack)

    newAttacks = getStrongAttacks(avoidAttack[0], attacks)
    print(newAttacks)
    for attack in newAttacks:
        if exists(attack):
            return attack
    return [-1]


def goToFight():
    select_dragon_thread = ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/battle/select_new_dragon.png', 0, 600, 1600, 900))
    select_dragon_thread.start()
    attack = getAttacks()

    if exists(attack):
        moveAndClick(attack)
        print('Attacked with', attack)
        delay(5)  # wait for the victory logo to have a chance to appear
        return goToFight()
    
    print('No attack, try to select a new dragon')
    selectDragonBtn = select_dragon_thread.join()
    print('Select Dragon is', selectDragonBtn)
    if exists(selectDragonBtn):
        moveAndClick(selectDragonBtn)
        print('New Dragon Selected')
        delay(5)  # wait for the dragon to have a change to appear
        return goToFight()
    return


def goToLeague():
    # League is positioned in the first half of the screen on the right hand side,so the rest can be skipped
    thread1 = ThreadWithReturnValue(target=getImagePositionRegion, args=(
   './img/battle/no_new_combats.png', 1000, 0, 1600, 450, 0.9, 20
    ))
    thread2 = ThreadWithReturnValue(target=getImagePosition, args=('./img/battle/league_oponent.png', 20, 0.8, 0.5))
    thread1.start()
    thread2.start()
    noMoreBattles = thread1.join()

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
    # end in the middle of the screen
    league = getImagePositionRegion('./img/battle/league.png', 0, 0, 900, 450)

    if not exists(league):
        return print('League button not found!')

    print('Start league battle...')
    moveAndClick(league)
    goToLeague()

def start():
    while True:
        goToFight()
        delay(5)

# start()