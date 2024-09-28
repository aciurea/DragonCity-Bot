from breed import Breed
from close import Close
from league import League
from utils import delay, exists
from move import moveAndClick, multiple_click
from screen import Screen
from position_map import Position_Map

text = {
    'laprewards': 'laprewards',
    'getitembyfeeding': 'getitembyfeeding',
    'winleaguebattles': 'winleaguebattles',
}


class Heroic:
    bbox_progress = [
        [0.9203125, 0.27129, 0.97239583, 0.3259259],
        [0.9203125, 0.4296296, 0.97239583, 0.4796296296],
        [0.9203125, 0.27129, 0.97239583, 0.3259259],
    ]
    heroic_race_center_pos = Screen.get_pos([0.5578125, 0.3629629])

    def race():
        if not exists(Position_Map.center_map()):
            return print('Something when wrong trying to do the race.')
        multiple_click(Heroic.heroic_race_center_pos, 5, 0.1)
        delay(1)

        if not Heroic._is_heroic_race():
            League.enter_league(),
            print('Not in heroic race do League')
            return

        # TODO: claim node
        # TODO: close extra popups
        # TODO: fight in heroic arena
        # TODO: do free spin.
        # TODO: if node is higher, pay with gemes the last battle. is 3 gems.

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
            # [0.76875, 0.26759259, 0.915625, 0.34259259],
        ]

        missions = []

        for bbox in bbox_missions:
            text_positions = Screen.get_text_pos(bbox)

            for t in text_positions:
                if Screen.is_match(text['getitembyfeeding'], t['text']):
                    missions.append(lambda: Breed.breed('feed', 20))
                    break
                if Screen.is_match(text['winleaguebattles'], t['text']):
                    missions.append(lambda: League.enter_league())
                    break
        return missions
