import time
from utils import getImagePosition, moveAndClick
from league import openLeaguePanel


def chooseBattle():
    battleBtn = getImagePosition('./img/battle/battle_btn.png')
    print(123, battleBtn[0], battleBtn[1], battleBtn[0] == -1)
    if (battleBtn[0] == -1):
        return print('Battle Button not found')

    moveAndClick(battleBtn)
    openLeaguePanel()


def start():
    print('Start to battle...')
    while (True):
        centerIsland = getImagePosition('./img/utils/center_island.png')
        if (centerIsland[0] == -1):
            return print('Center not found. Cannot continue')
        moveAndClick(centerIsland)
        chooseBattle()
        time.sleep(20)


start()
