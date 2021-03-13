import schedule
import time
from datetime import datetime
import threading

def job():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(current_time, "Am arbeiten")

def allefuenf():
    for i in range(4):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print(current_time,"hallo",i)
        time.sleep(1)

def run_threaded(funktion):
    thread = threading.Thread(target=funktion)
    thread.start()


schedule.every(5).seconds.do(run_threaded, allefuenf)

while True:
    schedule.run_pending()
    time.sleep(1)
