from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from fail import checkAndCloseIfFails
from heroic import heroic
from rewards import collectRewards
from utils import delay, dragMapToCenter

halfAnHour = 1800

def runAction(action):
    dragMapToCenter()
    action()

def doHeroicRace():
    priorities = {'breed': startBreeding,
                  'feed': startBreeding,
                  'hatch': startBreeding,
                  'food': collectFood
                  }
    priority = heroic()
    print('priority is ', priority)
    if (priority == -1):
        print('no priority')
    else:
        work = priorities['hatch']
        print(work, priority)
        times = 20
        while (times > 0):
            work('hatch')
            times -= 1
            delay(0.5)

def start():
    # doHeroicRace()
    runAction(collectGold)
    runAction(collectFood)
    runAction(collectRewards)
    runAction(startBattle)
    runAction(startBreeding)
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
        delay(60)

run()
