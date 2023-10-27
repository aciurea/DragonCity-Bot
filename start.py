from app_start import check_if_can_claim_daily, check_if_can_close_divine_offer
from arena import arena
from battle import startBattle
from breed import startBreeding
from collectFood import collect_food
from collectGold import collectGold
from divine_tree import tree_of_life
from heroic import heroic_race
from open import close_app, open_app
from rewards import collectRewards
from shop import shop
from towers import boost_gold, collect_gems, collect_resources
from utils import check_if_not_ok, delay, dragMapToCenter, exists, get_time_to_midnight, getImagePosition
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


# 1600 900 309 174
# mouse pos (611, 739)
# 1600 900 309 174
# mouse pos (775, 690)
# 1600 900 309 174
# mouse pos (775, 690)
# 1600 900 309 174
# mouse pos (985, 744)
# 1600 900 309 174
# mouse pos (834, 814)
def doHeroicRace():
    if not exists(getImagePosition(C.HEROIC_ARENA, 2)): return
    print('Entered heoric race')

    priorities = { 'breed': startBreeding,
                  'feed': startBreeding,
                  'hatch': startBreeding,
                  'food': collect_food
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
  
        times = 15
        while (times > 0):
            runAction(do_action(mission))
            times -= 1

def start():
    st = time.time()   
    open_app()
    if not exists(collect_resources()):
        runAction(collectGold)
        runAction(collectFood)
    runAction(doHeroicRace)
    runAction(startBattle)
    runAction(shop)
    runAction(collectRewards)
    runAction(startBreeding)
    runAction(tree_of_life)
    delay(.5)
    check_if_not_ok()
    runAction(collectGold)
    boost_gold(dragMapToCenter())
    collect_gems(dragMapToCenter())
    runAction(arena) # run it again since it might failed on first run
    print('Operation took: '+ str(((time.time() - st) / 60)) + ' minutes')
    print('End At: ' + datetime.datetime.now().strftime("%X"))
    close_app()

while(True):
    seconds_limit = 60 * 20
    seconds_to_midnight = get_time_to_midnight()
    #  when fighting, the midnight offers popups and blocks all the fights if it happens to be there.
    # delay this in order to have a proper way of starting the game
    if seconds_to_midnight < seconds_limit:
        delay(seconds_to_midnight + 120) # delay the difference + 2 minutes.
    start()
    delay_time = HALF_AN_HOUR if exists(getImagePosition(C.HEROIC_ARENA, 2)) else HALF_AN_HOUR * 4
    print('Next time is ', delay_time)
    delay(delay_time)