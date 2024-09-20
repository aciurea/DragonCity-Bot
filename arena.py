import time

from position_map import Position_Map
from battle import Battle
from close import check_if_ok, Close
from move import multiple_click, moveAndClick
from popup import Popup
from utils import (delay, exists, getImagePositionRegion)
from screen import Screen

text = {
    'refill': 'refill24',
    'fight': 'fightl',
    'claim': 'claimi',
    'attack': 'attack',
    'collect': 'collect',
    'change': 'change',
    'enhance': 'enhance',
    'freespini': 'freespini',
    'freespin': 'freespin',
}

class Arena:
    @staticmethod
    def _change_defetead_dragon():
        bboxes = [
            [0.19921875, 0.72, 0.27734375, 0.770834],
            [0.51953125, 0.72, 0.59765625, 0.770834],
            [0.841796875, 0.72, 0.916015625, 0.770834],
        ]

        for bbox in bboxes:
            text_positions = Screen.get_text_pos(bbox)
            print(text_positions)
            if len(text_positions) > 0 and Screen.is_match_with_one_difference(text['enhance'], text_positions[0]['text']) : continue

            moveAndClick(Screen.get_pos([bbox[0], bbox[1]]))
            delay(1)
            filter_pos = [0.68854167, 0.8481]
            order_pos = [0.65677083, 0.23981]
            order_by_power_pos = [0.62083, 0.487037]
            first_dragon_pos = [0.26875, 0.3943]

            moveAndClick(Screen.get_pos(filter_pos))
            delay(.2)
            moveAndClick(Screen.get_pos(order_pos))
            delay(1)
            moveAndClick(Screen.get_pos(order_by_power_pos))
            delay(1)
            moveAndClick(Screen.get_pos(first_dragon_pos))
        check_if_ok()

    def _wait_for_the_fight_tab():
        start = time.time()
        fight_tab = Arena._get_fight_tab()

        while time.time() - start < 10 and not exists(fight_tab):
            fight_tab = Arena._get_fight_tab()
            delay(1)
        moveAndClick(fight_tab)

    def _do_free_spin():
        bbox = [0.782, 0.25929, 0.872395834, 0.312037]
        text_positions = Screen.get_text_pos(bbox)

        if len(text_positions) == 0: return
        for t in text_positions:
            if Screen.is_match_with_one_difference(text['freespini'], t['text'].lower()):
                moveAndClick(t['center'])
                delay(1)
                break

        bbox = [0.46927083, 0.7935185, 0.546354167, 0.8361]
        text_positions = Screen.get_text_pos(bbox)
        for t in text_positions:
            if Screen.is_match_with_one_difference(text['freespin'], t['text'].lower()):
                moveAndClick(t['center'])
                delay(5)
                check_if_ok()
                break

    @staticmethod
    def enter_battle():
        Arena._open_arena()
        Arena._preapre_arena()

        start_fight = Arena._get_fight_btn()
       
        # if doesn't end in 10 minutes, we stop the script.
        time_limit = 600
        start_time = time.time()

        while exists(start_fight):
            if (time.time() - start_time) > time_limit: 
                raise Exception('Time limit exceded on arena. Closing the app....')
            
            print('Start new Arena battle')
            Arena._prepare_fight()
            Arena._check_and_collect_rewards()

            # start the fight
            moveAndClick(start_fight)
            delay(.5)
            moveAndClick([start_fight[0], start_fight[1] + 15]) # because of spin button I need to click again.

            Battle.fight()
            
            Arena._claim_arena_battle_result()
            
            delay(1)
            Arena.close_buying_dragon_powers()
            start_fight = Arena._get_fight_btn()
        check_if_ok()
        print('Arena battle is over')

    @staticmethod
    def _open_arena():
        battle_pos = Screen.get_pos([0.30859375, 0.868056])
        arena_pos = Screen.get_pos([0.698046875, 0.50694])
        open_actions = [
            Position_Map.center_map,
            lambda: moveAndClick(battle_pos),
            lambda: moveAndClick(arena_pos),
        ]
        for action in open_actions:
            action()
            delay(1)

    @staticmethod
    def _preapre_arena():
        if not exists(Arena._get_fight_btn()):
            get_to_fight_ready_actions = [
                Arena._check_attack_report,
                Arena._check_start_new_season,
                Arena._claim_rush_battle_end,
                Arena._wait_for_the_fight_tab,
                Arena._prepare_fight,
                Arena._do_free_spin
            ]
            for action in get_to_fight_ready_actions:
                st = time.time()
                action()
                print('Time to get to fight ready', str(action.__name__), time.time() - st)
                delay(.3)

    @staticmethod
    def _get_fight_btn(gray_mode=False):
        bbox = [0.430859375, 0.814583,0.5234375, 0.868056]
        text_positions = Screen.get_text_pos(bbox, gray_mode)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['refill'], t['text'].lower()): return [-1]
            if Screen.is_match_with_one_difference(text['fight'], t['text'].lower()): return t['position']

        if not gray_mode: return Arena._get_fight_btn(True)
        return [-1]

    
    @staticmethod
    def _prepare_fight():
        bbox = [0.118359375, 0.679167, 0.411328125, 0.731945]
        text_positions = Screen.get_text_pos(bbox)
        if len(text_positions) == 3: return

        bbox = [0.25390625, 0.7916, 0.337890625, 0.861]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if text['change'] in t['text'].lower():
                moveAndClick(t['position'])
                delay(1)
                Arena._change_defetead_dragon()

    def _claim_rush_battle_end():
        bbox = [0.622265625, 0.854861, 0.71875, 0.9305]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claim'], t['text']):
                moveAndClick(t['position'])
                delay(2)
                moveAndClick(Screen.get_pos([0.36875, 0.62]))
                delay(3)
                times = 5
                while times > 0:
                    times -= 1
                    Popup.check_popup_chest()
                    delay(1)
                # it happens that on last chest for the Tap to Open message to not appear and claim button to be displayed directly.
                moveAndClick(Popup._get_claim_btn())

    @staticmethod
    def _claim_arena_battle_result():
        bbox = [0.4625, 0.862037, 0.5328125, 0.916]
        text_positions = Screen.get_text_pos(bbox)

        if len(text_positions) == 0: moveAndClick(Screen.get_pos([0.49375, 0.893518]))
        else: 
            for t in text_positions: moveAndClick(t['position'])
        delay(2)

    @staticmethod
    def close_buying_dragon_powers():
        if exists(Arena._get_fight_btn()): return

        check_if_ok() # first we hit the close button
        delay(1)
        Close.get_lose_text()

    @staticmethod
    def _get_fight_tab():
        bbox = [0.28984375, 0.232, 0.35078125, 0.278]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference('fight', t['text']):  return t['position']
              
        return [-1]

    @staticmethod
    def _check_start_new_season():
        if exists(Arena._get_fight_tab()): return print('Season is over. No need to check if ended.')
        bbox = [0.42578125, 0.78056, 0.480859375, 0.8354169]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference('start', t['text']):
                moveAndClick(t['position'])
    
    @staticmethod
    def _check_attack_report():
        bbox = [0.4171875, 0.21, 0.499609375, 0.27361]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['attack'], t['text']):
                close_pos = Screen.get_pos([0.77421875, 0.2604167])
                return moveAndClick(close_pos)
        # TODO when accept button will be available, click on it by taking the text or by position

    @staticmethod
    def _check_and_collect_rewards():
        bbox = [0.462890625, 0.146527, 0.527734375, 0.195834]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['collect'], t['text'].lower()):
                multiple_click(t['position'])
                delay(1)
                Popup.check_popup_chest()
                delay(5)
                check_if_ok()
                delay(1)
                