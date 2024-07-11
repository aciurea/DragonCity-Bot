from battle import Battle
from close import check_if_ok
from popup import Popup
from utils import delay, exists, get_monitor_quarters, moveAndClick, getImagePositionRegion, scroll

from position_map import Position_Map
from pyautogui import scroll
import constants as C
import time

class Quest:
    mon_quarters = get_monitor_quarters()

    def open_quest():
        Position_Map.center_map()

        battle_btn = Quest._get_batttle_btn()
        if not exists(battle_btn): return print('Battle button not found')

        moveAndClick(battle_btn)
        delay(1)
        moveAndClick(Quest.mon_quarters['center'])
        delay(10)

        scroll_times = 10

        # loop through all the quests
        while scroll_times >= 0:
            scroll_times -= 1
            Quest._open_quest_battle()
            scroll(-2_000)
        check_if_ok()
        
    def _open_quest_battle():
        quest_battle_btn = Quest._get_quest_battle_btn()
        curr_time = time.time()

        # sometimes there are multiple battle available in the same screen without scrolling
        while exists(quest_battle_btn) and time.time() - curr_time < 120:
            if not exists(quest_battle_btn): return print('Quest battle button not found')

            moveAndClick(quest_battle_btn)
            delay(2)

            quest_go_to_battle_btn = Quest._get_quest_go_to_battle_btn()

            if not exists(quest_go_to_battle_btn): return print('Quest go to battle button not found')

            moveAndClick(quest_go_to_battle_btn)

            delay(2)
            moveAndClick(Quest._get_quest_go_to_battle_btn_2())
            delay(2)
            Battle.fight(change_dragon=False)
            delay(2)
            Popup.check_popup_chest()

    def _get_quest_go_to_battle_btn_2():
        return getImagePositionRegion(C.QUEST_GO_TO_BATTLE_2, *Quest.mon_quarters['2ndHorHalf'], .8, 2)

    def _get_quest_go_to_battle_btn():
        return getImagePositionRegion(C.QUEST_GO_TO_BATTLE, *Quest.mon_quarters['4thRow'], .8, 2)

    def _get_quest_battle_btn():
        return getImagePositionRegion(C.QUEST_BATTLE_BTN, *Quest.mon_quarters['4thRow'], .8, 2)

    def _get_batttle_btn():
        return getImagePositionRegion(C.BATTLE_BATTLE_BTN, *Quest.mon_quarters['4thRow'], .8, 2)
