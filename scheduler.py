import time

from do_work import start_working

while True:
    try:
        print("Starting the application...")
        start_working()
    except Exception as e:
        print("Script crashed, restarting...", e)
    finally:
            one_hour = 1800
            print("Waiting for 1 hour...")
            # Wait for 30 minutes (1800 seconds)
            time.sleep(one_hour)
