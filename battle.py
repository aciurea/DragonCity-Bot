from utils import getImagePosition, moveAndClick
from league import openLeaguePanel


def chooseBattle():
    battleBtn = getImagePosition('./img/battle/battle_btn.png')

    if (battleBtn[0] == -1):
        return print('Battle Button not found')

    moveAndClick(battleBtn)
    openLeaguePanel()


def startBattle():
    print('Start to battle...')
    centerIsland = getImagePosition('./img/utils/center_island.png')

    print('Center island ', centerIsland)
    if (centerIsland[0] == -1):
        return print('Center not found. Cannot continue')
    moveAndClick(centerIsland)
    chooseBattle()
