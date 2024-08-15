
from alliance import Alliance
from arena import Arena
from breed import Breed
from claim_all import claim_all
from close import check_if_ok
from collectFood import collect_food
from collectGold import collectGold
from daily_collect import Daily_Collect
from habitat import Habitat
from heroic import Heroic
from league import League
from open import open_app, close_app
from orbs import Orbs
from quest import Quest
from runner import Runner
from shop import Shop
from towers import activate_towers
from tv import TV
from utils import get_int
from daily_treasure import collect_daily_treasure
from events_collection import Events_Collection
from wizard import Wizard
from move import center_map
import time

def start_working():
    do_work = [
        open_app,
        claim_all,
        activate_towers,
        collect_food,
        collectGold,
        Orbs.collect_orbs,
        Events_Collection.collect_events,
        Shop.open_shop,
        collect_daily_treasure,
        League.enter_league,
        Alliance.open_alliance,
        # Heroic.race,
        Daily_Collect.collect,
        Arena.enter_battle,
        Quest.open_quest,
        Runner.run,
        Wizard.open_wizard,

        # TV.open_tv,
        # Habitat.buy_habitat,
        # More work can be added here
        # Tree of life
        close_app
    ]
    str_actions = "Actions with time are: \n\n"

    for i, work in enumerate(do_work):
        start = time.time()
        work()
        end = time.time()
        str_actions += f"Work {str(work.__name__)} took {str(get_int(end - start))} seconds\n"
        if i == len(do_work) - 1: return str_actions

        check_if_ok()
        center_map()
    return str_actions
    