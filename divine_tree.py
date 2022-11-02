from utils import closePopup, exists, getImagePositionRegion, moveAndClick, delay, scroll

RARITY_PATHS = [
    './img/tree/common.png',
    './img/tree/rare.png',
    './img/tree/very_rare.png',
    './img/tree/epic.png',
    './img/tree/legendary.png',
]

def change_rarity(path):
    print('changing the rarity')
    rarirty =  getImagePositionRegion('./img/tree/rarity.png', 0, 500, 300, 650, .8, 3)

    if not exists(rarirty):
        return print('Cannot continue since there is no rarity button')
    moveAndClick(rarirty)
  
    rarity = getImagePositionRegion(path, 100, 200, 800, 700)
    if exists(rarity):
        moveAndClick(rarity)
        delay(.5)
        moveAndClick([rarity[0] + 500, rarity[1]])
    return rarity

def summon():
    print('TODO inside summon ')

def recall():
    finish = getImagePositionRegion('./img/tree/finish_recall.png', 1000, 700, 1400, 850, .8, 3)

    if exists(finish):
        moveAndClick(finish)
    select_dragon = getImagePositionRegion('./img/tree/select_new_dragon.png', 900, 200, 1400, 600, .8, 20) 
   
    if not exists(select_dragon): return print('Recall not ready yet')

    for rarity_path in RARITY_PATHS:
        rarity = change_rarity(rarity_path)
        if exists(rarity):
            dragon = getImagePositionRegion('./img/tree/40.png', 100, 200, 1000, 800)
            if exists(dragon):
                moveAndClick(dragon)
                recall_btn = getImagePositionRegion('./img/tree/recall_btn.png', 1000, 700, 1400, 850, .8,3 )
                if not exists(recall_btn): return print('Recall btn not found')
                moveAndClick(recall_btn)
                delay(2)
                yes = getImagePositionRegion('./img/tree/yes.png', 400, 500, 1100, 800)
                if not exists(yes): return print('Yes btn not exists')
                moveAndClick(yes, 'No yes button')
                return print('Dragon added to recall')
            change_rarity(rarity_path)

def empower():
    print('TODO empower ')
    
def trading_hub():
    claim = getImagePositionRegion('./img/tree/trading_claim.png', 1000, 700, 1400, 850, .8, 3)
    print('loogin for claim', claim)
    if exists(claim):
        moveAndClick(claim) 
        delay(2)

    unavailable_btn = getImagePositionRegion('./img/tree/unavailable.png', 600, 600, 1400, 900, .8, 3)

    if not exists(unavailable_btn):
        return print('Cannot continue since there is no unavailable btn')
    delay(1)

    while(True):
        new = getImagePositionRegion('./img/tree/trading_new.png', 300, 200, 800, 600, .8, 3)
        if not exists(new):
            scroll([410, 795], [410, 700])
            continue
        moveAndClick(new)
        delay(1)
        moveAndClick([310, 350]) # first dragon always
        delay(1)
        moveAndClick([1260, 780]) # hard to identify the essence, hardcoded the position
        delay(1)
        return print('Trading placed')

def inside_divine_tree():
    trading_hub()
    right = getImagePositionRegion('./img/tree/next.png', 1000, 0, 1300, 200)

    if not exists(right):
        return print('No right arrow to click')
    list = [summon, recall, empower]

    for action in list:
        moveAndClick(right)
        action()
        delay(1)
  

def devine_tree():
    print('start looking for divine tree')
    tree = getImagePositionRegion('./img/tree/devine_tree.png', 300, 100, 800, 400,.8, 20)

    if not exists(tree):
        return print('Devine Tree not found')
    moveAndClick(tree)

    delay(.5)
    trade_btn = getImagePositionRegion('./img/tree/trade.png', 1200, 700, 1600, 900)

    if not exists(trade_btn):
        return print('Trade btn not found, cannot continue')
    moveAndClick(trade_btn)
    inside_divine_tree()
    closePopup()
        


def start():
    delay(2)
    devine_tree()

# start()