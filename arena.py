import pyautogui
from league import goToFight
from utils import ThreadWithReturnValue, closePopup, delay, exists, get_path, getImagePositionRegion, moveAndClick, openChest, type_combination, type_on_keyboard
from pynput.keyboard import Key
import cv2
from PIL import ImageGrab
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def get_text():
    # x1 = 400, x2 = 600, y1= 120, y2 = 165
    path ='./temp/img.png'
    # cap = ImageGrab.grab(bbox=(511, 127, 589, 159))
    # cap.save(path)
    times = 5

    list = []
    while(times > 0):
        times -= 1
        img = cv2.imread(path)
        words_in_image = pytesseract.image_to_string(img)
        list.append(words_in_image)
        delay(.3)
  
    words_in_image = None
    for item in list:
        try:
            num = int(item)
            words_in_image = num
            break
        except:
            print('error')

    return words_in_image

BASE_ARENA = './img/battle/arenas/' 

def get_arena_path(path):
    return get_path(BASE_ARENA+path)

def cheat_btn():
    list = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('new_scan'), 600, 100, 1400, 600, .8, 5)),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('first'), 600, 100, 1400, 600, .8, 5))
    ]

    for thread in list:
        thread.start()
    for thread in list:
        img = thread.join()
        if exists(img): 
            return img
    return [-1]

def type_inside_cheat_engine():
    print('Started typing....')
    type_on_keyboard('backspace', 20)
    delay(.5)
    # pyteseract to identify the screen
    text_to_write = '182540'  #get_text()
    pyautogui.write(text_to_write)

  
def freeze_dragons():
    cheat_engine_pos = [220, 880]
    moveAndClick(cheat_engine_pos)
    delay(1)

    new_scan = getImagePositionRegion(get_arena_path('new_scan'), 0, 100, 1600, 600, .8, 10) 

    if(exists(new_scan)):
        moveAndClick(new_scan)
    delay(1)
    
    first = getImagePositionRegion(get_arena_path('first'), 0, 100, 1500, 600)
    if not exists(first): 
        print('First btn cannot find')
        return [[-1], [-1]]
    x = first[0] - 115
    y = first[1]- 53
    moveAndClick([x, y])
    delay(.5)
    type_inside_cheat_engine()
    delay(.5)

    moveAndClick(first)
    delay(5)
    all_addresses=[first[0]-163, first[1]+65]
    moveAndClick(all_addresses)
    type_combination(Key.ctrl, 'a')

    delay(1)
    arrow = [first[0]-30, first[1]+322]
    moveAndClick(arrow)
    delay(1)
    addresses = [arrow[0], arrow[1] + 100]
    moveAndClick(addresses)
    type_combination(Key.ctrl, 'a')
    delay(1)
    type_on_keyboard('space', 1)
    return [cheat_engine_pos, arrow]

def unfreeze_dragons(first_btn):
    type_on_keyboard('space', 1)
    moveAndClick([first_btn[0] -20, first_btn[1]+35])
    delay(2)
    type_on_keyboard('enter', 1)

def check_attack_report():
    threads = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('attack_report'), 780, 180, 940, 270, .8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('close_attack_report'), 1190, 180, 1270, 280, .8, 3)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('attack_report_accept'), 550, 550, 670, 670, .8, 3)).start()
    ]
 
    for thread in threads:
        img = thread.join()
        print(img)
        if exists(img):
            moveAndClick(img)

def check_if_can_fight():
    cannot_fight = getImagePositionRegion(get_arena_path('wait_time'),180, 380, 790, 490, .8, 3)

    if not exists(cannot_fight):
        return print('Battle can start')
    delay(.5)
    change = getImagePositionRegion(get_arena_path('change_dragon'), 375, 670, 590 ,760, .8, 3)

    if not exists(change):
        return print('Change button not found.')
    moveAndClick(change)
    delay(1)
    
    # try 3 times for 3 dragons
    list = [
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('speed'), 280, 620, 680, 720, .8, 20)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('speed'), 800, 620, 1020, 720, .8, 20)).start(),
        ThreadWithReturnValue(target=getImagePositionRegion, args=(get_arena_path('speed'), 1300, 620, 1530, 720, .8, 20)).start(),
    ]
    for item in list:
        speed_up_btn = item.join()
        if not exists(speed_up_btn): continue
        moveAndClick([speed_up_btn[0] - 175, speed_up_btn[1]])
        delay(1)
        left_arrow = [1084, 760]
        moveAndClick(left_arrow)
        delay(.5)
        dragon = [660, 330]
        moveAndClick(dragon)
        delay(2)
    closePopup()
           

def check_and_collect():
    collect= getImagePositionRegion(get_arena_path('collect'), 1015, 125, 1200, 200, .8, 3)

    if exists(collect):
        moveAndClick(collect)
        openChest()

def arena():
    delay(1)
    if not exists(getImagePositionRegion(get_arena_path('arenas_quest'), 1000, 120, 1200, 220)): 
        return print('No arena found')
   
    arena_btn = [1100, 400];
    moveAndClick(arena_btn)
    delay(2)
    check_attack_report()
    check_if_can_fight()
    check_and_collect()

    fight = getImagePositionRegion(get_arena_path('fight'), 740, 730, 870, 800)

    if not exists(fight): 
        closePopup()
        return print('No fight button found')
    moveAndClick(fight)
    delay(2)

    swap = getImagePositionRegion(get_arena_path('swap'), 80, 650, 305, 740, .8, 10)

    if exists(swap):
        moveAndClick(swap)

    delay(1)
    select_new_dragon = getImagePositionRegion(get_arena_path('new_dragon'), 600, 730, 1520, 830, .8, 10)
    if not exists(select_new_dragon): return print('Select new Dragon Btn not found')
    moveAndClick(select_new_dragon)
    cheat_engine_pos, arrow = freeze_dragons()
    if not exists(cheat_engine_pos):
        closePopup()
        return print('Cheat engine error, exit the game')

    delay(5)
    goToFight(cheat_engine_pos)
    unfreeze_dragons(arrow)

    claim_btn = getImagePositionRegion(get_arena_path('claim'), 740, 750, 890, 850)
    print(claim_btn)
    if(exists(claim_btn)):
        moveAndClick(claim_btn)
    closePopup()
