from battle import Battle
from close import check_if_ok
from popup import Popup
from utils import delay, exists, get_monitor_quarters, getImagePositionRegion
from screen import Screen
from move import moveAndClick

from position_map import Position_Map
from pyautogui import scroll
import constants as C


class Quest:
    mon_quarters = get_monitor_quarters()

    def open_quest():
        Position_Map.center_map()

        battle_btn = Quest._get_batttle_btn()
        if not exists(battle_btn): return print('Battle button not found')

        moveAndClick(battle_btn)
        delay(1)
        moveAndClick(Quest.mon_quarters['center'])
        delay(2)
        scroll_times = 11
        # loop through all the quests
        while scroll_times >= 0:
            scroll_times -= 1
            Quest._open_quest_battle_by_checking_requirements()
            scroll(-2_000)
        check_if_ok()
        check_if_ok()

    @staticmethod
    def _open_quest_battle_by_checking_requirements():
        info = getImagePositionRegion(C.QUEST_INFO, *[300, 1040, 1800, 1200], .8, 2)

        if exists(info):
            if exists(getImagePositionRegion(C.QUEST_REQ, *[0, info[1] - 150, info[0], info[1]], .8, 2)):
                return print('Requirements not met')
            if exists(getImagePositionRegion(C.QUEST_NOT_READY, *[info[0] - 700, info[1] - 200, info[0], info[1] + 100], .8, 2)): return print('Requirements not met ::')

            moveAndClick([info[0], info[1]- 400])
            delay(1)
            moveAndClick(Quest._get_battle_btn(bbox=[1077, 1240, 1258, 1339]))
            delay(1)
            moveAndClick(Quest._get_battle_btn(bbox=[1057, 1023, 1254, 1128]))
            delay(1)
            Battle.fight(change_dragon=False)
            delay(1)
            Popup.check_popup_chest()
            return Quest._open_quest_battle_by_checking_requirements()
        else:
            text_positions = Screen.get_text_pos(Quest.mon_quarters['2ndHorHalf'])

            for t in text_positions:
                if 'claim' in t['text'].lower(): return moveAndClick(t['position'])

    @staticmethod
    def _get_battle_btn(bbox=[850, 995, 1550, 1370]):
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if 'goto' in t['text'].lower():
                return t['position']

    def _get_batttle_btn():
        return getImagePositionRegion(C.QUEST_BATTLE_BTN, *Quest.mon_quarters['4thRow'], .8, 2)
