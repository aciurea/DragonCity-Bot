
from arena import Arena
from close import check_if_ok
from collectFood import collect_food
from collectGold import collectGold
from open import open_app, close_app
from shop import Shop
from towers import activate_towers
from tv import TV
from utils import dragMapToCenter


def start_working():
    do_work = [
        open_app,
        activate_towers,
        collect_food,
        collectGold,
        Shop.open_shop,
        TV.open_tv,
        Arena.enter_battle,
        # More work can be added here
        close_app
    ]

    for i, work in enumerate(do_work):
        work()
        if i == len(do_work) - 1: return
        check_if_ok()
        dragMapToCenter()
    