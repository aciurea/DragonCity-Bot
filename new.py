from python_imagesearch.imagesearch import imagesearch
import time
import mouse

def close():   
    pos = imagesearch('./img/close.png')
 
    if(pos[0] != -1):
        mouse.move(pos[0], pos[1])
        mouse.click()

def triggerRegrow():
    pos = imagesearch('./img/farm.png')

    if(pos[0] != -1):
        print('farm position: ', pos[0], pos[1], pos)
        mouse.move(pos[0] +15, pos[1] + 15)
        mouse.click()
        close()
    else:
        print('farm image not found')

def regrow():
    pos = imagesearch('./img/regrow.png')

    if pos[0] != -1:
        print('regrow position: ', pos[0], pos[1])
        mouse.move(pos[0], pos[1], absolute=True)
        mouse.click()
    else:
        print('regrow image not found')
       

def collectFood():
    pos = imagesearch('./img/food.png')

    if pos[0] != -1:
        print('position: ', pos[0], pos[1])
        mouse.move(pos[0], pos[1], absolute=True)
        mouse.click()
        time.sleep(1)
        collectFood()
    else:
        print('food not found')
        triggerRegrow()
        time.sleep(1)
        regrow()
        time.sleep(31)
        collectFood()
       
collectFood()

