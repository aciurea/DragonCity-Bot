import time

import mouse
from python_imagesearch import (imagesearch, imagesearch_loop,
                                imagesearch_numLoop, imagesearcharea)


def commonClaim():
    greenClaim = getImagePosition('./img/tv/green_claim.png', 3)
    moveAndClick(greenClaim)
    delay(1)
    tap = getImagePosition('./img/tv/tap.png', 3)
    moveAndClick(tap)
    delay(1)
    claim = getImagePosition('./img/fails/claim_yellow.png', 3)
    moveAndClick(claim)
    closePopup()
    print('Claimed rewards')

def delay(seconds):
    time.sleep(seconds)

def exists(value):
    return value[0] != -1;

def checkIfCanClaim():
    image = imagesearch_loop('./img/utils/ready_to_claim.png', 3)

    return image if exists(image) else [-1]


def getImagePosition(path, tries=20, precision=0.8, delay=0.5):
    image = imagesearch_numLoop(path, delay, tries, precision)

    return image if exists(image) else [-1]

def retry(fn, tries = 3):
    if tries == 0: return [-1]

    if(tries > 0):
        img = fn()
        if not exists(img):
            return retry(fn, tries -1)
        return img

def moveAndClickOnIsland(pos, msg = 'Nothing to click'):
    # TODO resolution is: 1600x900
    moveAndClick(pos, msg)
    delay(.5)
    backBtn = retry(imagesearcharea('./img/fails/back.png', 0, 0, 500, 200), 2) # start at 0, 0, and end at 500, 200
    moveAndClick(backBtn)
    closeBtn = retry(imagesearch( './img/utils/close.png', 500, 0, 1600, 450), 2) # start at 0, 0, and end at 1600, 450. (most right horizonatlly, half the screen vertically)
    moveAndClick(closeBtn)
    

def moveAndClick(pos, msg = 'Nothing to click'):
    if not exists(pos):
        return print(msg)
        
    moveTo(pos)
    
    while(mouse.get_position()[0] != pos[0]):
       delay(0.2)

    time.sleep(0.2)
    mouse.click()

def closePopup(): 
    closeBtn = getImagePosition('./img/utils/close.png')
    moveAndClick(closeBtn, 'no close button')

def closeVideo():
    closeBtn = getImagePosition('./img/utils/close_video.png')

    moveAndClick(closeBtn, 'Close video button not found')


def moveTo(position):
   mouse.move(position[0], position[1])
