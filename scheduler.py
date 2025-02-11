from do_work import start_working
from open import OpenApp
from datetime import datetime
from PIL import ImageGrab
from screeninfo import get_monitors

from git import update_project
from mail import Mail
from utils import get_screen_resolution


def save_log_to_file(message, filename):
    with open(filename, 'w') as file:
        file.write(message)


try:
    print("Starting the application... on resolution ", get_screen_resolution())
    work_message = start_working()

    message = f'[Success]... "{datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")} {work_message} {get_screen_resolution()}'
    Mail.send(message=message, subject="DC")
except Exception as e:
    print('[Error is]: ', e)
    message = '[Error is]: ' + str(e) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = f'./log/{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}'
    monitors = get_monitors()
    bbox = [0, 0, monitors[0].width, monitors[0].height]
    ImageGrab.grab(bbox).save(f'{path}image.png')
    save_log_to_file(message, f'{path}text.txt')
    Mail.send(message=message, subject="DC")

OpenApp._close_app()
update_project()
