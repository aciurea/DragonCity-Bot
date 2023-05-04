from utils import delay, exists, getImagePositionRegion, moveAndClick
import constants as C
import time

from utilss.drag_map import drag_to, dragMapToCenter

def _wait_for_artifact_to_be_visible():
    st = time.time()

    while(time.time() - st < 10 or not exists(dragMapToCenter())):
        delay(.5)

def collect_resources():
    _wait_for_artifact_to_be_visible()
    artifact = dragMapToCenter()
    if exists(artifact):
        drag_to(artifact, [artifact[0], artifact[1]-150])
    resources_tower = getImagePositionRegion(C.TOWERS_RESOURCESS_TOWER, 950, 500, 1250, 800, 0.8, 5)

    if not exists(resources_tower): return [-1]
    moveAndClick(resources_tower)

    resources_btn = getImagePositionRegion(C.TOWERS_COLLECT_RESOURCES_BTN, 1100, 700, 1350, 850, 0.8, 3)
    if not exists(resources_btn): return [-1]
    moveAndClick(resources_btn)
    return resources_btn

def boost_gold(artifact):
    print(artifact)
    boost_gold_tower = getImagePositionRegion(C.TOWERS_BOOST_GOLD_TOWER, 100, 50, 1000, 700, 0.8, 3)
    if not exists(boost_gold_tower): return [-1]
    moveAndClick(boost_gold_tower)
    boost_gold_btn = getImagePositionRegion(C.TOWERS_BOOST_GOLD_BTN, 1160, 700, 1330, 860, 0.8, 3)
    if not exists(boost_gold_btn): return [-1]
    moveAndClick(boost_gold_btn)
    print('Goold boosted')

def collect_gems(artifact):
    print(artifact)
    if exists(artifact):
        drag_to(artifact, [artifact[0], artifact[1]+50])
    gems_tower = getImagePositionRegion(C.TOWERS_GEMS_TOWER, 1120, 10, 1400, 300, 0.8, 3)
    if not exists(gems_tower): return [-1]
    moveAndClick(gems_tower)
    gems_btn = getImagePositionRegion(C.TOWERS_GEMS_BTN, 1160, 700, 1330, 860, 0.8, 3)
    if not exists(gems_btn): return [-1]
    moveAndClick(gems_btn)
    print('Gems collected')