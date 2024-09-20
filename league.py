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
        Position_Map.center_map()
        delay(.5)
        moveAndClick(League.battle_pos)
        delay(.5)
        moveAndClick(League.league_pos)
        delay(2)
        League._open_battle()
        check_if_ok()


    @staticmethod
    def _open_battle(times = 3):
        if times == 0: return print('League finished.')
        if not League._is_league_ready(): return print('League not ready.')

        position = [*Screen.get_pos([0.016, 0.35648148148]), *Screen.get_pos([0.98489583, 0.849074074])]

        _base_battle = './img/battle'
        path = f'{_base_battle}/{League.screen_res}_oponent.png'
        oponent = getImagePositionRegion(path, *position, .8, 1)

        if not exists(oponent): return print('No oponent found.')

        moveAndClick(oponent)
        Battle.fight(change_dragon=False)
        moveAndClick(League.claim_pos)

        return League._open_battle(times - 1)

    @staticmethod
    def _is_league_ready():
        bbox = [0.808854167, 0.262037, 0.8765625, 0.32037037]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['refill'], t['text']):
                return False
        return True
