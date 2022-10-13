import time
from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from drag import dragMap, getMovePositions
from fail import checkAndCloseIfFails
from rewards import collectRewards


def start():
    collectGold()
    print('Finished collecting the gold...')
    collectFood()
    print('Finished collecting the food...')
    #collectRewards()
    print('Finished watching videos...')
    # startBattle()
    print('Finishe battles')
    # startBreeding()

def run():
    while (True):
        positions = getMovePositions()
        for position in positions:
            print('Position is ', position)
            dragMap(position)
            start()

        time.sleep(5)


run()
