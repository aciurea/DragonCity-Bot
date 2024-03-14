
from arena import Arena
from close import check_if_ok
from collectFood import collect_food
from collectGold import collectGold
from habitat import Habitat
from heroic import Heroic
from open import open_app, close_app
from shop import Shop
from towers import activate_towers
from tv import TV
from utils import dragMapToCenter
from daily_treasure import collect_daily_treasure

def start_working():
    do_work = [
        open_app,
        activate_towers,
        collect_food,
        collectGold,
        Shop.open_shop,
        collect_daily_treasure,
        Heroic.race,
        Arena.enter_battle,
        TV.open_tv,
        Habitat.buy_habitat,
        # More work can be added here
        # collect daily chest
        # fight in league
        # Tree of life
        close_app
    ]

    for i, work in enumerate(do_work):
        work()
        if i == len(do_work) - 1: return
        check_if_ok()
        dragMapToCenter()
    