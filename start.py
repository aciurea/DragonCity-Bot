from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from divine_tree import devine_tree
from heroic import heroic_race
from rewards import collectRewards
from shop import shop
from utils import check_if_not_ok, delay, dragMapToCenter, exists
import win32gui
import win32con
HALF_AN_HOURS = 1800

Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

def runAction(action):
    dragMapToCenter()
    action()
    delay(1)
    check_if_not_ok()

def doHeroicRace():
    priorities = { 'breed': startBreeding,
                  'feed': startBreeding,
                  'hatch': startBreeding,
                  'food': collectFood
                  }
    mission = heroic_race()
    if not exists(mission):
       return print('no priority')

    action = priorities[mission]

    def do_action():
        action(mission)
    times = 20
    while (times > 0):
        runAction(do_action)
        times -= 1
        delay(0.5)

def start():
    runAction(doHeroicRace)
    print('start doing the rest of the actions....')
    runAction(collectGold)
    runAction(collectFood)
    runAction(startBattle)
    runAction(shop)
    runAction(collectRewards)
    runAction(startBreeding)
    runAction(devine_tree)
    delay(.5)
    check_if_not_ok()


def hatchAndCollect():
    index = 10
    collectFood()
    while (index > 0):
        startBreeding('hatch')
        index -= 1
    delay(30)

def run():
    while (True):
        start()
        # delay(5)

run()
