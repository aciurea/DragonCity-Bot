import time
from utils import ThreadWithValue, closePopup, exists, getImagePositionRegion, moveAndClick, delay, scroll
import constants as C

RARITY_PATHS = [
    # C.TREE_RARITY_COMMON,
    C.TREE_RARITY_RARE,
    C.TREE_RARITY_VERY_RARE,
    C.TREE_RARITY_EPIC,
    C.TREE_RARITY_LEGENDARY,
]

def _change_rarity(path):
    print('changing the rarity')
    rarirty =  getImagePositionRegion(C.TREE_RARITY, 0, 500, 300, 650, .8, 3)

    if not exists(rarirty):
        return print('Cannot continue since there is no rarity button')
    moveAndClick(rarirty)
  
    rarity = getImagePositionRegion(path, 100, 200, 800, 700)
    if exists(rarity):
        moveAndClick(rarity)
        delay(.5)
        moveAndClick([rarity[0] + 500, rarity[1]])
    return rarity

def _summon():
    print('TODO inside summon ')

def _recall():
    finish = getImagePositionRegion(C.TREE_FINISH_RECALL, 1000, 700, 1400, 850, .8, 3)

    if exists(finish):
        moveAndClick(finish)
    select_dragon = getImagePositionRegion(C.TREE_NEW_DRAGON, 900, 200, 1400, 600, .8, 20) 
   
    if not exists(select_dragon): return print('Recall not ready yet')

    for rarity_path in RARITY_PATHS:
        rarity = _change_rarity(rarity_path)
        if exists(rarity):
            dragon = getImagePositionRegion(C.TREE_40, 100, 200, 1000, 800)
            if exists(dragon):
                print('dragon is ', dragon)
                moveAndClick(dragon)
                delay(10)
                recall_btn = getImagePositionRegion(C.TREE_RECALL_BTN, 1000, 700, 1400, 850, .8,3 )
                if not exists(recall_btn): return print('Recall btn not found')
                moveAndClick(recall_btn)
                delay(2)
                yes = getImagePositionRegion(C.TREE_YES, 400, 500, 1100, 800)
                if not exists(yes): return print('Yes btn not exists')
                moveAndClick(yes, 'No yes button')
                return print('Dragon added to recall')
            _change_rarity(rarity_path)

def _empower():
    print('TODO empower ')
    
def _trading_hub():
    refund = ThreadWithValue(target=getImagePositionRegion, args=(C.TREE_REFUND, 1000, 600, 1500, 850, .8, 3)).start()
    claim = ThreadWithValue(target=getImagePositionRegion, args=(C.TREE_TRADING_CLAIM, 1000, 700, 1400, 850, .8, 3)).start()
    claim = claim.join()
    refund = refund.join()

    print('claim :', claim, ' refund: ', refund)
    btn = claim if exists(claim) else refund
    if exists(btn) or exists:
        moveAndClick(btn) 
        delay(2)

    unavailable_btn = getImagePositionRegion(C.TREE_UNAVAILABLE, 600, 600, 1400, 900, .8, 3)

    if not exists(unavailable_btn):
        return print('Cannot continue since there is no unavailable btn')
    delay(1)
    st = time.time()
    while(time.time() - st < 120):
        new = getImagePositionRegion(C.TREE_TRADING_NEW, 300, 200, 800, 600, .8, 3)
        if exists(new):
            moveAndClick(new)
            delay(1)
            moveAndClick([310, 350]) # first dragon always
            delay(10)
            moveAndClick([1260, 780]) # hard to identify the essence, hardcoded the position
            delay(1)
            return print('Trading placed')
        scroll([410, 795], [410, 700])

def _inside_devine_tree():
    _trading_hub()
    right = getImagePositionRegion(C.TREE_NEXT, 1000, 0, 1300, 200)

    if not exists(right):
        return print('No right arrow to click')
    list = [_summon, _recall, _empower]

    for action in list:
        moveAndClick(right)
        action()
        delay(2)
  
def _get_tree():
    trees = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.TREE_OF_LIFE,300, 100, 800, 400,.8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.WINTER_TREE_OF_LIFE ,300, 100, 800, 400,.8, 3)).start(),
    ]

    for tree in trees:
        tree = tree.join()
        if exists(tree):
            return tree
    return [-1]

def tree_of_life():
    print('start looking for divine tree')
    tree = _get_tree()

    if not exists(tree):
        return print('Devine Tree not found')
    moveAndClick(tree)

    delay(.5)
    trade_btn = getImagePositionRegion(C.TREE_TRADE, 1200, 700, 1600, 900)

    if not exists(trade_btn):
        return print('Trade btn not found, cannot continue')
    moveAndClick(trade_btn)
    _inside_devine_tree()
    closePopup()
        


def start():
    delay(2)
    tree_of_life()

# start()