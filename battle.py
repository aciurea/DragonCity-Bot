from quest import openQuestPanel
from utils import getImagePosition, moveAndClick
from league import openLeaguePanel


def chooseBattle():
    battleBtn = getImagePosition('./img/battle/battle_btn.png')

    if (battleBtn[0] == -1):
        return print('Battle Button not found')

    moveAndClick(battleBtn)


def startBattle():
    for action in [openLeaguePanel, openQuestPanel]:
        centerIsland = getImagePosition('./img/utils/center_island.png')

        if (centerIsland[0] == -1):
            return print('Center not found. Cannot continue')
        moveAndClick(centerIsland)
        chooseBattle()
        action()
    return print('Finishe battles')
