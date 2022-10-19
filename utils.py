from threading import Thread
import time
import mouse
from python_imagesearch.imagesearch import (imagesearch_loop, imagesearch,
                                            imagesearcharea, imagesearch_region_loop)

# It retries 10 times which means 5 seconds for the image to appear
def getImagePositionRegion(path, x1, y1, x2=1600, y2=900, precision=0.8, retries=10):
    image = imagesearcharea(path, x1, y1, x2, y2, precision)
    while not exists(image):
        image = imagesearcharea(path, x1, y1, x2, y2, precision)
        if retries == 0: return [image[0] + x1, image[1] + y1] if exists(image) else [-1]
        retries -=1
        delay(0.5)
    return [image[0] + x1, image[1] + y1]


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


def getImagePosition(path, tries=20, precision=0.8, seconds=0.5):
    image = imagesearch(path, precision)

    while (not exists(image)):
        tries -= 1
        image = imagesearch(path, precision)
        if (tries == 0):
            return image
        delay(seconds)

    return image

def retry(fn, tries = 3):
    if tries == 0: return [-1]

    if(tries > 0):
        img = fn()
        if not exists(img):
            return retry(fn, tries -1)
        return img

def backFn(): return imagesearcharea('./img/fails/back.png', 0, 0, 500, 150)
def closeFn(): return imagesearcharea('./img/utils/close.png', 300, 0, 1600, 450)

def moveAndClickOnIslandWrapper(lastCall='none'):
    times = {'gold': 0, 'food': 0, 'breed': 0,
             'hatch': 0, 'none': 0, 'farm': 0, 'regrow': 0}
    lastCall = ['none']
    # TODO try to use the function that is called as the key. 
    # Clear the object after is success
    def inner(pos, msg='Nothing to click', type='none'):
        if (times[type] >= 4):
            # TODO try to move the map
            return print(type + ' to many calls')

        moveAndClick(pos, msg)
        delay(.5)
        # start at 0, 0, and end at 1600, 450. (most right horizonatlly, half the screen vertically)

        backBtn = retry(backFn, 3)  # start at 0, 0, and end at 500, 200
        closeBtn = retry(closeFn, 3)

        if exists(backBtn) or exists(closeBtn):
            times[type] += 1
        if (lastCall[0] != type):  # reset when it fails for other reason
            times[type] = 0
            lastCall[0] = type

        if exists(backBtn):
            moveAndClick(backBtn, 'Back button')
        if exists(closeBtn):
          moveAndClick([closeBtn[0] + 300, closeBtn[1]], 'Close button')

    return inner


moveAndClickOnIsland = moveAndClickOnIslandWrapper()

def moveAndClick(pos, msg = 'Nothing to click'):
    if not exists(pos):
        return print(msg)
        
    moveTo(pos)
    
    while(mouse.get_position()[0] != pos[0]):
       delay(0.2)

    time.sleep(0.2)
    mouse.click()

def closePopup(): 
    closeBtn = getImagePositionRegion('./img/utils/close.png', 900, 0, 1600, 450) # close is on the top right corner. I can also be in the middle of the screen
    moveAndClick(closeBtn, 'no close button')

def closeVideo():
    closeBtn = getImagePositionRegion('./img/utils/close_video.png', 900, 0, 1600, 350) # close is on the top right corner. I can also be in the middle of the screen

    moveAndClick(closeBtn, 'Close video button not found')

def moveTo(position):
   mouse.move(position[0], position[1])


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return
