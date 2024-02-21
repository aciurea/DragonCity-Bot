
from arena import Arena
from close import check_if_ok
from collectFood import collect_food
from open import open_app
from utils import dragMapToCenter


def start_app():
    do_work = [
        open_app,
        collect_food,
        Arena.enter_battle
        # More work can be added here
    ]

    for work in do_work:
        work()
        check_if_ok()
        dragMapToCenter()
    