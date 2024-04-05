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
_BASE_WRONG_POPUPS = './img/wrong_popups/'
_BASE_APP_CLOSE = './img/close_buttons/'
_BASE_APP_POPUP = './img/popups/'
_BASE_HABITAT = './img/habitat/'
_BASE_ORBS = './img/orbs/'
_BASE_ALLIANCE = './img/alliance/'

#Alliance
ALLIANCE_CONTINUE = get_path(_BASE_ALLIANCE + 'continue')
ALLIANCE_CLAIM = get_path(_BASE_ALLIANCE + 'claim')
#End Alliance

GOALS_CLOSE_BTN = get_path(_BASE_WRONG_POPUPS + 'goals_close')
ENJOY_POPUP = get_path(_BASE_WRONG_POPUPS + 'enjoy')

LEAGUE_OPONENT = get_path(_BASE_BATTLE + 'league_oponent')
LEAGUE_CLAIM = get_path(_BASE_BATTLE + 'claim')
LEAGUE_NOT_READY = get_path(_BASE_BATTLE + 'no_new_combats')

# ORBS
ORBS_CLAIM = get_path(_BASE_ORBS + 'claim')
#END ORBS

#Habitat
HABITAT_INFO = get_path(_BASE_HABITAT + 'info')
HABITAT_CONTINUE = get_path(_BASE_HABITAT + 'continue')

# End Habitat

# Start Arena
ARENA_ATTACK_REPORT = get_path(_BASE_ARENA + 'attack_report')
ARENA_CLOSE_ATTACK_REPORT = get_path(_BASE_ARENA + 'close_attack_report')

ARENA_REPEAL = get_path(_BASE_ARENA + 'repeal')

ARENA_CHEST_COLLECT = get_path(_BASE_ARENA + 'collect')
ARENA_QUEST = get_path(_BASE_ARENA + 'arenas_quest')
ARENA_CLAIM_BTN = get_path(_BASE_ARENA + 'claim')

ARENA = get_path(_BASE_ARENA + 'arena')
ARENA_FIGHT = get_path(_BASE_ARENA + 'fight')
ARENA_FIGHT_SPIN = get_path(_BASE_ARENA + 'fight_spin')
ARENA_FREE_SPIN = get_path(_BASE_ARENA + 'free_spin')

ARENA_SPEED = get_path(_BASE_ARENA + 'speed')
ARENA_DEFETEAD_DRAGON = get_path(_BASE_ARENA + 'defeated_dragon')
ARENA_DEFETEAD_DRAGON_SELECT_TEAM = get_path(_BASE_ARENA + 'defeated_dragon_select_team')
ARENA_CHANGE = get_path(_BASE_ARENA + 'change_dragon')
ARENA_FILTER_DRAGONS = get_path(_BASE_ARENA + 'filter_dragons')
ARENA_NEW_DRAGON = get_path(_BASE_ARENA + 'new_dragon')
ARENA_ORDER_BY = get_path(_BASE_ARENA + 'order_by')
ARENA_ORDER_BY_POWER = get_path(_BASE_ARENA + 'order_by_power')
ARENA_SKIP = get_path(_BASE_ARENA + 'skip')
ARENA_REPORT_ACCEPT = get_path(_BASE_ARENA + 'report_accept')
ARENA_CLAIM_RUSH = get_path(_BASE_ARENA + 'claim_rush')

ARENA_DURIAN = get_path(_BASE_ARENA + 'durian')
ARENA_SELECT_DRAGON = get_path(_BASE_ARENA + 'select_dragon')


# End Arena


# Start Strong Dragons

ARENA_HIGH_ARCANA = get_path(_BASE_ARENA + 'high_arcana')
ARENA_STRONG_DRAGON = get_path(_BASE_ARENA + 'strong_dragon')
ARENA_HAXED_VAMPIRE = get_path(_BASE_ARENA + 'haxed_vampire')
ARENA_DUAL_PERFECEPTION = get_path(_BASE_ARENA + 'dual_perception')
ARENA_DUAL_PARLIAMENT = get_path(_BASE_ARENA + 'dual_parliament')

# End Strong Dragons

# Start Fight
FIGHT_SWAP = get_path(f'{_BASE_BATTLE}swap')
FIGHT_PLAY = get_path(f'{_BASE_BATTLE}play')
FIGHT_X3 = get_path(f'{_BASE_BATTLE}fight_in_progress')
FIGHT_GOOD_LIFE = get_path(f'{_BASE_BATTLE}low_life')
FIGHT_TAB = get_path(f'{_BASE_BATTLE}fight_tab')
FIGHT_SELECT_DRAGON = get_path(f'{_BASE_BATTLE}select_dragon')
FIGHT_ATTACK_READY = get_path(f'{_BASE_BATTLE}attack_ready')


# End Fight



GOLD_1 = get_path(_BASE_GOLD+'gold')
GOLD_2 = get_path(_BASE_GOLD+'gold_2')

FOOD_FARM = get_path(_BASE_FOOD + 'farm')
FOOD_FARM_WINTER = get_path(_BASE_FOOD + 'farm_winter')
FOOD_REGROW_ALL = get_path(_BASE_FOOD + 'regrow')
FOOD_REGROW_SINGLE = get_path(_BASE_FOOD + 'regrow_single')
FOOD_IMG = get_path(_BASE_FOOD + 'food')

ORBS_GOLD = get_path(_BASE_ORBS + 'gold')
ORBS_SHOP = get_path(_BASE_ORBS + 'shop')
ORBS_ORBS = get_path(_BASE_ORBS + 'orbs')


# Start section popups

POPUP_CLAIM = get_path(f'{_BASE_APP_POPUP}claim')
POPUP_TAP = get_path(f'{_BASE_APP_POPUP}tap')
POPUP_LEFT_CORNER = get_path(f'{_BASE_APP_POPUP}left_corner')
POPUP_HEADER = get_path(f'{_BASE_APP_POPUP}left_header')

# End section popups




## Start section close buttons

APP_CLOSE_DIVINE = get_path(f'{_BASE_APP_CLOSE}divine')
APP_CLOSE_GEMS = get_path(f'{_BASE_APP_CLOSE}gems')
APP_CLOSE_OFFERS = get_path(f'{_BASE_APP_CLOSE}offers')
APP_CLOSE_PIGGY = get_path(f'{_BASE_APP_CLOSE}piggy')
APP_CLOSE_SETTINGS = get_path(f'{_BASE_APP_CLOSE}settings')
APP_CLOSE_TOWER = get_path(f'{_BASE_APP_CLOSE}tower')
APP_LOOSE = get_path(f'{_BASE_APP_CLOSE}loose')
APP_CLOSE_BACK = get_path(f'{_BASE_APP_CLOSE}back')
APP_CLOSE_ANOTHER_RED = get_path(f'{_BASE_APP_CLOSE}another_red')

## End section close buttons



# Start App start
APP_START_CLAIM_BTN = get_path(_BASE_APP_START + 'claim_yellow')
APP_START_DIVINE_CLOSE = get_path(f'{_BASE_APP_START}close_divine')
APP_START_RED_CLOSE = get_path(_BASE_APP_START + 'red_close')
APP_START_BIG_CLOSE = get_path(_BASE_APP_START + 'big_close')
APP_START_NO = get_path(_BASE_APP_START + 'no')
APP_START_BUY_NOW = get_path(f'{_BASE_APP_START}buy_now')
APP_START_BUY_NOW_2 = get_path(f'{_BASE_APP_START}buy_now2')


APP_START_EXTRA_CLAIM = get_path(_BASE_APP_START + 'extra_claim')

# End App start

BREED_FEED_BTN = get_path(_BASE_BREED + 'feed') 
BREED_SELL_BTN = get_path(_BASE_BREED + 'sell') 
BREED_SELL_BTN_CENTER = get_path(_BASE_BREED + 'sell_center') 
BREED_CONFIRM_SELL_BTN = get_path(_BASE_BREED + 'sell_confirmation') 
BREED_PLACE_BTN = get_path(_BASE_BREED + 'place') 
BREED_DRAGON_PLACE_POINT = get_path(_BASE_BREED + 'dragon_place_point') 
BREED_DRAGON = get_path(_BASE_BREED + 'dragon') 
BREED_TERRA_EGG = get_path(_BASE_BREED + 'terra_egg') 
BREED_TREE = get_path(_BASE_BREED + 'tree') 
BREED_WINTER_TREE = get_path(_BASE_BREED + 'winter_tree') 
HATCH_DRAGON = get_path(_BASE_BREED  + 'dragon')

RE_BREED_BTN = get_path(_BASE_BREED + 're-breed') 

BREED_BTN = get_path(_BASE_BREED + 'breed_btn') 
BREED_ROCK = get_path(_BASE_BREED + 'rock') 
BREED_WINTER_ROCK = get_path(_BASE_BREED + 'winter_rock')
HATCHERY_FULL = get_path(_BASE_BREED + 'hatchery_full') 
HATCHERY = get_path(_BASE_BREED + 'hatchery') 
BREED_EGG = get_path(_BASE_BREED + 'egg') 


### Start TV

TV_CLAIM = get_path(_BASE_TV + 'claim')
TV_GET_REWARDS_BTN = get_path(_BASE_TV + 'get_rewards_btn')
TV_CLOSE_WATCHED_VIDEO = get_path(_BASE_TV + 'claim_close')
TV_READY_TO_CLOSE_WATCHED_VIDEO = get_path(_BASE_TV + 'ready_to_claim')
TV_DTV = get_path(_BASE_TV + 'dtv')
TV_LAST_CLAIM = get_path(_BASE_TV + 'last_claim')
TV_FAILED_VIDEO = get_path(_BASE_TV + 'failed_video')
TV_PRAIZES = get_path(_BASE_TV + 'prizes')

## END TV

## Quest
QUEST_GO_TO_BATTLE = get_path(_BASE_BATTLE + 'go_to_battle')

## End Quest

BATTLE_QUEST_BTN = get_path(_BASE_BATTLE + 'quest')
BATTLE_NEXT_QUEST = get_path(_BASE_BATTLE + 'next_quest')
BATTLE_GREEN_CLAIM = get_path(_BASE_BATTLE + 'claim')
BATTLE_ATTACK_IS_AVAILABLE = get_path(_BASE_BATTLE + 'attacks_available')

HEROIC_ARENA = get_path(_BASE_HEROIC + 'heroic')
HEROIC_SELECT_BTN = get_path(_BASE_HEROIC + 'select')
HEROIC_DRAGON = get_path(_BASE_HEROIC + 'dragon')
HEROIC_OK = get_path(_BASE_HEROIC + 'ok')

HEROIC_FOOD = get_path(_BASE_HEROIC + 'food')
HEROIC_BREED = get_path(_BASE_HEROIC + 'breed')
HEROIC_HATCH = get_path(_BASE_HEROIC + 'hatch')
HEROIC_FEED = get_path(_BASE_HEROIC + 'feed')
HEROIC_LEAGUE = get_path(_BASE_HEROIC + 'league')

HEROIC_COMPLETED = get_path(_BASE_HEROIC + 'completed')
HEROIC_GREEN_CLAIM_BTN = get_path(_BASE_HEROIC + 'claim')
HEROIC_NO_CLAIM_BTN_2 = get_path(_BASE_HEROIC + 'no_claim2')
HEROIC_NO_CLAIM_BTN_1 = get_path(_BASE_HEROIC + 'no_claim')
HEROIC_FIGHT = get_path(_BASE_HEROIC + 'fight')
HEROIC_NOT_READY = get_path(_BASE_HEROIC + 'not_ready_yet')
HEROIC_START_FIGHT_BTN = get_path(_BASE_HEROIC + 'start_fight')
HEROIC_IN_PROGRESS = get_path(_BASE_HEROIC + 'in_progress')
HEROIC_CLAIM = get_path(_BASE_HEROIC + 'claim')

# End Heroic


# Start Towers
TOWERS_RESOURCESS_TOWER = get_path(_BASE_TOWERS + 'resources_tower')
TOWERS_GEMS_TOWER = get_path(_BASE_TOWERS + 'gems_tower')
TOWERS_GOLD_TOWER = get_path(_BASE_TOWERS + 'gold_tower')
TOWERS_POWER_TOWER = get_path(_BASE_TOWERS + 'power_tower')
TOWERS_FOOD_TOWER = get_path(_BASE_TOWERS + 'food_tower')

TOWERS_COLLECT_RESOURCES_BTN = get_path(_BASE_TOWERS + 'collect_resources')
TOWERS_GEMS_BTN = get_path(_BASE_TOWERS + 'collect_gems')
TOWERS_BOOST_GOLD_BTN = get_path(_BASE_TOWERS + 'boost_gold')
TOWERS_BOOST_COMBAT_BTN = get_path(_BASE_TOWERS + 'boost_combat')
TOWERS_BOOST_FOOD_BTN = get_path(_BASE_TOWERS + 'boost_food')

# End Towers

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