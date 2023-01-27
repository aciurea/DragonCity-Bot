from app_start import check_if_can_claim_daily, check_if_can_close_divine_offer
from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from divine_tree import tree_of_life
from heroic import heroic_race
from open import close_app, open_app
from rewards import collectRewards
from shop import shop
from towers import boost_gold, collect_gems, collect_resources
from utils import check_if_not_ok, delay, dragMapToCenter, exists, getImagePosition
import win32gui
import win32con
import datetime
import time
import constants as C

HALF_AN_HOUR = 1800

Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

def runAction(action):
    dragMapToCenter()
    action()
    delay(1)
    check_if_not_ok()
    check_if_can_claim_daily()
    check_if_can_close_divine_offer()

def doHeroicRace():
    if not exists(getImagePosition(C.HEROIC_ARENA, 2)): return
    priorities = { 'breed': startBreeding,
                  'feed': startBreeding,
                  'hatch': startBreeding,
                  'food': collectFood
                  }
    missions = heroic_race()
    print('Missions are ', missions)
    if len(missions) == 0:
       return print('no priority')
    def do_action(mission):
        def inner():
            action(mission)
        return inner

    for mission in missions:
        action = priorities[mission]
        if mission != 'food':
            collectFood(False, lambda: None)
  
        times = 20
        while (times > 0):
            runAction(do_action(mission))
            times -= 1

def start():
    st = time.time()   
    open_app()
    runAction(startBattle)
    if not exists(collect_resources(dragMapToCenter())):
        runAction(collectGold)
        runAction(collectFood)
    runAction(doHeroicRace)
    runAction(shop)
    runAction(collectRewards)
    runAction(startBreeding)
    runAction(tree_of_life)
    delay(.5)
    check_if_not_ok()
    runAction(collectGold)
    boost_gold(dragMapToCenter())
    collect_gems(dragMapToCenter())
    if exists(getImagePosition(C.HEROIC_ARENA, 2)): runAction(startBattle)
    print('Operation took: '+ str(((time.time() - st) / 60)) + ' minutes')
    print('End At: ' + datetime.datetime.now().strftime("%X"))
    close_app()

while(True):
    start()
    delay(HALF_AN_HOUR * 1.5)