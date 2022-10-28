from quest import openQuestPanel
from utils import exists, getImagePositionRegion, moveAndClick
from league import openLeaguePanel


def chooseBattle():
    moveAndClick([800, 450])
    battleBtn = getImagePositionRegion('./img/battle/battle_btn.png', 400, 700, 600, 900, .8, 3)

    if not exists(battleBtn):
        return print('Battle Button not found')

    moveAndClick(battleBtn)


def startBattle():
    for action in [openQuestPanel, openLeaguePanel]:
        chooseBattle()
        action()
    return print('Finishe battles')
