import random
import time
import concurrent.futures

from screen import Screen
from move import moveAndClick
from utils import delay, exists, getImagePositionRegion, get_screen_resolution, is_in_time

text = {
    'select': 'select',
    'selectdragon': 'selectdragon',
}

attacks = {
    'GammaExplosion': 'GammaExplosion',
    'DivineSacrifice': 'DivineSacrifice',
}


class Battle:
    base = './img/battle'
    screen_res = get_screen_resolution()

    @staticmethod
    def get_speed_btn():
        position = [*Screen.get_pos([0.0197916, 0.238]), *Screen.get_pos([0.07, 0.3185185])]

        path = f'{Battle.base}/{Battle.screen_res}_x4.png'

        return getImagePositionRegion(path, *position, .8, 1)

    @staticmethod
    def _on_team_selection():
        bbox = [0.3947916, 0.03148148, 0.472395835, 0.0935185]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['select'], t['text']): return t['position']
        return [-1]

    @staticmethod
    def get_play_button():
        position = [*Screen.get_pos([0.0197916, 0.15]), *Screen.get_pos([0.06979167, 0.234])]
        path = f'{Battle.base}/{Battle.screen_res}_play.png'

        return getImagePositionRegion(path, *position, .8, 1)

    @staticmethod
    def _is_in_battle():
        work = [Battle.get_play_button, Battle.get_speed_btn, Battle._on_team_selection]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            btns = executor.map(lambda func: func(), work)
            for btn in btns:
                if exists(btn): return True
        return False

    @staticmethod
    def wait_for_battle_to_start():
        retries = 15
        while retries > 0:
            retries -= 1
            if Battle._is_in_battle(): return print('Ready to fight!')
            delay(1)
        raise Exception('Battle didn`t start in time....')

    @staticmethod
    def get_new_dragon_btn():
        bbox = [0.09895834, 0.83425925, 0.89375, 0.899074]

        dragons_life_bbox = [0.0885416, 0.76851851, 0.91822916, 0.826851851]

        text_positions = Screen.get_text_pos(dragons_life_bbox)
        print(text_positions)

        text_positions = Screen.get_text_pos(bbox)

        lst = []

        for t in text_positions:
            if Screen.is_match(text['selectdragon'], t['text']):
                lst.append(t['position'])

        return random.choice(lst) if lst else [-1]

    @staticmethod
    def _get_swap_button():
        position = [*Screen.get_pos([0.00729167, 0.7167]), *Screen.get_pos([0.0645834, 0.83518518])]
        path = f'{Battle.base}/{Battle.screen_res}_swap.png'

        return getImagePositionRegion(path, *position, .8, 1)

    @staticmethod
    def change_dragon():
        swap_btn = Battle._get_swap_button()
        if exists(swap_btn):
            moveAndClick(swap_btn)
            delay(1)
        new_dragon = Battle.get_new_dragon_btn()
        if not exists(new_dragon): return print('Dragon not found')
        moveAndClick(new_dragon)

    @staticmethod
    def fight(change_dragon=True):
        Battle.wait_for_battle_to_start()

        if not change_dragon: return Battle._battle_with_no_change_dragon()
        start = time.time()
        is_last_dragon = False

        # 6 minutes is more than enough
        while is_in_time(start, 300):
            st = time.time()
            if not Battle._is_in_battle(): return
            print(f'[LOG] Battle._is_in_battle: {time.time() - st}')
            if is_last_dragon:
                delay(2)
                continue

            # TODO need a smart way to fight. This will be work in progress. No only hit 3 times.
            # TODO check for critical hits from my dragon
            # TODO maybe remember my dragon life and check If I got a critical hit and change it if is the case.
            if not Battle._can_dragon_support_an_attack():
                st = time.time()
                Battle.change_dragon()
                print(f' Battle.change_dragon: {time.time() - st}')
                delay(1)

            Battle._attack()

            st = time.time()
            if not Battle._wait_for_oponent_to_attack():
                print(f'[LOG] Battle._wait_for_oponent_to_attack: {time.time() - st}')
                st = time.time()
                Battle.change_dragon()
                print(f'[LOG] Battle.change_dragon: {time.time() - st}')
                continue

            # NEED to check if last dragon that is defeated is selected automatically
            st = time.time()
            if not exists(Battle._get_swap_button()):
                print(f'[LOG] Battle._get_swap_button: {time.time() - st}')
                is_last_dragon = True
                st = time.time()
                moveAndClick(Battle.get_play_button())
                print(f'[LOG] Battle.get_play_button: {time.time() - st}')
        print('Fight is over!')

    @staticmethod
    def _attack():
        best_attack = Battle._get_attack()
        if best_attack: return moveAndClick(best_attack)

        play_btn = Battle.get_play_button()
        moveAndClick(play_btn)
        delay(.3)
        # pause fight
        moveAndClick(play_btn)

    @staticmethod
    def _can_dragon_support_an_attack():
        st = time.time()
        dragon_life = Battle._get_dragon_life()
        print(f'[LOG] Battle._get_dragon_life: {time.time() - st}')
        if dragon_life is None: return True

        return (dragon_life[0] / dragon_life[1]) > 0.3

    @staticmethod
    def _get_dragon_life():
        bbox = [0.2364583, 0.13518518, 0.38802083, 0.1768518]
        text_positions = Screen.get_text_pos(bbox)

        if len(text_positions) == 2:
            return [int(text_positions[0]['text']), int(text_positions[1]['text'])]

        return None

    @staticmethod
    def _wait_for_oponent_to_attack():
        retries = 5
        while retries > 0:
            if Battle._get_ico_in_battle(): return True
            if Battle._get_ico_in_team_selection(): return False
            delay(1)
            retries -= 1
        return False

    @staticmethod
    def _get_ico_in_team_selection():
        path = f'{Battle.base}/{Battle.screen_res}_ico.png'
        pos = [*Screen.get_pos([0.253125, 0.6759259]), *Screen.get_pos([0.9671875, 0.774074])]

        return exists(getImagePositionRegion(path, *pos, .8, 1))

    @staticmethod
    def _get_ico_in_battle():
        path = f'{Battle.base}/{Battle.screen_res}_ico.png'
        pos = [*Screen.get_pos([0.840625, 0.8537037]), *Screen.get_pos([0.8921875, 0.93])]

        return exists(getImagePositionRegion(path, *pos, .8, 1))

    @staticmethod
    def _battle_with_no_change_dragon():
        start = time.time()
        moveAndClick(Battle.get_play_button())

        while is_in_time(start, limit=120):
            if not Battle._is_in_battle(): return
            delay(2)

    @staticmethod
    def _get_attack():
        bbox = [0.1734375, 0.856481, 0.28125, 0.9527]

        text_positions = Screen.get_text_pos(bbox)
        print(text_positions)

        if len(text_positions) > 1: return None

        for t in text_positions:
            if Screen.is_match(attacks['GammaExplosion'], t['text']):
                return t['position']

    @staticmethod
    def _get_boost_attack():
        bbox = [*Screen.get_pos([0.14947916, 0.8185]), *Screen.get_pos([0.838, 0.86481])]
        path = f'{Battle.base}/{Battle.screen_res}_boost_attack.png'

        pos = getImagePositionRegion(path, *bbox, .8, 1)

        # TODO check if the attack has no affect and don't use it on this dragon.
        if exists(pos):
            return [pos[0], pos[1] + 30]
        return None
