# from breed import sellEgg
# from utils import delay, moveTo
import mouse
import keyboard as K
from datetime import datetime, timedelta

from pyautogui import scroll
from screeninfo import get_monitors
from alliance import Alliance
from arena import Arena
from battle import Battle
from breed import Breed
from collectFood import heroic_collect

from collectGold import collectGold
from daily_collect import Daily_Collect
from habitat import Habitat
from heroic import Heroic
from league import League
from move import moveAndClick, moveTo, multiple_click
from orbs import Orbs
from quest import Quest
from runner import Runner
from shop import Shop
from tv import TV
from utils import delay, dragMapToCenter, get_grid_monitor, move_to_left

import requests


#orbs position
# 724, 629
while 1:
    if K.is_pressed('w'):
        Daily_Collect.collect()
    #    Heroic.race()
    if K.is_pressed('l'):
        multiple_click(mouse.get_position(), 112, 0.2)
    if K.is_pressed('q'):
        Quest.open_quest()
    if K.is_pressed('a'):
        Arena.enter_battle()
    if K.is_pressed('v'):
        TV.open_tv()
    if K.is_pressed('o'):
       Orbs.collect_orbs()
    if K.is_pressed('l'):
        League.enter_league()
    if K.is_pressed('e'):
        arr = [1,2 ,3, 4,5]
        print(arr[1:0:-1])
    if K.is_pressed('h'):
        Breed.breed('hatch', 30)
        # Habitat.buy_habitat()
    if K.is_pressed('f'):
        heroic_collect(times=40)
    if K.is_pressed('n'):
        move_to_left()
    if K.is_pressed('b'):
        Breed.breed('breed', 20)
    if K.is_pressed('c'): 
        dragMapToCenter()
    if K.is_pressed('r'):
        Heroic.race()
    if K.is_pressed('g'):
        collectGold()
    if K.is_pressed('p'):  # if key 'q' is pressed 
        [ res ] = get_monitors()
        print(get_grid_monitor())
        # print(res)
        # print(res.width, res.height, res.width_mm, res.height_mm)ppppppppp
        print('mouse pos',mouse.get_position())
        # print('grid', get_grid_monitor())
        # moveAndClick(mouse.get_position())
        # print(Battle.is_fight_in_progress())
        # print(get_text(oponent=False))
        # print(get_text(oponent=True))
        # _freeze_dragons(-1, 313707)
        # _freeze_dragons(999999991, 285192)
        # get_text()
    if K.is_pressed('t'):
      moveAndClick([724, 629])
    delay(.5)
