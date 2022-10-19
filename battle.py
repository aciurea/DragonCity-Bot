from quest import openQuestPanel
from utils import exists, getImagePosition, getImagePositionRegion, moveAndClick
from league import openLeaguePanel


def chooseBattle():
    battleBtn = getImagePositionRegion('./img/battle/battle_btn.png', 200, 500, 1000, 900) # battle position is at the bottom

    if not exists(battleBtn):
        return print('Battle Button not found')

    moveAndClick(battleBtn)


def startBattle():
    for action in [openQuestPanel, openLeaguePanel]:
        centerIsland = getImagePosition('./img/utils/center_island.png')

        if (centerIsland[0] == -1):
            return print('Center not found. Cannot continue')
        moveAndClick(centerIsland)
        chooseBattle()
        action()
    return print('Finishe battles')
