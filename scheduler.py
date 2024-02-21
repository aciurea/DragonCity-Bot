import time

from start import start_app

while True:
    try:
        print("Starting the application...")
        start_app()
    except Exception as e:
        print("Script crashed, restarting...", e)
    finally:
            print("Waiting for 1 minute...")
            # Wait for 30 minutes (1800 seconds)
            time.sleep(10)