import subprocess
from AppOpener import run
import pyautogui
import constants as C
from utils import ThreadWithReturnValue, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick
import time

def close_app():
    subprocess.call("TASKKILL /F /IM DragonCity.exe", shell=True)

def zoom_out():
    pyautogui.scroll(-5000)

def open_app():
    run("Dragon City")
    delay(1)
    moveAndClick([50, 300])
    delay(20)
    _close_all_the_windows()

def _close():
    closes = [
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_GEMS_CLOSE, 1000, 0, 1400, 200, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_RED_CLOSE,  1000, 0, 1400, 200, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_DIVINE_CLOSE,  1000, 0, 1400, 200, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_LEGENDARY_CLOSE,  1000, 0, 1400, 200, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_MEGA_PACK_CLOSE,  1000, 0, 1400, 200, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_PIGGY_CLOSE,  1000, 0, 1400, 200, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_TWD_CLOSE,  1000, 0, 1400, 200, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_CLAIM_DAILY,  800, 0, 1400, 500, 0.8, 5)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_NO,  600, 0, 1400, 600, 0.8, 5)).start(),
    ]

    print('started to look for close buttons')
    
    for close in closes:
        c = close.join()
        if exists(c):
            print('found a close button')
            return moveAndClick(c)

def get_artifact():
    artifacts = [
         ThreadWithReturnValue(target=getImagePosition, args=('./img/utils/artifact.png', 5)).start(),
       ThreadWithReturnValue(target=getImagePosition, args=('./img/utils/artifact.png', 5)).start(),
    ]

    for artifact in artifacts:
        artifact = artifact.join()
        if exists(artifact):
            return artifact
    return [-1]


def _close_all_the_windows():
    start = time.time()
    while(not exists(get_artifact())):
        if time.time() - start > 60: close_app()
        zoom_out()
        _close()
        delay(1)