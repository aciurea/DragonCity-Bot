from arena import arena
from quest import openQuestPanel
from utils import delay, exists, getImagePositionRegion, moveAndClick
from league import openLeaguePanel

def chooseBattle():
    moveAndClick([800, 450])
    delay(1)
    battleBtn = getImagePositionRegion('./img/battle/battle_btn.png', 400, 700, 600, 900)

    if not exists(battleBtn):
        return print('Battle Button not found')

    moveAndClick(battleBtn)

def startBattle():
    print('start the battle')
    for action in [openLeaguePanel, openQuestPanel]:
        chooseBattle()
        action()
    arena()
    return print('Finishe battles')


def start():
    delay(1)
    startBattle()

# start()
    