from threading import Thread, Event
from win32gui import FindWindow, GetWindowRect
import pyautogui
import time
import mouse
from python_imagesearch.imagesearch import (imagesearch, imagesearcharea)
import cv2
from pytesseract import pytesseract
from PIL import ImageGrab
import constants as C
import random
import time

def get_path(path):
    return path+'.png'

class ThreadWithValue(Thread):
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
    video_error, close_btn = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.TV_VIDEO_ERROR, 200, 50, 1600, 800, 0.8, 12)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=('./img/utils/close_video_no_claim.png', 900, 100, 1500, 300, 0.8, 5)).start()
    ]
    close_btn = close_btn.join()
    if exists(close_btn):
        moveAndClick(close_btn)
        return close_btn
    
    video_error = video_error.join()
    if not exists(video_error): return video_error

    close = getImagePositionRegion('./img/utils/close.png', video_error[0], video_error[1], 1600, 600)

    if exists(close):
        moveAndClick(close)
        print('Error exists but couldnt find the close button')
        return close
   
    return [-1]
    
def go_back():
    back_btn = getImagePositionRegion('./img/app_start/back.png', 0, 0, 150, 150, .8, 2)
    moveAndClick(back_btn)

# It retries 10 times which means 5 seconds for the image to appear
def getImagePositionRegion(path, x1, y1, x2=1600, y2=900, precision=0.8, retries=10, speed=0.5):
    image = imagesearcharea(path, x1, y1, x2, y2, precision)
    while not exists(image):
        image = imagesearcharea(path, x1, y1, x2, y2, precision)
        if retries == 0: return [image[0] + x1, image[1] + y1] if exists(image) else [-1]
        retries -=1
        delay(speed)
    return [image[0] + x1, image[1] + y1]


def commonClaim():
    greenClaim = getImagePosition(C.HEROIC_GREEN_CLAIM_BTN, 3)
    moveAndClick(greenClaim)
    delay(1)
    tap = getImagePosition(C.TV_TAP, 3)
    moveAndClick(tap)
    delay(1)
    claim = getImagePosition('./img/app_start/claim_yellow.png', 3)
    moveAndClick(claim)
    closePopup()
    print('Claimed rewards')

def delay(seconds):
    if seconds < 0:
        seconds = 0
    time.sleep(seconds)

def exists(value):
    return value[0] != -1;

def checkIfCanClaim():
    st = time.time()
    limit = 60
    while((time.time() - st) < limit):
        lst = [
            ThreadWithValue(target=getImagePositionRegion, args=(C.TV_READY_TO_CLAIM, 570, 120, 1020, 170, .8, 1)).start(),
            ThreadWithValue(target=getImagePositionRegion, args=(C.TV_OUT_OF_OFFERS, 400, 200, 1400, 800, 0.8, 1)).start(),
        ]
        for l in lst:
            l = l.join()
            if exists(l): return l
        moveTo([random.randrange(200, 1400), random.randrange(200, 800)])
        delay(1)
   
    return [-1]


def getImagePosition(path, tries=10, precision=0.8, seconds=0.5):
    image = imagesearcharea(path, 0, 0, 1600, 900, precision)

    while (not exists(image)):
        tries -= 1
        image = imagesearch(path, precision)
        if (tries == 0):
            return image
        delay(seconds)

    return image



def check_if_not_ok():
    btns = [
        ThreadWithValue(target=getImagePositionRegion, args=('./img/app_start/back.png', 0, 0, 150, 150, .8, 2)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=('./img/utils/close.png', 800, 0, 1600, 500, .8, 2)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=('./img/app_start/no.png', 610, 635, 800, 735 , .8, 2)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=(C.APP_START_DIVINE_CLOSE,  1000, 0, 1400, 200, 0.8, 2)).start(),
    ]

    for btn in btns:
        btn = btn.join()
        if exists(btn):
            moveAndClick(btn)
            delay(1)
            return closePopup()

def openChest():
    # TODO fix it according to all the scenarios
    tap, close_btn = [
        ThreadWithValue(target=getImagePositionRegion, args=(C.TV_TAP, 300, 300, 1600, 800, 0.8, 2)).start(),
        ThreadWithValue(target=get_close_btn).start(),
    ]
    tap = tap.join()
    close_btn = close_btn.join()
    if not exists(tap):
        moveAndClick(close_btn, 'Close btn from open chest not found')
        return print('Chest not found in order to be opened')
    moveAndClick(tap)
    delay(3)
    claim = getImagePositionRegion(
        './img/tv/yellow_claim.png', 630, 500, 1200, 800, .8, 3)
    if not exists(claim):
        delay(1)
        closePopup()
 
    moveAndClick(claim)
    delay(1)
  

def backFn(): return imagesearcharea('./img/app_start/back.png', 0, 0, 500, 150)
def closeFn(): return imagesearcharea('./img/utils/close.png', 800, 0, 1600, 450)
def claim(): return imagesearcharea('./img/utils/close.png', 400, 200, 1200, 800)

def moveAndClick(pos, msg = 'Nothing to click'):
    if not exists(pos):
        return print(msg)
    mouse.release() 
    moveTo(pos)
    
    while(mouse.get_position()[0] != pos[0]):
       delay(0.2)
    delay(0.1)
    mouse.click()
    delay(0.1)
    mouse.release()

def get_close_btn(x1 = 1000, y1= 0, x2 = 1600, y2 = 300):
    return getImagePositionRegion('./img/utils/close.png', x1, y1, x2, y2, .8, 3)

def closePopup(btn = [-1]):
    if exists(btn):  
        delay(1)
        moveAndClick(btn) 
    else: moveAndClick(get_close_btn(), 'no close button')

def closeVideo():
    threads = [
        ThreadWithValue(target=getImagePositionRegion, args=('./img/utils/close_video.png', 900, 0, 1600, 350, 0.8, 3)).start(),
        ThreadWithValue(target=getImagePositionRegion, args=('./img/utils/close_video_no_claim.png', 900, 100, 1500, 300, 0.8, 3)).start()
    ]

    for thread in threads:
        moveAndClick(thread.join(), 'Close btn not found')

def moveTo(position):
   mouse.release()
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
    print('artifact is', artifact)
    if not exists(artifact): return [-1]
    print('move to top')
    dragMap(artifact, [800, 700])

def move_to_bottom():
    artifact = dragMapToCenter()
    print('artifact is', artifact)
    if not exists(artifact): return
    print('move to bottom')
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
    mouse.move(pos2[0], pos2[1], True, .05)
    delay(.5)
    mouse.release()
   
def get_text(x = 410):
    pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    path ='./temp/img.png'
    cap_length_6 = ImageGrab.grab(bbox=(x, 127, 491, 161))
    cap_length_6.save(path)
    ref = cv2.imread(path)
    
    lst = [
        _get_text_2(ref).replace(" ", "").replace(".","").rstrip(),
        _get_text_3(ref).replace(" ", "").replace(".","").rstrip(),
        _get_text_4(ref).replace(" ", "").replace(".","").rstrip()
    ]

    i = 0
    while (i < len(lst)):
        if len(lst[i]) > 6:
            lst[i] = lst[i][1:]
        i+=1


    try:
        lst.sort(reverse=True)
        lst = list(filter(lambda item: len(item) > 0, lst))
        return int(lst[0])
    except: return 247336 # value of strongest dragon
    
def _get_text_2(ref):
    gry = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    thr = gry
    bnt = cv2.bitwise_not(thr)

    return pytesseract.image_to_string(bnt, config="--psm 6 digits")

def _get_text_3(ref):
    gry = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w * 2, h * 2))
    erd = cv2.erode(gry, None, iterations=1)
    thr = cv2.threshold(erd, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    bnt = cv2.bitwise_not(thr)

    return pytesseract.image_to_string(bnt, config="--psm 6 digits")

def _get_text_4(ref):
    gry = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w * 2, h * 2))
    erd = cv2.erode(gry, None, iterations=1)
    thr = cv2.threshold(erd, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    bnt = cv2.bitwise_not(thr)

    return pytesseract.image_to_string(bnt, config="--psm 6 digits")



def get_in_progress():
    return getImagePositionRegion('./img/battle/fight_in_progress.png', 0, 100, 190, 300, .8, 2)

def get_window_size():
    window_handle = FindWindow(None, "DragonCity")
    default_size = [1600, 900]
  
    return default_size  if (window_handle != None) else GetWindowRect(window_handle)

def run_for(fnToRun, limit=60):
    e = Event()
    thread = Thread(target=fnToRun)
    thread.start()
    thread.join(timeout=limit)
    if(thread.is_alive()):
        print("Thread is not done, stop it")
        e.set()
    else: print("Thread successfully finished")