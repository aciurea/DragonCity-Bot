from threading import Thread
import pyautogui
import time
import mouse
from python_imagesearch.imagesearch import (imagesearch, imagesearcharea)
from pynput.keyboard import Controller

def type_on_keyboard(key, times = 1):
    while(times > 0):
        times -= 1
        pyautogui.press(key)

def type_combination(key1, key2):
    print('Try to press ', key1, '+ ', key2)
    keyboard = Controller()
    keyboard.press(key1)
    keyboard.press(key2)
    keyboard.release(key2)
    keyboard.release(key1)

def get_path(path):
    return path+'.png'

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def start(self) -> None:
        super().start()
        return self

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def video_error():
    error = getImagePosition('./img/tv/video_error.png')

    if not exists(error): return [-1]
    close = getImagePositionRegion('./img/utils/close.png', error[0], error[1], 1600, 600)

    if not exists(close):
        print('Error exists but couldnt find the close button')
        return [-1]
    moveAndClick(close)
    return [1]
    
def go_back():
    back_btn = getImagePositionRegion('./img/fails/back.png', 0, 0, 150, 150, .8, 2)
    moveAndClick(back_btn)

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
    ## stop after 90s, try 30 times * 3 = 90 seconds
    times = 30
    while(times > 0):
        image = getImagePosition('./img/utils/ready_to_claim.png', 5)
        if exists(image):
            return image
        delay(3)
   
    return [-1]


def getImagePosition(path, tries=20, precision=0.8, seconds=0.5):
    image = imagesearcharea(path, 0, 0, 1600, 900, precision)

    while (not exists(image)):
        tries -= 1
        image = imagesearch(path, precision)
        if (tries == 0):
            return image
        delay(seconds)

    return image



def check_if_not_ok(msg = 'None'):
    list= [
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/fails/back.png', 0, 0, 150, 150, .8, 2)),
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/utils/close.png', 800, 0, 1600, 500, .8, 2)),
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/fails/red_close.png', 800, 0, 1600, 500, .8, 2)),
        ThreadWithReturnValue(target=getImagePositionRegion, args=('./img/fails/claim_yellow.png', 700, 600, 1200, 850, .8, 2))
    ]
    
    for thread in list:
        thread.start()
    
    index = -1
    for thread in list:
        index += 1
        item = thread.join()
        if exists(item):
            moveAndClick(item)
            print('Clicked outside:: ', msg)
            if index == len(list):
                delay(2)
                openChest()
                closePopup()
                print(msg, '::: when closePopup')
            dragMapToCenter()
    
def openChest():
    tap = getImagePositionRegion('./img/tv/tap.png', 300, 300, 1600, 800)
    moveAndClick(tap, 'No tap button found')
    delay(3)
    claim = getImagePositionRegion(
        './img/tv/yellow_claim.png', 200, 300, 1600, 800)
    moveAndClick(claim, 'No claim button after opening chest found')
    delay(.5)
    if not exists(claim):
        closePopup()


def backFn(): return imagesearcharea('./img/fails/back.png', 0, 0, 500, 150)
def closeFn(): return imagesearcharea('./img/utils/close.png', 800, 0, 1600, 450)
def claim(): return imagesearcharea('./img/utils/close.png', 400, 200, 1200, 800)

def moveAndClick(pos, msg = 'Nothing to click'):
    if not exists(pos):
        return print(msg)
        
    moveTo(pos)
    
    while(mouse.get_position()[0] != pos[0]):
       delay(0.2)

    delay(0.1)
    mouse.click()

def get_close_btn(x1 = 1400, y1= 0, x2 = 1600, y2 = 150):
    return getImagePositionRegion('./img/utils/close.png', x1, y1, x2, y2)

def closePopup(btn = [-1]):
    if exists(btn): 
        delay(1)
        moveAndClick(btn) 
    else: moveAndClick(get_close_btn(), 'no close button')

def closeVideo():
    closeBtn = getImagePositionRegion('./img/utils/close_video.png', 900, 0, 1600, 350) # close is on the top right corner. I can also be in the middle of the screen

    moveAndClick(closeBtn, 'Close video button not found')

def moveTo(position):
   mouse.move(position[0], position[1], True, .05)


def dragMap(artifact, next=[800, 450]):
    x, y = next
    moveTo(artifact)
    delay(.2)
    pyautogui.mouseDown()
    pyautogui.moveTo(x, y)
    delay(1)
    pyautogui.mouseUp()


def dragMapToCenter():
    print('Drag map to center')
    artifact = getImagePosition('./img/utils/artifact.png', 5, .8, .5)
    if(artifact[0] == 800 and artifact[1] == 450):
        moveAndClick(artifact)
        return artifact

    if not exists(artifact):
        print('Cannot move the map since there is no point of reference')
        return [-1]
    print('artifact is ', artifact)
    dragMap(artifact)
    return artifact
    
def move_to_top():
    artifact = dragMapToCenter()
    if not exists(artifact): return
    print('move to top')
    dragMap(artifact, [800, 600])

def move_to_bottom():
    artifact = dragMapToCenter()
    if not exists(artifact): return
    print('move to top')
    dragMap(artifact, [800, 300])

def getMovePositions():
    return [
        'down',
        'up',
    ]


def scroll(pos1, pos2):
    moveTo(pos1)
    delay(.5)
    mouse.hold()
    delay(.1)
    moveTo(pos2)
    delay(.5)
    mouse.release()
   
