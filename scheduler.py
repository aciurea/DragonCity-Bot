from do_work import start_working
from open import close_app
from datetime import datetime
from PIL import ImageGrab

from git import update_project
from utils import delay
from mail import Mail

try:
    print("Starting the application...")
    work_message = start_working()

    message="[Success] ... " + datetime.now().strftime("%Y-%m-%d %H:%M:%S \n\n") + work_message
    Mail.send(message=message, subject="DC")
except Exception as e:
    print('[Error is]: ', e)
    message = '[Error is]: ' + str(e) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ImageGrab.grab().save('./log/' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '.png')
    Mail.send(message=message, subject="DC")
close_app()
update_project()
