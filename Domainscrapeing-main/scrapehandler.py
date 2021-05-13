from namecheapscraper import main as ncmain
from godaddyscraper import main as gdmain
from namecheapauctiondb import NamecheapDb
from godaddyauctiondb import GodaddyDb
import schedule
import time
from datetime import datetime
import threading

def nc_data_to_base(data):
	ncdb = NamecheapDb("namecheapauction.db")
	print("start saving scrapedata")
	for dpack in data:
		try:
			ncdb.insert_domain(dpack)
		except Exception as e:
			print("ERROR while saving to db at:")
			print(dpack)
	print("finished saving scrapedata")
	ncdb.close_db()
	print("Database (Namecheap) closed")
	
def gd_data_to_base(data):
	gddb = GodaddyDb("godaddyauction.db")
	print("start saving scrapedata")
	for dpack in data:
		try:
			gddb.insert_domain(dpack)
		except Exception as e:
			print("ERROR while saving to db at:")
			print(dpack)
	print("finished saving scrapedata")
	gddb.close_db()
	print("Database (Godaddy) closed")
	
	



def run_threaded(funktion):
    thread = threading.Thread(target=funktion)
    thread.start()
    
def do_namecheapscrape():
    print(20*"#")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    # SCRAPE
    nc_res = ncmain()
    print("finished namecheapscrape")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    
    # DATABASE
    print("----- Start writing to Database -----")
    nc_data_to_base(nc_res)
    print("----- Finished writing to Database -----")
    
    print(20*"#")
    
def do_godaddyscrape():
    print(20*"#")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    # SCRAPE
    gd_res = gdmain()
    print("finished godaddyscrape")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    
    # DATABASE
    print("----- Start writing to Database -----")
    gd_data_to_base(gd_res)
    print("----- Finished writing to Database -----")
    
    print(20*"#")

def print_time():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(current_time)
    
def main():
    #schedule.every(5).seconds.do(run_threaded, allefuenf)
    schedule.every().hour.at(":36").do(run_threaded, do_namecheapscrape)
    schedule.every().hour.at(":46").do(run_threaded, do_godaddyscrape)
    schedule.every().minute.do(print_time)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
        
if __name__ == "__main__":
    main()
