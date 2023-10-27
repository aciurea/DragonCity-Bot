import time

def delay(seconds):
    if seconds < 0:
        seconds = 0
    time.sleep(seconds)