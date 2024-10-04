from do_work import start_working
from open import OpenApp
from datetime import datetime
from PIL import ImageGrab
from screeninfo import get_monitors

from git import update_project
from mail import Mail

try:
    print("Starting the application...")
    work_message = start_working()

    message = "[Success] ... " + datetime.now().strftime("%Y-%m-%d %H:%M:%S \n\n") + work_message
    Mail.send(message=message, subject="DC")
except Exception as e:
    print('[Error is]: ', e)
    message = '[Error is]: ' + str(e) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = f'./log/{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.png'
    monitors = get_monitors()
    bbox = [0, 0, monitors[0].width, monitors[0].height]
    ImageGrab.grab(bbox).save(path)
    Mail.send(message=message, subject="DC")

OpenApp._close_app()
update_project()
