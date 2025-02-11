from battle import Battle
from close import Close
from utils import delay, exists, getImagePositionRegion, get_screen_resolution
from position_map import Position_Map
from move import moveAndClick
from screen import Screen

text = {
    'refill': 'refill',
}


class League:
    battle_pos = Screen.get_pos([0.30859375, 0.868056])
    league_pos = Screen.get_pos([0.290625, 0.44074])
    claim_pos = Screen.get_pos([0.49010416, 0.79])
    screen_res = get_screen_resolution()

    @staticmethod
    def fight_league():
        if not exists(Position_Map.center_map()): return
        delay(.5)
        moveAndClick(League.battle_pos)
        delay(.5)
        moveAndClick(League.league_pos)
        delay(3)
        if not League._is_league_ready():
            print('League not ready.')
            Close.check_if_ok()
            return 0
        remaining_oponents = League._open_battle()
        Close.check_if_ok()
        delay(1)
        if remaining_oponents == 1: return League.fight_league()

    @staticmethod
    def _open_battle():
        retries = 3
        while retries > 0:
            retries -= 1

            position = [*Screen.get_pos([0.016, 0.35648148148]), *Screen.get_pos([0.98489583, 0.849074074])]

            path = f'./img/battle/{League.screen_res}_oponent.png'
            oponent = getImagePositionRegion(path, *position, .8, 1)

            if not exists(oponent) or not League._is_league_ready(): return 0

            moveAndClick(oponent)
            Battle.fight(change_dragon=False)
            moveAndClick(League.claim_pos)
            delay(1)
        return retries

    @staticmethod
    def _is_league_ready():
        bbox = [0.809, 0.262, 0.8765625, 0.32]

        text_positions = Screen.get_text_pos(bbox, custom_filter=Screen.convert_to_gray)
        for t in text_positions:
            if Screen.is_match(text['refill'], t['text']):
                return False
        return True
