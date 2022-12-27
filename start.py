from app_start import check_if_can_claim_daily, check_if_can_close_divine_offer
from battle import startBattle
from breed import startBreeding
from collectFood import collectFood
from collectGold import collectGold
from divine_tree import devin_tree
from heroic import heroic_race
from open import close_app, open_app
from rewards import collectRewards
from shop import shop
from utils import check_if_not_ok, delay, dragMapToCenter
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
    check_if_can_claim_daily()
    check_if_can_close_divine_offer()

def doHeroicRace():
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
  
        times = 20
        while (times > 0):
            runAction(do_action(mission))
            times -= 1
            delay(0.1)

def start():
    print('hello')
    open_app()
    # runAction(doHeroicRace)
    i = 5
    while i > 0:
        i -= 1
        runAction(collectGold)
        runAction(collectFood)
        runAction(startBattle)
        runAction(shop)
        runAction(collectRewards)
        runAction(startBreeding)
        # runAction(devin_tree)
        delay(.5)
        check_if_not_ok()
    close_app()

while(True):
    start()
    delay(60)