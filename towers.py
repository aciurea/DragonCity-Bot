
from utils import delay, exists
from position_map import Position_Map
from screen import Screen
from move import multiple_click, moveAndClick
from close import check_if_ok


class Towers:
    gems_tower = Screen.get_pos([0.7359375, 0.206481])
    food_tower = Screen.get_pos([0.8625, 0.3])
    breed_tower = Screen.get_pos([0.821875, 0.68056])
    collect_tower = Screen.get_pos([0.6640625, 0.85])
    resource_btn_pos = Screen.get_pos([0.777083, 0.867])

    @staticmethod
    def activate_towers():
        if not exists(Position_Map.center_map()):
            return print('Something wrong with the map.')
        towers_pos = [
            Towers.gems_tower,
            Towers.food_tower,
            Towers.collect_tower,
            # Towers.breed_tower,
        ]

        for tower_pos in towers_pos:
            multiple_click(tower_pos, 5, 0.01)
            delay(.5)
            moveAndClick(Towers.resource_btn_pos)
            delay(.5)
            check_if_ok()
            Position_Map.center_map()
        print('Finish activating towers')
