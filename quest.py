from league import goToFight
from rewards import openChest
from utils import backFn, closePopup, delay, exists, getImagePosition, moveAndClick, moveTo, getImagePositionRegion, dragMap


def getQuest(retries=1):
    if retries == 0:
        return [-1]

    next = getImagePositionRegion(
        './img/battle/start_quest1.png', 0, 450, 1600, 900)

    print('next is ', next)
    if exists(next):
        return [next[0], next[1] - 100]

    moveTo([1500, 450])  # move to center, drag the map to the left by 100px
    dragMap([0, 450])
    return getQuest(retries - 1)


def battle():
    quest = getQuest()

    if not exists(quest):
        return print('No quest fight available')
    moveAndClick(quest)

    battle = getImagePositionRegion(
        './img/battle/go_battle.png', 500, 500, 1600, 900)
    if exists(battle):
        moveAndClick(battle)
    else:
        return print('No quest Battle')

    delay(1)
    battle = getImagePositionRegion(
        './img/battle/go_to_battle.png', 200, 200, 1600, 900)
    if exists(battle):
        print('battle 2', battle)
        moveAndClick(battle)

    dragonIsMissing = getImagePosition('./img/battle/missing_dragon.png', 10)
    if exists(dragonIsMissing):
        return moveAndClick(backFn())
    if exists(battle):
        goToFight()
        openChest()
    else: 
        print('No quest go to battle available')


def openQuestPanel():
    quest = getImagePosition('./img/battle/quest.png', 5)

    if not exists(quest):
        return print('Quest is not available')

    print('Start to battle...')
    moveAndClick(quest)
    battle()
    delay(.5)
    closePopup()
