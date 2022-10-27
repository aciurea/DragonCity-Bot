from quest import openQuestPanel
from utils import exists, getImagePosition, getImagePositionRegion, moveAndClick
from league import openLeaguePanel


def chooseBattle():
    battleBtn = getImagePositionRegion('./img/battle/battle_btn.png', 400, 700, 600, 900, .8, 3)

    if not exists(battleBtn):
        return print('Battle Button not found')

    moveAndClick(battleBtn)


def startBattle():
    for action in [openQuestPanel, openLeaguePanel]:
        centerIsland = getImagePosition('./img/utils/artifact_2.png')

        if not exists(centerIsland):
            return print('Center not found. Cannot continue')
        moveAndClick([centerIsland[0] - 30, centerIsland[1]])
        chooseBattle()
        action()
    return print('Finishe battles')
