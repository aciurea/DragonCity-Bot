def get_path(path):
    return path+'.png'

_BASE_BATTLE = './img/battle/'
_BASE_ARENA = _BASE_BATTLE + 'arenas/'
_BASE_GOLD = './img/gold/'
_BASE_FOOD = './img/food/'
_BASE_ORBS = './img/orbs/'
_BASE_APP_START= './img/app_start/'
_BASE_BREED = './img/breed/'
_BASE_TV = './img/tv/'
_BASE_HEROIC = './img/heroic/'
_BASE_TOWERS = './img/towers/'
_BASE_TREE = './img/tree/'
_BASE_UTILS = './img/utils/'

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

FIGHT_SWAP_DRAGON = get_path(f'{_BASE_BATTLE}swap')
FIGHT_PLAY = get_path(f'{_BASE_BATTLE}play')
FIGHT_IN_PROGRESS = get_path(f'{_BASE_BATTLE}fight_in_progress')

GOLD_1 = get_path(_BASE_GOLD+'gold')
GOLD_2 = get_path(_BASE_GOLD+'gold_2')

FOOD_FARM = get_path(_BASE_FOOD + 'farm')
FOOD_FARM_WINTER = get_path(_BASE_FOOD + 'farm_winter')
FOOD_REGROW_ALL = get_path(_BASE_FOOD + 'regrow')
FOOD_REGROW_SINGLE = get_path(_BASE_FOOD + 'regrow_0')
FOOD_REGROW_SINGLE = get_path(_BASE_FOOD + 'regrow_single')
FOOD_IMG = get_path(_BASE_FOOD + 'food')

ORBS_GOLD = get_path(_BASE_ORBS + 'gold')
ORBS_SHOP = get_path(_BASE_ORBS + 'shop')
ORBS_ORBS = get_path(_BASE_ORBS + 'orbs')

APP_START_CLAIM_BTN = get_path(_BASE_APP_START + 'claim_yellow')
APP_START_DIVINE_CLOSE = get_path(_BASE_APP_START + 'close_divine')
APP_START_RED_CLOSE = get_path(_BASE_APP_START + 'red_close')
APP_START_BIG_CLOSE = get_path(_BASE_APP_START + 'big_close')
APP_START_CLAIM_DAILY = get_path(_BASE_APP_START + 'claim_yellow')
APP_START_NO = get_path(_BASE_APP_START + 'no')
APP_START_STATIC = get_path(_BASE_APP_START + 'static_icon')
APP_START_BUY_NOW = get_path(f'{_BASE_APP_START}buy_now')
APP_START_BUY_NOW_2 = get_path(f'{_BASE_APP_START}buy_now2')

BREED_FEED_BTN = get_path(_BASE_BREED + 'feed') 
BREED_SELL_BTN = get_path(_BASE_BREED + 'sell') 
BREED_CONFIRM_SELL_BTN = get_path(_BASE_BREED + 'sell_confirmation') 
BREED_PLACE_BTN = get_path(_BASE_BREED + 'place') 
BREED_DRAGON_PLACE_POINT = get_path(_BASE_BREED + 'dragon_place_point') 
BREED_DRAGON = get_path(_BASE_BREED + 'dragon') 
BREED_TERRA_EGG = get_path(_BASE_BREED + 'terra_egg') 
BREED_TREE = get_path(_BASE_BREED + 'tree') 
BREED_WINTER_TREE = get_path(_BASE_BREED + 'winter_tree') 
BREED_RE_BREED_BTN = get_path(_BASE_BREED + 're-breed') 
BREED_BREED_BTN = get_path(_BASE_BREED + 'breed_btn') 
BREED_ROCK = get_path(_BASE_BREED + 'rock') 
BREED_WINTER_ROCK = get_path(_BASE_BREED + 'winter_rock')
BREED_HATCHERY_FULL = get_path(_BASE_BREED + 'hatchery_full') 
BREED_HATCHERY = get_path(_BASE_BREED + 'hatchery') 
BREED_EGG = get_path(_BASE_BREED + 'egg') 

TV_DAILY_CHEST = get_path(_BASE_TV + 'daily_chest')
TV_COLLECT = get_path(_BASE_TV + 'collect')
TV_CLAIM = get_path(_BASE_TV + 'claim')
TV_CLAIM_AND_NEXT = get_path(_BASE_TV + 'claim_next')
TV_PRIZES = get_path(_BASE_TV + 'prizes')
TV_TV = get_path(_BASE_TV + 'tv')
TV_GET_REWARDS_BTN = get_path(_BASE_TV + 'get_rewards_btn')
TV_DTV = get_path(_BASE_TV + 'dtv')
TV_VIDEO_ERROR = get_path(_BASE_TV + 'video_error')
TV_TAP = get_path(_BASE_TV + 'tap')
TV_READY_TO_CLAIM = get_path(_BASE_TV + 'ready_to_claim')
TV_OUT_OF_OFFERS = get_path(_BASE_TV + 'out_of_offers')
TV_GREEN_CLAIM = get_path(_BASE_TV + 'green_claim')

BATTLE_QUEST_BTN = get_path(_BASE_BATTLE + 'quest')
BATTLE_GO_TO_BATTLE = get_path(_BASE_BATTLE + 'go_to_battle')
BATTLE_NEXT_QUEST = get_path(_BASE_BATTLE + 'next_quest')
BATTLE_GREEN_CLAIM = get_path(_BASE_BATTLE + 'claim')
BATTLE_ATTACK_IS_AVAILABLE = get_path(_BASE_BATTLE + 'attacks_available')

HEROIC_SELECT_BTN = get_path(_BASE_HEROIC + 'select')
HEROIC_DRAGON = get_path(_BASE_HEROIC + 'dragon')
HEROIC_OK = get_path(_BASE_HEROIC + 'ok')
HEROIC_FOOD = get_path(_BASE_HEROIC + 'food')
HEROIC_BREED = get_path(_BASE_HEROIC + 'breed')
HEROIC_HATCH = get_path(_BASE_HEROIC + 'hatch')
HEROIC_FEED = get_path(_BASE_HEROIC + 'feed')
HEROIC_GREEN_CLAIM_BTN = get_path(_BASE_HEROIC + 'claim')
HEROIC_NO_CLAIM_BTN_2 = get_path(_BASE_HEROIC + 'no_claim2')
HEROIC_NO_CLAIM_BTN_1 = get_path(_BASE_HEROIC + 'no_claim')
HEROIC_ARENA = get_path(_BASE_HEROIC + 'heroic_arena')
HEROIC_FIGHT = get_path(_BASE_HEROIC + 'fight')
HEROIC_NOT_READY = get_path(_BASE_HEROIC + 'not_ready_yet')
HEROIC_START_FIGHT_BTN = get_path(_BASE_HEROIC + 'start_fight')

TOWERS_RESOURCESS_TOWER = get_path(_BASE_TOWERS + 'resources_tower')
TOWERS_BOOST_GOLD_TOWER = get_path(_BASE_TOWERS + 'gold_tower')
TOWERS_GEMS_TOWER = get_path(_BASE_TOWERS + 'gems_tower')
TOWERS_COLLECT_RESOURCES_BTN = get_path(_BASE_TOWERS + 'collect_resource_btn')
TOWERS_BOOST_GOLD_BTN = get_path(_BASE_TOWERS + 'boost_gold')
TOWERS_GEMS_BTN = get_path(_BASE_TOWERS + 'gems')


TREE_OF_LIFE = get_path(_BASE_TREE + 'devine_tree')
WINTER_TREE_OF_LIFE = get_path(_BASE_TREE + 'winter_devine_tree')
TREE_TRADE = get_path(_BASE_TREE + 'trade')
TREE_NEXT = get_path(_BASE_TREE + 'next')
TREE_REFUND = get_path(_BASE_TREE + 'refund')
TREE_TRADING_CLAIM = get_path(_BASE_TREE + 'trading_claim')
TREE_UNAVAILABLE = get_path(_BASE_TREE + 'unavailable')
TREE_TRADING_NEW = get_path(_BASE_TREE + 'trading_new')
TREE_RARITY = get_path(_BASE_TREE + 'rarity')
TREE_FINISH_RECALL = get_path(_BASE_TREE + 'finish_recall')
TREE_NEW_DRAGON = get_path(_BASE_TREE + 'select_new_dragon')
TREE_40 = get_path(_BASE_TREE + '40')
TREE_RECALL_BTN = get_path(_BASE_TREE + 'recall_btn')
TREE_YES = get_path(_BASE_TREE + 'yes')
TREE_RARITY_COMMON = get_path(_BASE_TREE + 'common')
TREE_RARITY_RARE = get_path(_BASE_TREE + 'rare')
TREE_RARITY_VERY_RARE = get_path(_BASE_TREE + 'very_rare')
TREE_RARITY_EPIC = get_path(_BASE_TREE + 'epic')
TREE_RARITY_LEGENDARY = get_path(_BASE_TREE + 'legendary')


UTILS_CLOSE_BTN = get_path(f'{_BASE_UTILS}close')