
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
from utils import dragMapToCenter
from daily_treasure import collect_daily_treasure
from events_collection import Events_Collection

def start_working():
    do_work = [
        open_app,
        claim_all,
        activate_towers,
        collect_food,
        collectGold,
        Orbs.collect_orbs,
        Shop.open_shop,
        collect_daily_treasure,
        # League.enter_league,
        Alliance.open_alliance,
        Heroic.race,
        Daily_Collect.collect,
        Arena.enter_battle,
        Quest.open_quest,
        Events_Collection.collect_events,

        # TV.open_tv,
        # Runner.run,
        # Habitat.buy_habitat,

        # lambda: Breed.breed(),
        # Quest.open_quest,
        # More work can be added here
        # Tree of life
        close_app
    ]

    for i, work in enumerate(do_work):
        work()
        if i == len(do_work) - 1: return
        check_if_ok()
        dragMapToCenter()
    