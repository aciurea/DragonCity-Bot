from breed import Breed
from close import Close
from league import League
from farm import Farm
from utils import delay, exists
from move import moveAndClick, multiple_click
from screen import Screen
from position_map import Position_Map
from battle import Battle
from popup import Popup

text = {
    'fight': 'fight',
    'laprewards': 'laprewards',
    'getitembyfeeding': 'getitembyfeeding',
    'winleaguebattles': 'winleaguebattles',
    'GETITEMFROMBATTLES': 'GETITEMFROMBATTLES',
    'GETITEMBYCOLLECTING': 'GETITEMBYCOLLECTING',
    'hatch': 'GETITEMBYHATCHING',
    'breed': 'breed',
    'FIGHTI': 'FIGHTI',
}


class Heroic:
    bbox_progress = [
        [0.9203125, 0.27129, 0.97239583, 0.3259259],
        [0.9203125, 0.4296296, 0.97239583, 0.4796296296],
    ]
    heroic_race_center_pos = Screen.get_pos([0.5578125, 0.3629629])

    def race():
        if not exists(Position_Map.center_map()):
            return print('Something when wrong trying to do the race.')
        multiple_click(Heroic.heroic_race_center_pos, 5, 0.1)
        delay(1)

        if not Heroic._is_heroic_race():
            League.fight_league(),
            return

        # TODO: claim node
        # TODO: close extra popups
        # TODO: do free spin.
        # TODO: if node is higher, pay with gemes the last battle. is 3 gems.
        Heroic._claim_node()
        missions = Heroic._get_missions()
        Close.check_if_ok()
        delay(1)
        for mission in missions:
            mission()

    @staticmethod
    def _is_heroic_race():
        # TODO when starting the race the popups are different
        # TODO the same when collecting a lap reward. Try to extra more text to identify heroic race.
        bbox = [0.0177083, 0.81759, 0.1171875, 0.861]

        text_positions = Screen.get_text_pos(bbox, gray_mode=True)
        for t in text_positions:
            if Screen.is_match(text['laprewards'], t['text']):
                return True
        return False

    @staticmethod
    def _get_missions():
        bbox_missions = [
            [0.76875, 0.26759259, 0.915625, 0.34259259],
            [0.76875, 0.4231481, 0.915625, 0.492592],
            [0.76875, 0.26759259, 0.915625, 0.34259259],
        ]

        missions = []
        fight_in_battle = False

        for bbox in bbox_missions:
            text_positions = Screen.get_text_pos(bbox)
            for t in text_positions:
                if Screen.is_match(text['getitembyfeeding'], t['text']):
                    missions.append(lambda: Breed.breed('feed', 20))
                    break
                if Screen.is_match(text['winleaguebattles'], t['text']):
                    missions.append(lambda: League.fight_league())
                    break
                if Screen.is_match(text['GETITEMBYCOLLECTING'], t['text']):
                    missions.append(lambda: Farm.fast_collect(times=20))
                    break
                if Screen.is_match(text['GETITEMFROMBATTLES'], t['text']):
                    fight_in_battle = True
                    break
                if Screen.is_match(text['hatch'], t['text']):
                    missions.append(lambda: Breed.breed('sell', 20))
                    break
                else:
                    missions.append(lambda: Breed.breed('breed', 20))
                    break

        if fight_in_battle:
            Heroic._fight_in_heroic()
        return missions

    @staticmethod
    def _fight_in_heroic():
        bbox = [0.81614583, 0.3379629, 0.903125, 0.7148148]
        text_positions = Screen.get_text_pos(bbox)
        back_btn = Screen.get_pos([0.04114583, 0.0879629])
        actions = [
            lambda: delay(1),
            lambda: moveAndClick(Screen.get_pos([0.17552083, 0.735185])),
            lambda: moveAndClick(Screen.get_pos([0.4296875, 0.354629629])),
            lambda: moveAndClick(Screen.get_pos([0.49583, 0.8972])),
            lambda: Battle.fight(change_dragon=False),
            lambda: moveAndClick(back_btn)
        ]

        for t in text_positions:
            if Screen.is_match(text['fight'], t['text']):
                moveAndClick(t['position'])
                delay(2)
                bbox = [0.1, 0.7259, 0.95, 0.83]

                text_positions = Screen.get_text_pos(bbox, gray_mode=True)
                for t in text_positions:
                    if Heroic._contains_digit(t['text']): return moveAndClick(back_btn)
                    if Screen.is_match(text['FIGHTI'], t['text']):
                        moveAndClick(t['position'])
                        for action in actions:
                            action()
                            delay(1)
                        return

    @staticmethod
    def _contains_digit(s):
        return any(char.isdigit() for char in s)

    @staticmethod
    def _claim_node():
        bbox = [0.4578125, 0.8009259259259259, 0.54739583, 0.874]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match(text['claim'], t['text']):
                moveAndClick(t['position'])
                delay(1)
                Popup.check_popup_chest()
