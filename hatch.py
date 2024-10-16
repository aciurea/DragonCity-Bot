from move import moveAndClick, multiple_click
from timers import delay
from close import check_if_ok
from screen import Screen
from position_map import Position_Map
from utils import exists, get_monitor_quarters, getImagePositionRegion, get_screen_resolution

class Hatch:
    dragonarium_pos = [1773, 473]
    screen_res = get_screen_resolution()
    mon_quarters = get_monitor_quarters()
    hatchery_pos = Screen.get_pos([0.346153, 0.639375])
    terra_habitat = Screen.get_pos([0.334375, 0.7167])
    sell_egg_btn_from_habitat = Screen.get_pos([0.8515625, 0.89537037])
    confirm_sell_btn = Screen.get_pos([0.55677083, 0.6879629])
    place_btn_pos = Screen.get_pos([0.544270834, 0.6861])

    def _get_terra_egg():
        _base =  './img/breed'
        path = f'{_base}/{Hatch.screen_res}_terra_egg.png'

        return getImagePositionRegion(path, *Hatch.mon_quarters['4thRow'], .8, 1)

    def sell_egg():
        moveAndClick(Hatch.hatchery_pos)
        egg = Hatch._get_terra_egg()

        if exists(egg):
            moveAndClick(egg)
            delay(.5)
            moveAndClick(Screen.get_pos([0.681153846, 0.6825])) # sell egg btn
            delay(.5)
            moveAndClick(Screen.get_pos([0.55730769, 0.676875])) # confirm sell egg btn
            return Hatch.sell_egg()

    def sell_dragon(work_type):
        _base = './img/breed/'
        path = f'{_base}/{Hatch.screen_res}_dragon.png'
        dragon_pos_in_habitat = getImagePositionRegion(path, *Hatch.mon_quarters['4thRow'], .8, 1)

        if exists(dragon_pos_in_habitat):
            moveAndClick(dragon_pos_in_habitat)
            delay(.5)
            if work_type == 'feed': Hatch.feed_dragon()
            moveAndClick(Hatch.sell_egg_btn_from_habitat)
            delay(.5)
            moveAndClick(Hatch.confirm_sell_btn)
            delay(.5)
            return Hatch.sell_dragon(work_type)

    def feed_dragon():
        feed_pos = Screen.get_pos([0.26197916, 0.8787037])
        multiple_click(feed_pos, 8, .3)
      
    @staticmethod
    def place_egg(work_type):
        if not exists(Position_Map.center_map()):
            check_if_ok()
            return
        moveAndClick(Hatch.hatchery_pos)
        egg = Hatch._get_terra_egg()

        if exists(egg):
            moveAndClick(egg)
            delay(.5)
            moveAndClick(Hatch.place_btn_pos) # place egg btn
            delay(1)
            Position_Map.center_map()
            delay(.2)
            moveAndClick(Hatch.terra_habitat)
            delay(1)
            Hatch.sell_dragon(work_type)

            return Hatch.place_egg(work_type)

    # @staticmethod
    # def hatch_dragon_in_dragonarium(egg = C.BREED_TERRA_EGG):
    #     Position_Map.center_map()
    #     moveAndClick(Hatch.hatchery_pos)

    #     flame_egg = getImagePositionRegion(egg, *Hatch.mon_quarters['4thRow'], .8, 1)

    #     if not exists(flame_egg): return check_if_ok()
    #     moveAndClick(flame_egg)
    #     delay(.5)
    #     moveAndClick(Hatch.place_btn_pos)
    #     delay(2)
    #     moveAndClick(Hatch.dragonarium_pos)
