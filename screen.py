import pytesseract
import os
import time
import easyocr

from PIL import Image, ImageGrab, ImageEnhance, ImageFilter, ImageOps

from screeninfo import get_monitors
from utils import get_int, get_monitor_quarters

reader = easyocr.Reader(['en'], gpu=False)
res = get_monitors()

class Screen:
    width = res[0].width
    height = res[0].height
    
    def get_res():
       res = get_monitors()
       return [res[0].width, res[0].height]
   
    def get_center_of_image(bbox):
        if len(bbox) != 4:
            raise ValueError('bbox must have 4 values')
        return [get_int((bbox[0] + bbox[2])) / 2, get_int((bbox[1] + bbox[3]) / 2)]

    def get_pos(pos):
        for i in pos:
            if i > 1: raise ValueError('pos must be lower than 1')

        return [get_int(pos[0] * Screen.width), get_int(pos[1] * Screen.height)]
        
    @staticmethod
    def get_text_pos(orig_bbox, gray_mode=False):
        # we have the bbox in percentages
        if len(orig_bbox) == 4 and orig_bbox[0] < 1:
            orig_bbox = [
                get_int(orig_bbox[0] * Screen.width),
                get_int(orig_bbox[1] * Screen.height),
                get_int(orig_bbox[2] * Screen.width),
                get_int(orig_bbox[3] * Screen.height)
            ]
        image = Screen.prepare_image(orig_bbox, gray_mode)
        result = reader.readtext('./toDelete.png', decoder='greedy', beamWidth=1, batch_size=1, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        
        text_positions = []
        for (bbox, text, prob) in result:
            if prob > 0.5:  # Filter out low-confidence results
                text_positions.append({
                    'text': text,
                    'position': [orig_bbox[0] + bbox[0][0], orig_bbox[1] + bbox[0][1]]
                })
        
        return text_positions
        
    @staticmethod
    def prepare_image(bbox, gray_mode):
        if len(bbox) != 4: raise ValueError('bbox must have 4 values')
        
        new_bbox = [get_int(i) for i in bbox]
        image = ImageGrab.grab(new_bbox)
        if gray_mode:
            image = image.convert('RGB')
            pixels = image.load()
            for i in range(image.width):
             for j in range(image.height):
                r, g, b = pixels[i, j]
                if not (r > 200 and g > 200 and b > 200):  # If not white
                    r = int(r * 0.5)
                    g = int(g * 0.5)
                    b = int(b * 0.5)
                pixels[i, j] = (r, g, b)
        image.save('./toDelete.png')
        
        return image

    @staticmethod
    def is_match_with_one_difference(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()

        if abs(len(str1) - len(str2)) > 1: return False
        
        # Count the number of differences
        differences = 0
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                differences += 1
                if differences > 1:
                    return False
        
        # Return True if there are 0 or 1 differences
        return differences <= 1
    
    