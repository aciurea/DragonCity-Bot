
from alliance import Alliance
from arena import Arena
from breed import Breed
from claim_all import claim_all
from close import check_if_ok
from farm import Farm
from gold import Gold
from daily_browser_collect import Daily_Browser_Collect
from habitat import Habitat
from heroic import Heroic
from league import League
from open import OpenApp
from orbs import Orbs
from quest import Quest
from runner import Runner
from shop import Shop
from towers import Towers
from tv import TV
from utils import get_int
from daily_treasure import Daily_Treasure
from events_collection import Events_Collection
from wizard import Wizard
from move import center_map
from puzzle import Puzzle
from clear_event import ClearEvent

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
        Arena.enter_battle,
        League.enter_league,

        ClearEvent.skip_event,
        # Heroic.race,
        # Quest.open_quest,
        Runner.run,
        Wizard.open_wizard,
        Puzzle.open_puzzle,
        Events_Collection.collect_events,

        # TV.open_tv,
        # Habitat.buy_habitat,
        # More work can be added here
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
        center_map()
    return str_actions
