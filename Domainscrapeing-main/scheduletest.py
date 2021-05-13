import schedule
import time
from datetime import datetime
import threading
from namecheapscraper import main as ncmain
from godaddyscraper import main as gdmain

"""
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
"""

def run_threaded(funktion):
    thread = threading.Thread(target=funktion)
    thread.start()
    
def do_namecheapscrape():
    print(20*"#")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    ncmain()
    print("finished namecheapscrape successfully")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    print(20*"#")
    
def do_godaddyscrape():
    print(20*"#")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    gdmain()
    print("finished godaddyscrape successfully")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    print(20*"#")

    
def main():
    #schedule.every(5).seconds.do(run_threaded, allefuenf)
    schedule.every().hour.at(":07").do(run_threaded, do_namecheapscrape)
    #schedule.every().hour.at(":03").do(run_threaded, do_godaddyscrape)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
        
if __name__ == "__main__":
    main()
