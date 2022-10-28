import mouse
from league import goToFight
from rewards import openChest
from utils import closePopup, delay, exists, moveAndClick, getImagePositionRegion


def getQuest(retries=2):
    if retries == 0:
        return [-1]

    next = getImagePositionRegion(
        './img/battle/start_quest1.png', 0, 600, 1600, 800)

    print('next is ', next)
    if exists(next):
        return [next[0], next[1] - 100]

    mouse.drag(1500, 450, 800, 450, True, .5)
    return getQuest(retries - 1)


def battle():
    quest = getQuest()

    if not exists(quest):
        return print('No quest fight available')
    moveAndClick(quest)

    ## TODO update the coordonates
    battle = getImagePositionRegion(
        './img/battle/go_battle.png', 650, 700, 1000, 850)
    if not exists(battle):
        return print('No quest Battle')

    moveAndClick(battle)

    delay(1)
    battle = getImagePositionRegion(
        './img/battle/go_to_battle.png', 600, 600, 900, 750)


    if exists(battle):
        print('battle 2', battle)
        moveAndClick(battle)
        battle =  getImagePositionRegion('./img/battle/go_to_battle.png', 600, 600, 900, 750, .8, 2)
        if exists(battle):
            delay(1)
            closePopup()
            return print('The battle didnt start')
        delay(3) # wait for the battle to start
        goToFight()
        openChest()
        return
   


def openQuestPanel():
    quest = getImagePositionRegion('./img/battle/quest.png', 650, 200, 1000, 500)

    if not exists(quest):
        return print('Quest is not available')

    print('Start to battle...')
    moveAndClick(quest)
    battle()
    delay(.5)
    closePopup()
