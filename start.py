from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from heroic import heroic
from rewards import collectRewards
from utils import check_if_not_ok, delay, dragMapToCenter

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
    pos = dragMapToCenter()
    print('center is ', pos)
    collectGold(pos)
    runAction(collectFood)
    runAction(collectRewards)
    runAction(startBattle)
    runAction(startBreeding)
    delay(.5)
    check_if_not_ok()


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
        delay(15)

run()
