from utils import getImagePosition, moveAndClick, closePopup, closeVideo


def openQuestPanel():
    quest = getImagePosition('./img/battle/quest.png')

    if (quest == -1):
        return print('Quest is not available')
    moveAndClick(quest)
