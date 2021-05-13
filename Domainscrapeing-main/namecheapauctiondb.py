import sqlite3
import datetime

class NamecheapDb():

    def __init__(self, name):
        self.name = name
        self.basedb = sqlite3.connect(name)
        self.c = self.basedb.cursor()
        print("Database opened:" + self.name)

    def initiate_db(self):
        self.c.execute("""CREATE TABLE namecheap_auction_scrape(
            domainname text,
            domainextension text,
            price integer,
            timedate timestamp

        )""")
        self.basedb.commit()

    def close_db(self):
        self.basedb.close()
        print("Database closed:" + self.name)

    def check_domain(self, domain_name):

        self.c.execute("SELECT * FROM namecheap_auction_scrape WHERE domainname = :domainname",
                       {"domainname": domain_name})

        ret = len(self.c.fetchall())
        return ret

    def insert_domain(self, domain_info_list):
        # print("l2", self.check_domain(domain_name))
        if self.check_domain(domain_info_list[0]) == 0:
            # self.c.execute(
            # "INSERT INTO godaddy_auction_scrape VALUES (:name, :ext, :bids, :traffic, :estimatedvalue, :price, :time)",
            # {"name": domain_info_list[0], "ext": domain_info_list[1], "bids":domain_info_list[2], "traffic":domain_info_list[3], "estimatedvalue":domain_info_list[4], "price":domain_info_list[5], "time":domain_info_list[6]})
            self.c.execute(
                "INSERT INTO namecheap_auction_scrape VALUES (:domainname, :domainextension, :price, :timedate)",
                {"domainname": domain_info_list[0], "domainextension": domain_info_list[1],
                 "price": domain_info_list[2], "timedate": datetime.datetime.now()})

        else:
            #print("Eintrag bereits vorhanden. Erstelle weiteren Eintrag.")
            self.c.execute(
                "INSERT INTO namecheap_auction_scrape VALUES (:domainname, :domainextension, :price, :timedate)",
                {"domainname": domain_info_list[0], "domainextension": domain_info_list[1],
                 "price": domain_info_list[2], "timedate": datetime.datetime.now()})
        self.basedb.commit()

    def get_domain_by_name(self, domain_name):
        self.c.execute("SELECT * FROM namecheap_auction_scrape WHERE domainname=:name", {"name": domain_name})
        ret = self.c.fetchone()
        if ret == None:
            ret = "Nicht vorhanden"
        return ret

    def remove_domain(self, domain_name, domain_extension):

        self.c.execute("DELETE from namecheap_auction_scrape WHERE domainname = :name AND domainextension = :ext",
                       {"name": domain_name, "ext": domain_extension})
        self.basedb.commit()

    def print_db(self):
        self.c.execute("SELECT * FROM namecheap_auction_scrape")
        all_domains = self.c.fetchall()
        for x in all_domains:
            print(x)
    
    def db_length(self):
        self.c.execute("SELECT * FROM namecheap_auction_scrape")
        all_domains = self.c.fetchall()
        return len(all_domains)


#tst = [['rebot', '.co.uk', 500, 'Tue Mar  9 18:32:05 2021'],
#['gamefarmauction', '.com', 20, 'Tue Mar  9 18:32:05 2021'],
#['meetfood', '.de', 99, 'Tue Mar  9 18:32:05 2021']]
#gdb = NamecheapDb("namecheapauction.db")
#gdb.insert_domain(tst[0])
#gdb.initiate_db()
#gdb.print_db()
#gdb.close_db()
