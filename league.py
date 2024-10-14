from battle import Battle
from close import check_if_ok
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
    claim_pos = Screen.get_pos([0.35677083, 0.7824074])
    screen_res = get_screen_resolution()

    @staticmethod
    def enter_league():
        if not exists(Position_Map.center_map()): return
        delay(.5)
        moveAndClick(League.battle_pos)
        delay(.5)
        moveAndClick(League.league_pos)
        delay(2)
        remaining_oponents = League._open_battle()
        check_if_ok()
        if remaining_oponents > 0: return League.enter_league()

    @staticmethod
    def _open_battle():
        tries = 3
        while tries > 0:
            tries -= 1
            if not League._is_league_ready():
                print('League not ready.')
                return 0

            position = [*Screen.get_pos([0.016, 0.35648148148]), *Screen.get_pos([0.98489583, 0.849074074])]

            _base_battle = './img/battle'
            path = f'{_base_battle}/{League.screen_res}_oponent.png'
            oponent = getImagePositionRegion(path, *position, .8, 1)

            if not exists(oponent):
                print('No oponent found.')
                return tries

            moveAndClick(oponent)
            Battle.fight(change_dragon=False)
            moveAndClick(League.claim_pos)
            delay(1)
        return tries

    @staticmethod
    def _is_league_ready():
        bbox = [0.808854167, 0.262037, 0.8765625, 0.32037037]

        text_positions = Screen.get_text_pos(bbox)
        for t in text_positions:
            if Screen.is_match_with_one_difference(text['refill'], t['text']):
                return False
        return True
