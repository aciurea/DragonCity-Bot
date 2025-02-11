from close import check_if_ok
from hatch import Hatch
from position_map import Position_Map
from screen import Screen
from move import moveAndClick
from utils import delay, exists, getImagePositionRegion, get_screen_resolution


class Breed:
    screen_res = get_screen_resolution()
    rock_pos = Screen.get_pos([0.4109375, 0.7324074074])
    tree_pos = Screen.get_pos([0.29427083, 0.67685185])
    breed_button_pos = Screen.get_pos([0.496875, 0.748148])

    _re_breed_btn = None

    def _get_re_breed():
        if not Breed._re_breed_btn:
            _base = './img/breed'
            path = f'{_base}/{Breed.screen_res}_re_breed.png'
            bbox = [*Screen.get_pos([0.73125, 0.799074]), *Screen.get_pos([0.824479167, 0.95])]
            Breed._re_breed_btn = getImagePositionRegion(path, *bbox, .8, 1)
        return Breed._re_breed_btn

    def _re_breed():
        delay(.5)
        btn = Breed._get_re_breed()
        if not exists(btn): return print('Rebreed button not found')

        moveAndClick(btn)
        delay(1)
        moveAndClick(Breed.breed_button_pos)
        check_if_ok()

    def clear_hatchery():
        if not exists(Position_Map.center_map()):
            return check_if_ok()
        Hatch.sell_egg()

    def start_fresh():
        Breed.clear_hatchery()

        for breed_place in [Breed.rock_pos, Breed.tree_pos]:
            if not exists(Position_Map.center_map()): return check_if_ok()
            moveAndClick(breed_place)
            delay(1)
        check_if_ok()
        # in case the tree and rock had eggs, wait 12 secs to hatch and clear them.
        delay(12)
        Breed.clear_hatchery()

    @staticmethod
    def breed(work_type="feed", times=15):
        Breed.start_fresh()
        first_time = True

        while times > 0:
            times -= 1

            for breed_place in [Breed.rock_pos, Breed.tree_pos]:
                if not exists(Position_Map.center_map()): check_if_ok()
                moveAndClick(breed_place)
                Breed._re_breed()
                delay(.2)

            delay(2.5)
            if first_time: delay(5)

            if work_type == "breed": Breed.clear_hatchery()
            else: Hatch.place_egg(work_type)

            # collect phase
            for breed_place in [Breed.rock_pos, Breed.tree_pos]:
                if not exists(Position_Map.center_map()): check_if_ok()
                moveAndClick(breed_place)
                delay(1)
            check_if_ok()
            first_time = False
            print('Breed cycle done')
