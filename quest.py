from battle import Battle
from close import check_if_ok
from move import center_map
from popup import Popup
from utils import delay, exists, get_monitor_quarters, moveAndClick, getImagePositionRegion, scroll
import constants as C


class Quest:
    quests_pos = [[530, 800], [1330, 800], [2100, 800]]
    battle_pos = [790, 1250]
    quest_pos = [1278, 710]
    scroll_pos = [2503, 810]

    def open_quest():
        center_map()
        delay(.2)
        moveAndClick(center_map())
        delay(.5)
        moveAndClick(Quest.battle_pos)
        delay(.5)
        moveAndClick(Quest.quest_pos)
        delay(1)
        scroll(Quest.scroll_pos, [0, Quest.scroll_pos[1]])
        delay(.5)
        scroll(Quest.scroll_pos, [0, Quest.scroll_pos[1]])
        delay(3)

        for quest in Quest.quests_pos:
            moveAndClick(quest)
            delay(1)
            go_to = getImagePositionRegion(C.QUEST_GO_TO_BATTLE, *get_monitor_quarters()['4thRow'], .8, 2)
            if exists(go_to):
                moveAndClick(go_to)
                delay(1)
                go_to = getImagePositionRegion(C.QUEST_GO_TO_BATTLE, *get_monitor_quarters()['full'], .8, 2)
                if exists(go_to): 
                    moveAndClick(go_to)
                    Battle.fight()
                    Popup.check_popup_chest()
        check_if_ok()
