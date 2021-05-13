import sqlite3 as lite



def get_gd():
    conn = lite.connect('godaddyauction.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM godaddy_auction_scrape")
    all_domains = cur.fetchall()
    for x in all_domains:
        print(x)
    conn.close()
    
def get_nc():
    conn = lite.connect('namecheapauction.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM namecheap_auction_scrape")
    all_domains = cur.fetchall()
    for x in all_domains:
        print(x)
    conn.close()

def len_gd():
    conn = lite.connect('godaddyauction.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM godaddy_auction_scrape")
    all_domains = cur.fetchall()
    conn.close()
    return len(all_domains)
    
def len_nc():
    conn = lite.connect('namecheapauction.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM namecheap_auction_scrape")
    all_domains = cur.fetchall()
    conn.close()
    return len(all_domains)
    
def errors_gd():
    conn = lite.connect('godaddyauction.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM godaddy_auction_scrape WHERE domainname=:name", {"name": "ERROR"})
    all_errors = cur.fetchall()
    conn.close()
    #for x in all_errors:
    #    print(x)
    return len(all_errors)
    
def errors_nc():
    conn = lite.connect('namecheapauction.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM namecheap_auction_scrape WHERE domainname=:name", {"name": "error"})
    all_errors = cur.fetchall()
    conn.close()
    return len(all_errors)


def main():
    print("Godaddy DB Length: ", len_gd())
    print("Godaddy DB Errors: ", errors_gd())
    print("Namecheap DB Length: ", len_nc())
    print("Namecheap DB Errors: ", errors_nc())

if __name__ == "__main__":
    main()
