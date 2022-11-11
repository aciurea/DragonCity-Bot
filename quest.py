from league import goToFight
from rewards import openChest
from utils import ThreadWithReturnValue, closePopup, delay, exists, go_back, moveAndClick, getImagePositionRegion, scroll


def getQuests():
    path = './img/battle/start_quest1.png'

    paths = []
    list = []
    step_px = 500
    for i in range(3):
        start, end = [i * step_px, i * step_px + step_px]
        list.append(ThreadWithReturnValue(target=getImagePositionRegion, args=(path, start, 600, end, 800, .8, 2)).start())

    for thread in list:
        quest = thread.join()

        if not exists(quest): continue;
        if quest in paths: continue
        paths.append([quest[0], quest[1]- 200])

    return paths

def open_battle():
    battle = getImagePositionRegion(
        './img/battle/go_battle.png', 650, 700, 1000, 850, .8, 2)
    if not exists(battle):
        print('No quest Battle')
        return [-1]
    moveAndClick(battle)
    delay(1)
    battle = getImagePositionRegion(
        './img/battle/go_to_battle.png', 600, 600, 900, 750, .8, 2)
    if not exists(battle):
        print('No go Battle btn available')
        return [-1]
    moveAndClick(battle)
    delay(1)
    battle =  getImagePositionRegion('./img/battle/go_to_battle.png', 600, 600, 900, 750, .8, 4)
    if exists(battle): 
        print('No go battle btn available')
        return [-1]
    return [1]

def open_quest():
    def inner_quest():
        quests = getQuests()

        for quest in quests:
            if not exists(quest): continue
            moveAndClick(quest)
            delay(1)
            battle = open_battle()
            if exists(battle): 
                print('Battle started')
                return [1]
            go_back()
            delay(.5)
            go_back()
        return [-1]
    quest = inner_quest()
    if exists(quest): 
       return quest

    delay(.5)
    scroll([1550, 450], [9, 450])
    delay(1)
    quest = inner_quest()
    if exists(quest):
        return quest
      
    return [-1]

def openQuestPanel():
    quest_panel = getImagePositionRegion('./img/battle/quest.png', 650, 200, 1000, 500)

    if not exists(quest_panel):
        closePopup()
        return print('Quest is not available')

    print('Start to battle...')
    moveAndClick(quest_panel)
    if exists(open_quest()):
        goToFight()
        delay(2)
        openChest()
    delay(.5)
    closePopup()
