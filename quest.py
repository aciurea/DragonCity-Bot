from league import goToFight
from utils import getImagePosition, moveAndClick, closePopup


def battle():
    paths = [
        './img/battle/start_quest1.png',
        './img/battle/start_quest2.png']
    next = [-1]

    for path in paths:
        next = getImagePosition(path, 5)
        if (next != -1):
            break

    if (next[0] == -1):
        return print('No reward to click')

    moveAndClick(next)
    battle = getImagePosition('./img/battle/go_battle.png')
    if (battle[0] != -1):
        moveAndClick(battle)
    else:
        print('No quest Battle')
    battle = getImagePosition('./img/battle/go_to_battle.png')
    if (battle[0] != -1):
        moveAndClick(battle)
        return goToFight()
    else:
        return print('No quest go to battle button')


def openQuestPanel():
    quest = getImagePosition('./img/battle/quest.png', 5)

    if (quest == -1):
        return print('Quest is not available')

    print('Start to battle...')
    moveAndClick(quest)
    battle()
    closePopup()
    return
