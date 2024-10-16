import time
import concurrent.futures

from screen import Screen
from move import moveAndClick
from utils import delay, exists, getImagePositionRegion, get_screen_resolution, is_in_time
from close import Close

text = {
    'select': 'select',
}

attacks = {
    'GammaExplosion': 'GammaExplosion',
    'DivineSacrifice': 'DivineSacrifice',
}


class Battle:
    base = './img/battle'
    screen_res = get_screen_resolution()
    hit_with_special_attack = False
    remaining_turns_for_boost_attack = -1

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
            if Screen.is_match_with_one_difference(text['select'], t['text']):
                return t['position']
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
        select_bboxes = [
            [0.1, 0.83, 0.1697916, 0.892],
            [0.42552083, 0.83, 0.4947916, 0.892],
            [0.746875, 0.83, 0.81510416, 0.892],
        ]
        critical_attack_positions = Battle._get_in_team_critical_attack_positions()
        dragon_life_bboxes = [
            [0.0875, 0.7, 0.25625, 0.815],
            [0.40677083, 0.7, 0.5859375, 0.815],
            [0.7239583, 0.7, 0.9114583, 0.815],
        ]
        best_dragons = []

        if len(critical_attack_positions) > 0:
            for position in critical_attack_positions:
                dragon_life_text = Screen.get_text_pos(dragon_life_bboxes[position])

                if len(dragon_life_text) == 2:
                    remaing = int(dragon_life_text[0]['text'])
                    if remaing > 0:
                        best_dragons.append([position, remaing])
            best_dragons = sorted(best_dragons, key=lambda x: x[1], reverse=True)
        else:
            for i, bbox in enumerate(dragon_life_bboxes):
                dragon_life_text = Screen.get_text_pos(bbox)
                if len(dragon_life_text) == 2:
                    remaing = int(dragon_life_text[0]['text'])
                    if remaing > 0:
                        best_dragons.append([i, remaing])
            best_dragons = sorted(best_dragons, key=lambda x: x[1], reverse=True)

        for best_dragon in best_dragons:
            select_position = Screen.get_text_pos(select_bboxes[best_dragon[0]])

            for t in select_position:
                if Screen.is_match(text['select'], t['text']):
                    return moveAndClick(t['position'])
            return Close.check_if_ok()

    @staticmethod
    def _get_swap_button():
        position = [*Screen.get_pos([0.00729167, 0.7167]), *Screen.get_pos([0.0645834, 0.83518518])]
        path = f'{Battle.base}/{Battle.screen_res}_swap.png'

        return getImagePositionRegion(path, *position, .8, 1)

    @staticmethod
    def change_dragon():
        swap_btn = Battle._get_swap_button()
        if not exists(swap_btn):
            if not exists(Battle._on_team_selection()): return
        else: moveAndClick(swap_btn)
        delay(1)
        Battle.get_new_dragon_btn()

    @staticmethod
    def fight(change_dragon=True):
        Battle.wait_for_battle_to_start()

        if not change_dragon: return Battle._battle_with_no_change_dragon()
        start = time.time()
        is_last_dragon = False

        # 6 minutes is more than enough
        while is_in_time(start, 300):
            if not Battle._is_in_battle(): return
            if is_last_dragon:
                delay(1)
                continue

            if Battle._wait_for_attack_ready() and not exists(Battle._get_swap_button()):
                is_last_dragon = True
                moveAndClick(Battle.get_play_button())
                continue

            # TODO check for critical hits from my dragon
            # if not Battle._can_dragon_support_an_attack():

            # TODO when chaning the dragon it happens for the oponent to attack again, leading to a missclick.
            Battle.change_dragon()
            Battle._attack()
        print('Fight is over!')

    @staticmethod
    def _attack():
        best_attack = Battle._get_attack()
        if best_attack:
            Battle.hit_with_special_attack = True
            return moveAndClick(best_attack)
            # Battle.remaining_turns_for_boost_attack = Battle._get_remaing_turns_for_boost_attack()

        play_btn = Battle.get_play_button()
        moveAndClick(play_btn)
        # Battle.remaining_turns_for_boost_attack -= 1
        delay(.3)
        # pause fight
        moveAndClick(play_btn)

    @staticmethod
    def _can_dragon_support_an_attack():
        dragon_life = Battle._get_dragon_life()
        if dragon_life is None:
            return Battle._has_critical_attack_in_battle()

        return Battle._has_critical_attack_in_battle() or (dragon_life[0] / dragon_life[1]) > 0.3

    @staticmethod
    def _get_dragon_life():
        bbox = [0.2364583, 0.13518518, 0.38802083, 0.1768518]
        text_positions = Screen.get_text_pos(bbox)

        if len(text_positions) == 2:
            return [int(text_positions[0]['text']), int(text_positions[1]['text'])]

        return None

    @staticmethod
    def _wait_for_attack_ready():
        retries = 10
        while retries > 0:
            if Battle._get_ico_in_battle(): return True
            if Battle._get_ico_in_team_selection(): return False
            delay(.5)
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
        # TODO improve best attack by checking exactly the text.
        text_positions = Screen.get_text_pos(bbox)

        if len(text_positions) > 1: return None

        for t in text_positions:
            for attack in attacks:
                if Screen.is_match(attacks[attack], t['text']):
                    return t['position']
        return None

    @staticmethod
    def _get_boost_attack():
        bbox = [*Screen.get_pos([0.14947916, 0.8185]), *Screen.get_pos([0.838, 0.86481])]
        path = f'{Battle.base}/{Battle.screen_res}_boost_attack.png'

        pos = getImagePositionRegion(path, *bbox, .8, 1)

        # TODO check if the attack has no affect and don't use it on this dragon.
        if exists(pos):
            return [pos[0], pos[1] + 30]
        return None

    @staticmethod
    def _has_critical_attack_in_battle():
        path = f'{Battle.base}/{Battle.screen_res}_critical_attack.png'

        position = [*Screen.get_pos([0.3, 0.824]), *Screen.get_pos([0.8421875, 0.9083])]

        return exists(getImagePositionRegion(path, *position, .8, 1))

    @staticmethod
    def _get_in_team_critical_attack_positions():
        bboxes = [
            [*Screen.get_pos([0.027083, 0.6787]), *Screen.get_pos([0.22447916, 0.77])],
            [*Screen.get_pos([0.3515625, 0.6787]), *Screen.get_pos([0.547916, 0.77])],
            [*Screen.get_pos([0.66875, 0.6787]), *Screen.get_pos([0.8697916, 0.77])],
        ]

        dragons_with_critical_attack = []

        for i, bbox in enumerate(bboxes):
            path = f'{Battle.base}/{Battle.screen_res}_team_critical_attack.png'

            pos = getImagePositionRegion(path, *bbox, .8, 1)

            if exists(pos):
                dragons_with_critical_attack.append(i)
        return dragons_with_critical_attack

    @staticmethod
    def _get_remaing_turns_for_boost_attack():
        bbox = [0.1802083, 0.9, 0.2677083, 0.95185]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            return Battle.get_digits_from_string(t['text'])
        return 0

    @staticmethod
    def get_digits_from_string(s):
        return ''.join([char for char in s if char.isdigit()])
