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
from collectFood import heroic_collect, FoodCollector

from collectGold import collectGold
from daily_collect import Daily_Collect
from habitat import Habitat
from heroic import Heroic
from league import League
from move import moveAndClick, moveTo, multiple_click
from position_map import Position_Map
from orbs import Orbs
from quest import Quest
from runner import Runner
from shop import Shop
from tv import TV
from utils import delay, get_grid_monitor, move_to_left, get_screen_resolution, get_pos_with_grid, getImagePositionRegion
from close import check_if_ok
from popup import Popup
from position_map import Position_Map
from events_collection import Events_Collection
from wizard import Wizard
from mail import Mail
from puzzle import Puzzle
from screen import Screen
from recall import Recall
from flame import Flame
from clear_event import ClearEvent
from open import OpenApp
from hatch import Hatch
from close import Close

import constants as C


import time
import requests


def get_pos_in_percentages(value):
    res = get_monitors()
    return [value[0] / res[0].width, value[1] / res[0].height]

while 1:
    if K.is_pressed('w'):
        Close.get_lose_text()
        # Battle.fight()
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
        Breed.breed('sell', 50)
    if K.is_pressed('f'):
        # heroic_collect(times=250)
        FoodCollector.fast_food()
    if K.is_pressed('n'):
        move_to_left()
    if K.is_pressed('b'):
        Breed.breed('breed', 24)
        Breed.breed('sell', 4)
        Breed.breed('sell', 4)
    if K.is_pressed('c'): 
        Position_Map.center_map()
    if K.is_pressed('r'):
        Heroic.race()
    if K.is_pressed('g'):
        collectGold()
    if K.is_pressed('p'):  # if key 'q' is pressed
        print('mouse pos', get_pos_in_percentages(mouse.get_position()))
    if K.is_pressed('t'):
        multiple_click([2560 / 2, 1440 / 2], 5)
        delay(2.5)
        moveAndClick([1251, 1146])
    delay(.5)



