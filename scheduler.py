from do_work import start_working
from open import close_app
from datetime import datetime

from utils import delay
from mail import Mail

error = False
try:
    print("Starting the application...")
    start_working()
except Exception as e:
    print('[Error is]: ', e)
    error = '[Error is]: ' + str(e)
finally:
    dd = "Exit ... " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = ("" if error == False else error) + " " + dd
    Mail.send(message=message, subject="DC")
    close_app()
