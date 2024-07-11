from do_work import start_working
from open import close_app
from datetime import datetime

from utils import delay

try:
    print("Starting the application...")
    start_working()
except Exception as e:
    print('[Error is]: ')
finally:
    close_app()
    raise Exception("Exit ... " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
