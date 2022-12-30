import subprocess
from AppOpener import run
import pyautogui
import constants as C
from utils import ThreadWithReturnValue, delay, exists, getImagePosition, getImagePositionRegion, moveAndClick, openChest
import time

def close_app():
    subprocess.call("TASKKILL /F /IM DragonCity.exe", shell=False)

def zoom_out():
    pyautogui.scroll(-5000)

def open_app():
    run("Dragon City")
    delay(1)
    moveAndClick([50, 300])
    _check_if_app_started()
    _close_all_the_windows()

def _close():
    closes = [
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_GEMS_CLOSE, 1000, 0, 1400, 200, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_RED_CLOSE,  1000, 0, 1400, 200, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_DIVINE_CLOSE,  1000, 0, 1400, 200, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_LEGENDARY_CLOSE,  1000, 0, 1400, 200, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_MEGA_PACK_CLOSE,  1000, 0, 1400, 200, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_PIGGY_CLOSE,  1000, 0, 1400, 200, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_TWD_CLOSE,  1000, 0, 1400, 200, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_CLAIM_DAILY,  500, 650, 1000, 850, 0.8, 3)).start(),
       ThreadWithReturnValue(target=getImagePositionRegion, args=(C.APP_START_NO,  600, 0, 1400, 600, 0.8, 3)).start(),
    ]

    for close in closes:
        c = close.join()
        if exists(c):
            print('found a close button')
            moveAndClick(c)  
            return _close()
    return [-1]

def _get_artifact():
    artifacts = [
         ThreadWithReturnValue(target=getImagePosition, args=('./img/utils/artifact.png', 5)).start(),
       ThreadWithReturnValue(target=getImagePosition, args=('./img/utils/artifact.png', 5)).start(),
    ]

    for artifact in artifacts:
        artifact = artifact.join()
        if exists(artifact):
            return artifact
    return [-1]

def _retry_to_open_app(start, retries):
    if retries > 10: close_app()
    if time.time() - start > 60:
        close_app()
        delay(10)
        open_app()

def _close_all_the_windows():
    start = time.time()
    tries = 0
    while(not exists(_get_artifact())):
        _retry_to_open_app(start, tries)
        zoom_out()
        _close()
        openChest()
        tries += 1

def _check_if_app_started():
    times = 50
    while(times > 0):
        image = getImagePositionRegion(C.APP_START_STATIC, 0, 250, 200, 400, .8, 1)
        if exists(image): return image
        delay(1)
    times -= 1
   
    return [-1]
