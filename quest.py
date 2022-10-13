from league import goToFight
from utils import getImagePosition, moveAndClick, closePopup, closeVideo


def battle():
    next = getImagePosition('./img/battle/next_reward.png')

    if (next[0] == -1):
        return print('No reward to click')
    moveAndClick(next)
    battle = getImagePosition('./img/battle/go_battle.png')
    if (battle[0] != -1):
        moveAndClick(battle)
    else:
        print('No quest Battle')
    goToBattle = getImagePosition('./img/battle/go_to_battle.png')
    if (goToBattle[0] != -1):
        moveAndClick()
        goToFight()
    else:
        print('No quest go to battle button')


def openQuestPanel():
    quest = getImagePosition('./img/battle/quest.png')

    if (quest == -1):
        return print('Quest is not available')
    moveAndClick(quest)
