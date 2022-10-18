from drag import dragMap
from league import goToFight
from utils import backFn, closePopup, exists, getImagePosition, moveAndClick, moveTo, retry


def getQuest(retries = 3, x = 900):
    if(retries == 0): return [-1]
    distance = 100
    paths = [
            './img/battle/start_quest2.png',
            './img/battle/start_quest1.png'
            ]

    for path in paths:
        next = getImagePosition(path, 5)
        if exists(next): 
            return next
    
    moveTo([x, 450]) # move to center, drag the map to the left by 100px
    dragMap([x - distance, 450])
    getQuest(retries - 1, x -distance)
    return [-1]

def battle():
    quest = getQuest()
          
    if not exists(quest):
        return print('No quest fight available')
   
    battle = getImagePosition('./img/battle/go_battle.png')
    if exists(battle):
        moveAndClick(battle)
    else:
       return print('No quest Battle')
    
    battle = getImagePosition('./img/battle/go_to_battle.png')

    # TODO take the question mark and if exists, click on back button
    dragonIsMissing = True
    if(dragonIsMissing):
       return moveAndClick(backFn())

    moveAndClick(battle, 'Battle')
    return goToFight() if exists(battle) else print('No quest go to battle available')


def openQuestPanel():
    quest = getImagePosition('./img/battle/quest.png', 5)

    if (quest == -1):
        return print('Quest is not available')

    print('Start to battle...')
    moveAndClick(quest)
    battle()
    closePopup()
    return
