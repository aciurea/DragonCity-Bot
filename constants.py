from utils import get_path

_BASE_BATTLE = './img/battle/'
_BASE_ARENA = _BASE_BATTLE + 'arenas/'
_BASE_GOLD = './img/gold/'
_BASE_FOOD = './img/food/'
_BASE_ORBS = './img/orbs/'

ARENA_ATTACK_REPORT = get_path(_BASE_ARENA + 'attack_report')
ARENA_CLOSE_ATTACK_REPORT = get_path(_BASE_ARENA + 'close_attack_report')
ARENA_ATTACK_REPORT_ACCEPT = get_path(_BASE_ARENA + 'attack_report_accept')
ARENA_REPEAL = get_path(_BASE_ARENA + 'repeal')
ARENA_WAIT_TIME = get_path(_BASE_ARENA + 'wait_time')
ARENA_CHANGE_DRAGON= get_path(_BASE_ARENA + 'change_dragon')
ARENA_SPEED_UP = get_path(_BASE_ARENA + 'speed')
ARENA_CHEST_COLLECT = get_path(_BASE_ARENA + 'collect')
ARENA_QUEST = get_path(_BASE_ARENA + 'arenas_quest')
ARENA_FIGHT = get_path(_BASE_ARENA + 'fight')
ARENA_SELECT_NEW_DRAGON_BTN = get_path(_BASE_ARENA + 'new_dragon')
ARENA_CLAIM_BTN = get_path(_BASE_ARENA + 'claim')

FIGHT_SWAP_DRAGON = get_path(_BASE_BATTLE + 'swap')
FIGHT_PLAY = get_path(_BASE_BATTLE+'play')

GOLD_1 = get_path(_BASE_GOLD+'gold')
GOLD_2 = get_path(_BASE_GOLD+'gold_2')

FOOD_FARM = get_path(_BASE_FOOD + 'farm')
FOOD_REGROW_ALL = get_path(_BASE_FOOD + 'regrow')
FOOD_REGROW_SINGLE = get_path(_BASE_FOOD + 'regrow_0')
FOOD_REGROW_SINGLE = get_path(_BASE_FOOD + 'regrow_single')
FOOD_IMG = get_path(_BASE_FOOD + 'food')

ORBS_GOLD = get_path(_BASE_ORBS + 'gold')
ORBS_SHOP = get_path(_BASE_ORBS + 'shop')
ORBS_ORBS = get_path(_BASE_ORBS + 'orbs')