
from alliance import Alliance
from arena import Arena
from claim_all import claim_all
from close import check_if_ok
from farm import Farm
from gold import Gold
from daily_browser_collect import Daily_Browser_Collect
from league import League
from open import OpenApp
from orbs import Orbs
from shop import Shop
from towers import Towers
from utils import get_int
from daily_treasure import Daily_Treasure
from events_collection import Events_Collection
from wizard import Wizard
from position_map import Position_Map

import time

# default screen resolution when no monitor is connected is 1024x768


def start_working():
    do_work = [
        OpenApp.open_app,
        claim_all,
        Towers.activate_towers,
        Farm.collect_food,
        Gold.collectGold,
        Orbs.collect_orbs,
        Shop.open_shop,
        Daily_Treasure.collect_daily_treasure,
        Daily_Browser_Collect.collect_daily_streak,
        Alliance.open_alliance,
        League.fight_league,
        Arena.enter_battle,
        Wizard.open_wizard,
        Events_Collection.collect_events,
        OpenApp._close_app,
    ]
    str_actions = "Actions with time are: \n\n"

    for i, work in enumerate(do_work):
        start = time.time()
        work()
        end = time.time()
        str_actions += f"[{str(work.__name__)}] took {str(get_int(end - start))} seconds\n"
        if i == len(do_work) - 1: return str_actions

        check_if_ok()
        Position_Map.center_map()
    return str_actions
