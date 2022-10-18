from league import goToFight
from utils import backFn, closePopup, exists, getImagePosition, moveAndClick, retry


def battle():
    paths = [
            './img/battle/start_quest2.png',
            './img/battle/start_quest1.png'
            ]
    next = [-1]

    for path in paths:
        next = getImagePosition(path, 5)
        if exists(next): 
            moveAndClick(next)
            break
          
    if not exists(next):
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
