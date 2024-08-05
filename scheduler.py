from do_work import start_working
from open import close_app
from datetime import datetime

from git import update_project
from utils import delay
from mail import Mail

try:
    print("Starting the application...")
    message = "started the work " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Mail.send(message, subject="DC")
    start_working()
    message="[Success] ... " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Mail.send(message=message, subject="DC")
except Exception as e:
    print('[Error is]: ', e)
    message = '[Error is]: ' + str(e) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Mail.send(message=message, subject="DC")
close_app()
update_project()
