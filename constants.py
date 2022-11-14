from utils import get_path

_BASE_BATTLE = './img/battle/'
_BASE_ARENA = _BASE_BATTLE + 'arenas/'
_BASE_GOLD = './img/gold/'
_BASE_FOOD = './img/food/'
_BASE_ORBS = './img/orbs/'
_BASE_APP_START= './img/app_start/'
_BASE_BREED = './img/breed'
_BASE_TV = './img/tv/'

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

APP_START_CLAIM_BTN = get_path(_BASE_APP_START + 'claim_yellow')
APP_START_DIVINE_CLOSE = get_path(_BASE_APP_START + 'close_divine')

BREED_FEED_BTN = get_path(_BASE_BREED + 'feed') 
BREED_SELL_BTN = get_path(_BASE_BREED + 'sell') 
BREED_CONFIRM_SELL_BTN = get_path(_BASE_BREED + 'sell_confirmation') 
BREED_PLACE_BTN = get_path(_BASE_BREED + 'place') 
BREED_DRAGON_PLACE_POINT = get_path(_BASE_BREED + 'dragon_place_point') 
BREED_DRAGON = get_path(_BASE_BREED + 'dragon') 
BREED_TERRA_EGG = get_path(_BASE_BREED + 'terra_egg') 
BREED_TREE = get_path(_BASE_BREED + 'tree') 
BREED_RE_BREED_BTN = get_path(_BASE_BREED + 're-breed') 
BREED_BREED_BTN = get_path(_BASE_BREED + 'breed_btn') 
BREED_ROCK = get_path(_BASE_BREED + 'rock') 
BREED_FINISH_BREED = get_path(_BASE_BREED + 'finish_breed') 

TV_DAILY_CHEST = get_path(_BASE_TV + 'daily_chest')
TV_COLLECT = get_path(_BASE_TV + 'collect')
TV_CLAIM = get_path(_BASE_TV + 'claim')
TV_PRIZES = get_path(_BASE_TV + 'prizes')
TV_TV = get_path(_BASE_TV + 'tv')
TV_GET_REWARDS_BTN = get_path(_BASE_TV + 'get_rewards_btn')