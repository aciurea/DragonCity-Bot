import random

from close import Close
from position_map import Position_Map
from utils import delay, exists
from move import moveAndClick, multiple_click
from screen import Screen

from screeninfo import get_monitors

text = {
    'play': 'play',
    'claim': 'claimi',
    'claim&quit': 'claim',
    'claimall': 'claimall'
}


class Wizard:
    res = get_monitors()[0]
    # relative to the center point.
    wizard_static_pos = Screen.get_pos([0.8203125, 0.14723])
    wizard_static_quit_when_fails = Screen.get_pos([0.34270834, 0.7842593])

    @staticmethod
    def open_wizard():
        if not exists(Position_Map.center_map()):
            return
        delay(1)
        moveAndClick(Wizard.wizard_static_pos)
        delay(1)
        play_btn = Wizard._get_play_btn()

        if not play_btn:
            Close.check_if_ok()
            return print('Wizard Already played')

        moveAndClick(play_btn)
        delay(10)
        Wizard._play_wizard()
        Wizard._claim_and_quit_wizard()
        Close.check_if_ok()

    @staticmethod
    def _play_wizard():
        tries = 3

        balls = [
            Screen.get_pos([0.3322916, 0.427]),
            Screen.get_pos([0.4354167, 0.5138]),
            Screen.get_pos([0.56875, 0.512963]),
            Screen.get_pos([0.66979167, 0.42962963])
        ]

        while tries >= 0:
            tries -= 1
            ball = random.choice(balls)
            multiple_click(ball)
            delay(7)

            if not exists(Wizard._get_claim_btn()):
                return Close.check_if_ok()

    @staticmethod
    def _claim_and_quit_wizard():
        claim_btn = Wizard._get_claim_btn()
        if not exists(claim_btn):
            Close.check_if_ok()
            delay(1)
            moveAndClick(Wizard.wizard_static_quit_when_fails)

        moveAndClick(claim_btn)
        delay(1)
        claim_and_quit = Wizard._get_claim_and_quit_btn()

        if not exists(claim_and_quit):
            return Close.check_if_ok()

        moveAndClick(claim_and_quit)
        delay(1)
        claim_all = Wizard._get_claim_all_btn()

        if not exists(claim_all):
            return Close.check_if_ok()
        moveAndClick(claim_all)

    @staticmethod
    def _get_claim_all_btn():
        bbox = [0.44583, 0.77, 0.55364583, 0.8287037]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claimall'], t['text']):
                return t['position']
        return [-1]

    @staticmethod
    def _get_claim_and_quit_btn():
        bbox = [0.30364583, 0.781481481, 0.3734375, 0.8481481]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claim&quit'], t['text']):
                return t['position']
        return [-1]

    @staticmethod
    def _get_claim_btn():
        bbox = [0.849479167, 0.8527, 0.9302083, 0.9231481]
        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['claim'], t['text']):
                return t['position']
        return [-1]

    @staticmethod
    def _get_play_btn():
        bbox = [0.46510416, 0.737, 0.53, 0.80278]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match_with_one_difference(text['play'], t['text']):
                return t['position']
        return None
