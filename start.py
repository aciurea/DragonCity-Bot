import time
from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from drag import dragMap, getMovePositions
from fail import checkAndCloseIfFails
from heroic import heroic
from rewards import collectRewards
from utils import delay


def start():
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
        work = priorities[priority]
        print(work, priority)
        times = 10
        while (times > 0):
            work(priority)
            times -= 1
            delay(0.5)

    collectGold()
    collectFood()
    startBattle()
    collectRewards()
    startBreeding()

    # checkAndCloseIfFails()

def run():
    while (True):
        positions = getMovePositions()
        for position in positions:
            print('Position is ', position)
            dragMap(position)
            start()

        time.sleep(5)


run()
