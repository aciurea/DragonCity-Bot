import cv2
from pytesseract import pytesseract
from PIL import ImageGrab, Image


def get_text(oponent = False):
    path ='./temp/img.png'
    bbox = [1563, 221, 1727, 281] if oponent else [651, 221, 798, 285] 
    cap_length_6 = ImageGrab.grab(bbox)
    cap_length_6.save(path)
    print(1)
    ref = cv2.imread(path)

    return int(_get_text_chat(ref))
    
def _get_text_chat(ref):
    gray = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        roi = thresh[y:y + h, x:x + w]
        digit = pytesseract.image_to_string(Image.fromarray(roi), config="--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789")
        digit = digit.replace(" ", "")
        if(len(digit) > 0 and len(digit) > 6):
            return digit[:-1]

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"