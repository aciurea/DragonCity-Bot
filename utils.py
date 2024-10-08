from python_imagesearch.imagesearch import (imagesearch, imagesearcharea, imagesearch_count)
from screeninfo import get_monitors
import time


def get_screen_resolution():
    res = get_monitors()

    if len(res) > 1:
        mon = res[0] if res[0].width < res[1].width else res[1]
        return f'{mon.width}x{mon.height}'
    return f'{res[0].width}x{res[0].height}'


def get_path(path):
    return f'{path}.png'


# It retries 10 times which means 5 seconds for the image to appear
def getImagePositionRegion(path, x1, y1, x2=1600, y2=900, precision=0.8, retries=10, speed=0.5):
    image = imagesearcharea(path, x1, y1, x2, y2, precision)

    while not exists(image):
        image = imagesearcharea(path, x1, y1, x2, y2, precision)
        if retries == 0: return [image[0] + x1, image[1] + y1] if exists(image) else [-1]
        retries -= 1
        delay(speed)
    return [image[0] + x1, image[1] + y1]


def getImagePositonCount(path):
    return imagesearch_count(path, precision=0.98)


def delay(seconds):
    if seconds < 0:
        seconds = 0
    time.sleep(seconds)


def exists(value):
    return value is not None and value[0] is not None and value[0] != -1


def getImagePosition(path, tries=10, precision=0.8, seconds=0.5):
    res = get_monitors()
    image = imagesearcharea(path, 0, 0, res[0].width, res[0].height, precision)

    while (not exists(image)):
        tries -= 1
        image = imagesearch(path, precision)
        if (tries == 0):
            return image
        delay(seconds)

    return image


def get_int(num):
    return int(round(num))


def get_monitor_quarters():
    res = get_monitors()[0]
    piece = get_int(res.height / 4)
    horizontal_piece = get_int(res.width / 8)

    return {
        "top_left": [0, 0, get_int(res.width / 2), get_int(res.height / 2)],
        "top_right": [get_int(res.width / 2), 0, res.width, get_int(res.height / 2)],
        "bottom_right": [get_int(res.width / 2), get_int(res.height / 2), res.width, res.height],
        "bottom_left": [0, get_int(res.height / 2), get_int(res.width / 2), res.height],
        "1stRow": [0, 0, res.width, piece],
        "2ndRow": [0, piece, res.width, piece * 2],
        "3rdRow": [0, piece * 2, res.width, piece * 3],
        "4thRow": [0, piece * 3, res.width, piece * 4],
        "half4thRow": [get_int(res.width / 2), piece * 3, res.width, piece * 4],

        "1stCol": [0, 0, horizontal_piece, res.height],
        "lastCol": [res.width - horizontal_piece, 0, res.width, res.height],
        "1stHorHalf": [0, 0, res.width, piece * 2],
        "2ndHorHalf": [0, piece * 2, res.width, res.height],
        "1stVerHalf": [0, 0, horizontal_piece * 4, res.height],
        "2ndVerHalf": [horizontal_piece * 4, 0, res.width, res.height],
        "full": [0, 0, res.width, res.height],
        "center": [get_int(res.width / 2), get_int(res.height / 2)]
    }


def is_in_time(start, limit):
    return (time.time() - start) < limit
