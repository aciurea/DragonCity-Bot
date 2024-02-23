from utils import delay, dragMapToCenter, exists, get_monitor_quarters, getImagePositionRegion, moveAndClick
import constants as C

class Towers:
    mon = get_monitor_quarters()

    @staticmethod
    def greedy_tower():
        dragMapToCenter()

        tower  = getImagePositionRegion(C.TOWERS_RESOURCESS_TOWER, *Towers.mon['4thRow'], 0.8, 1)
        if not exists(tower): return print("No Greedy Tower found")
        moveAndClick(tower)

        delay(1)
        
        resources_btn = getImagePositionRegion(C.TOWERS_COLLECT_RESOURCES_BTN, *Towers.mon['4thRow'], 0.8, 1)
        if not exists(resources_btn): return 
        moveAndClick(resources_btn)
        print('Resources collected')

    @staticmethod
    def gems_towers():
        dragMapToCenter()

        tower  = getImagePositionRegion(C.TOWERS_GEMS_TOWER, *Towers.mon['top_right'], 0.8, 1)
        if not exists(tower): return print("No Gems Tower found")
        moveAndClick(tower)

        delay(1)
        
        resources_btn = getImagePositionRegion(C.TOWERS_GEMS_BTN, *Towers.mon['4thRow'], 0.8, 1)
        if not exists(resources_btn): return
        moveAndClick(resources_btn)
        print('Gems collected')

    @staticmethod
    def gold_tower():
        dragMapToCenter()

        tower  = getImagePositionRegion(C.TOWERS_GOLD_TOWER, *Towers.mon['top_left'], 0.8, 1)
        if not exists(tower): return print("No Gold Tower found")
        moveAndClick(tower)

        delay(1)

        resources_btn = getImagePositionRegion(C.TOWERS_BOOST_GOLD_BTN, *Towers.mon['4thRow'], 0.8, 1)
        if not exists(resources_btn): return
        moveAndClick(resources_btn)
        print('Gold boosted')

    @staticmethod
    def power_tower():
        dragMapToCenter()

        tower  = getImagePositionRegion(C.TOWERS_POWER_TOWER, *Towers.mon['bottom_right'], 0.8, 1)
        if not exists(tower): return print("No Power Tower found")
        moveAndClick(tower)

        delay(1)

        resources_btn = getImagePositionRegion(C.TOWERS_BOOST_COMBAT_BTN, *Towers.mon['4thRow'], 0.8, 1)
        if not exists(resources_btn): return

        moveAndClick(resources_btn)
        print('Power collected')

    @staticmethod
    def food_tower():
        dragMapToCenter()

        tower  = getImagePositionRegion(C.TOWERS_FOOD_TOWER, *Towers.mon['top_right'], 0.8, 1)
        if not exists(tower): return print("No Food Tower found")
        moveAndClick(tower)

        delay(1)

        resources_btn = getImagePositionRegion(C.TOWERS_BOOST_FOOD_BTN, *Towers.mon['4thRow'], 0.8, 1)
        if not exists(resources_btn): return 

        moveAndClick(resources_btn)
        print('Power collected')

def activate_towers():
    Towers.greedy_tower()
    Towers.gems_towers()
    Towers.gold_tower()
    Towers.power_tower()
    Towers.food_tower()


