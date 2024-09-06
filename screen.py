from PIL import Image, ImageGrab, ImageEnhance, ImageFilter, ImageOps
from screeninfo import get_monitors

from utils import get_int, get_monitor_quarters

import pytesseract
import os
import time
import easyocr

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
        
        
    @staticmethod
    def get_text_pos(orig_bbox):
        # we have the bbox in percentages
        if len(orig_bbox) == 4 and orig_bbox[0] < 1:
            orig_bbox = [
                get_int(orig_bbox[0] * Screen.width),
                get_int(orig_bbox[1] * Screen.height),
                get_int(orig_bbox[2] * Screen.width),
                get_int(orig_bbox[3] * Screen.height)
            ]
        image = Screen.prepare_image(orig_bbox)
        result = reader.readtext('./toDelete.png', decoder='beamsearch', beamWidth=5, batch_size=1, workers=0, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        
        text_positions = []
        for (bbox, text, prob) in result:
            if prob > 0.5:  # Filter out low-confidence results
                text_positions.append({
                    'text': text,
                    'position': [orig_bbox[0] + bbox[0][0], orig_bbox[1] + bbox[0][1]]
                })
        
        return text_positions
        
    @staticmethod
    def prepare_image(bbox):
        if len(bbox) != 4: raise ValueError('bbox must have 4 values')
        
        new_bbox = [get_int(i) for i in bbox]
        image = ImageGrab.grab(new_bbox)
        image.save('./toDelete.png')
        
        return image

    @staticmethod
    def is_match_with_one_difference(str1, str2):
        # Check if the lengths are different
        if len(str1) != len(str2):
            return False
        
        # Count the number of differences
        differences = 0
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                differences += 1
                if differences > 1:
                    return False
        
        # Return True if there are 0 or 1 differences
        return differences <= 1
    
    