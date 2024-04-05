from do_work import start_working
from open import close_app
from datetime import datetime

from utils import delay

while True:
    try:
        print("Starting the application...")
        start_working()
    except Exception as e:
        close_app()
        print("Exit: ", e)
    finally:
            one_hour = 3600
            print("Waiting for 1 hour... ", datetime.now().time())
            # Wait for 30 minutes (1800 seconds)
            delay(one_hour)
