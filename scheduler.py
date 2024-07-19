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
    error = e
finally:
    print("Exit ... " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    Mail.send("" if error == False else str(error) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    close_app()
