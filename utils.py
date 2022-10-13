from python_imagesearch.imagesearch import imagesearch, imagesearcharea
import time
import mouse


def checkIfCanClaim():
    image = getImagePosition('./img/utils/ready_to_claim.png', 20, 0.9)
    if (image[0]):
        return image
    time.sleep(3)
    return checkIfCanClaim()


def getImagePosition(path, tries=20, precision=0.8):
    image = imagesearch(path, precision)
    if(image[0] != -1): return image

    time.sleep(0.5)
    if (tries > 0):
        return getImagePosition(path, tries - 1, precision)
      
    return [-1, -1]

def moveAndClick(pos):
    mouse.move(pos[0], pos[1])
    
    while(mouse.get_position()[0] != pos[0]):
        time.sleep(0.5)

    time.sleep(1)
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