from move import moveAndClick
from utils import exists, get_monitor_quarters, getImagePositionRegion
import constants as C

def claim_all():
    claim_btn = getImagePositionRegion(C.APP_CLAIM_ALL, *get_monitor_quarters()['full'], .8, 2)
    if exists(claim_btn):
        moveAndClick(claim_btn)
 