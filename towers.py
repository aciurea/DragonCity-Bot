from utils import dragMap, exists, getImagePositionRegion, moveAndClick
import constants as C


def collect_resources(artifact):
    print(artifact)
    dragMap(artifact, [artifact[0], artifact[1]-150])
    resources_tower = getImagePositionRegion(C.TOWERS_RESOURCESS_TOWER, 950, 500, 1250, 800, 0.8, 5)

    if not exists(resources_tower): return
    moveAndClick(resources_tower)

    resources_btn = getImagePositionRegion(C.TOWERS_COLLECT_RESOURCES_BTN, 1100, 700, 1350, 850, 0.8, 3)
    if not exists(resources_btn): return
    moveAndClick(resources_btn)
