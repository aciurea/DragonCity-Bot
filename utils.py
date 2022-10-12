from python_imagesearch.imagesearch import imagesearch, imagesearcharea
import time
import mouse


def getImagePosition(path, tries=10, precision=0.85):
    image = imagesearch(path, precision)
    if(image[0] != -1): return image

    time.sleep(0.2)
    if(tries > 0): return getImagePosition(path, tries - 1)
      
    return [-1, -1]

def moveAndClick(pos):
    mouse.move(pos[0], pos[1])
    
    while(mouse.get_position()[0] != pos[0]):
        time.sleep(0.5)

    time.sleep(0.5)
    mouse.click()

def closePopup(): 
    closeBtn = getImagePosition('./img/utils/close.png')
   
    if(closeBtn[0] == -1):
        return print('no close button')

    moveAndClick(closeBtn)

def closeVideo():
    closeBtn = getImagePosition('./img/utils/close_video.png')
    if(closeBtn[0] == -1): 
        return print('Close video button not found')
        
    moveAndClick(closeBtn)