from move import moveAndClick
from screen import Screen


def claim_all():
    bbox = [0.4416, 0.7638, 0.55416, 0.8342592]
    text_positions = Screen.get_text_pos(bbox)

    for t in text_positions:
        if Screen.is_match('CLAIMALL', t['text']):
            moveAndClick(t['position'])
