import sqlite3
import datetime

#testdomainlist = [['joelbodine', '.com', '2', '-', '628', '12', '31S'], ['masonenergy', '.com', '30', '30', '1518', '128', '31S']]


def datapackage_encrypter(package):
    package_converted = []
    datastring = ""
    package_converted.append(package[0])
    package_converted.append(package[1])
    for i in range(len(package)-2):
        datastring = datastring + package[i+2] + "/"
    package_converted.append(datastring)
    return package_converted

#print(datapackage_encrypter(testdomainlist[0]))

#['joelbodine', '.com', '2/-/628/12/31S/']

def datapackage_decrypter(package_converted):
    normal_package = []
    normal_package.append(package_converted[0])
    normal_package.append(package_converted[1])
    datastring = package_converted[2]
    for i in range(5):
        print("ds before", datastring)
        normal_package.append(datastring[:datastring.find("/")])
        datastring = datastring[datastring.find("/")+1:]
        print("ds after", datastring)

    return normal_package

#print(datapackage_decrypter(['joelbodine', '.com', '2/-/628/12/31S/']))



#print(raw_converter(testdomainlist[0]))

class GodaddyDb():

    def __init__(self, name):
        self.name = name
        self.basedb = sqlite3.connect(name)
        self.c = self.basedb.cursor()
        print("Database opened:" + self.name)

    def initiate_db(self):
        self.c.execute("""CREATE TABLE godaddy_auction_scrape(
            domainname text,
            domainextension text,
            datastring text,
            timedate timestamp
            
        )""")
        self.basedb.commit()
        #[domainname, bids, traffic, estimated_value, price, time_left]

    def close_db(self):
        self.basedb.close()
        print("Database closed:" + self.name)

    def check_domain(self, domain_name):

        self.c.execute("SELECT * FROM godaddy_auction_scrape WHERE domainname = :domainname", {"domainname": domain_name})

        ret = len(self.c.fetchall())
        return ret

    def insert_domain(self, domain_info_list):
        #print("l2", self.check_domain(domain_name))
        if self.check_domain(domain_info_list[0]) == 0:
            #self.c.execute(
               # "INSERT INTO godaddy_auction_scrape VALUES (:name, :ext, :bids, :traffic, :estimatedvalue, :price, :time)",
                #{"name": domain_info_list[0], "ext": domain_info_list[1], "bids":domain_info_list[2], "traffic":domain_info_list[3], "estimatedvalue":domain_info_list[4], "price":domain_info_list[5], "time":domain_info_list[6]})
            self.c.execute(
                "INSERT INTO godaddy_auction_scrape VALUES (:domainname, :domainextension, :datastring, :timedate)",
                {"domainname": domain_info_list[0], "domainextension": domain_info_list[1], "datastring": domain_info_list[2], "timedate":datetime.datetime.now()})

        else:
            print("Eintrag bereits vorhanden. Erstelle weiteren Eintrag.")
            self.c.execute(
                "INSERT INTO godaddy_auction_scrape VALUES (:domainname, :domainextension, :datastring, :timedate)",
                {"domainname": domain_info_list[0], "domainextension": domain_info_list[1],
                 "datastring": domain_info_list[2], "timedate": datetime.datetime.now()})

        self.basedb.commit()

    def get_domain_by_name(self, domain_name):
        self.c.execute("SELECT * FROM godaddy_auction_scrape WHERE domainname=:name", {"name": domain_name})
        ret = self.c.fetchone()
        if ret == None:
            ret = "Nicht vorhanden"
        return ret

    def remove_domain(self, domain_name, domain_extension):

        self.c.execute("DELETE from godaddy_auction_scrape WHERE domainname = :name AND domainextension = :ext",
                    {"name": domain_name, "ext": domain_extension})
        self.basedb.commit()

    def print_db(self):
        self.c.execute("SELECT * FROM godaddy_auction_scrape")
        all_domains = self.c.fetchall()
        for x in all_domains:
            print(x)

tst = [['liberalclub', '.biz', '27/180/-/80/28S/'], ['eurosteelline', '.com', '6/128/942/45/28S/'], ['inkmaniacs', '.com', '6/2/1246/31/28S/']]
gdb = GodaddyDb("godaddyauction.db")
gdb.insert_domain(tst[1])
#gdb.initiate_db()
gdb.print_db()
gdb.close_db()
