from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from drag import dragMapToCenter, getMovePositions
from fail import checkAndCloseIfFails
from heroic import heroic
from rewards import collectRewards
from utils import delay


def runAction(action):
    dragMapToCenter()
    action()

def start():
    # priorities = {'breed': startBreeding,
    #               'feed': startBreeding,
    #               'hatch': startBreeding,
    #               'food': collectFood
    #               }
    # priority = heroic()
    # print('priority is ', priority)
    # if (priority == -1):
    #     print('no priority')
    # else:
    #     work = priorities['hatch']
    #     print(work, priority)
    #     times = 20
    #     while (times > 0):
    #         work('hatch')
    #         times -= 1
    #         delay(0.5)

    runAction(collectGold)
    runAction(collectFood)
    runAction(startBattle)
    runAction(collectRewards)
    # runAction(startBreeding)
    # checkAndCloseIfFails()


def hatchAndCollect():
    index = 10
    collectFood()
    while (index > 0):
        startBreeding('hatch')
        index -= 1
    delay(5)

def run():
    while (True):
        start()
        delay(5)

run()
