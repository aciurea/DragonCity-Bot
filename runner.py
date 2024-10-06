from breed import Breed
from close import check_if_ok
from move import moveAndClick, multiple_click
from utils import delay, exists
from screen import Screen
from position_map import Position_Map


text = {
    'runner': 'runner',
    'Claim': 'Claim',
    'Complete': 'Complete',
    'claimed': 'claimed',
    'BREEDDRAGONS': 'BREEDDRAGONS',
    'FEEDYOURDRAGONS': 'FEEDYOURDRAGONS'
}


class Runner:
    runner_pos = Screen.get_pos([0.4296875, 0.19537])
    close_pos = Screen.get_pos([0.9546875, 0.09351])
    work = {
        'BREEDDRAGONS': lambda: Breed.breed(work_type='breed', times=10),
        'FEEDYOURDRAGONS': lambda: Breed.breed(work_type='feed', times=10),
    }

    def run():
        if not exists(Position_Map.center_map()):
            return check_if_ok()
        multiple_click(Runner.runner_pos, 10, 0.01)
        delay(1)
        if not Runner._is_runner():
            return check_if_ok()

        if not Runner._is_expanded():
            expand_pos = Screen.get_pos([0.4921875, 0.85648])
            moveAndClick(expand_pos)
            delay(1)
        Runner._claim_nodes()
        delay(1)
        work_to_do = Runner._get_work()

        multiple_click(Runner.close_pos, 2, 0.5)

        for work in work_to_do:
            work()

    @staticmethod
    def _is_runner():
        bbox = [0.3109375, 0.031481, 0.45260416, 0.11]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match(text['runner'], t['text']):
                return True
        return False

    @staticmethod
    def _get_work():
        bboxes = [
            [0.3484375, 0.487, 0.7375, 0.55],
            [0.3484375, 0.6, 0.7375, 0.69],
            [0.3484375, 0.72, 0.7375, 0.799],
        ]

        work_to_do = []
        for bbox in bboxes:
            text_positions = Screen.get_text_pos(bbox, gray_mode=True)
            added_work = False
            for t in text_positions:
                work = Runner.work.get(t['text'])

                if work:
                    work_to_do.append(work)
                    added_work = True
                if Screen.is_match(text['claimed'], t['text']) and added_work:
                    work_to_do.pop()
                    break
        return work_to_do

    @staticmethod
    def _claim_nodes():
        bbox = [0.649479, 0.4768518, 0.7375, 0.81]
        text_positions = Screen.get_text_pos(bbox, gray_mode=True)

        for t in text_positions:
            if Screen.is_match(text['Claim'], t['text']):
                moveAndClick(t['position'])

    @staticmethod
    def _is_expanded():
        bbox = [0.28697916, 0.3935185, 0.37760416, 0.451]

        text_positions = Screen.get_text_pos(bbox)

        for t in text_positions:
            if Screen.is_match(text['Complete'], t['text']):
                return True

        return False
