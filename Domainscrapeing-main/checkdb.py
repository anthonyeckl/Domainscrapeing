import sqlite3


#basedb = sqlite3.connect("checkdb.db")
#c = basedb.cursor()
class searchdb():

    def __init__(self, name):
        self.name = name
        self.basedb = sqlite3.connect(name)
        self.c = self.basedb.cursor()
        print("Database opened:" + self.name)


    def close_db(self):
        self.basedb.close()
        print("Database closed:" + self.name)

    # checks for existence of Domain / returns 1 if Domain already exists, 0 if not
    def check_domain(self, name):

        self.c.execute("SELECT * FROM checked_domain WHERE name = :name", {"name": name})

        ret = len(self.c.fetchall())
        return ret

    def insert_domain(self, domain_name, results):
        #print("l2", self.check_domain(domain_name))
        if self.check_domain(domain_name) == 0:
            self.c.execute(
                "INSERT INTO checked_domain VALUES (:name, :com, :net, :org, :info, :me, :io, :link, :click, :help, :global, :biz, :co, :us, :uk, :couk, :ru, :de)",
                {"name": domain_name, "com": results[0], "net": results[1], "org": results[2], "info": results[3],
                 "me": results[4], "io": results[5], "link": results[6], "click": results[7], "help": results[8],
                 "global": results[9], "biz": results[10], "co": results[11], "us": results[12], "uk": results[13],
                 "couk": results[14], "ru": results[15], "de": results[16]})
        else:
            print("Eintrag bereits vorhanden")
        self.basedb.commit()

    #returns domain and data by name search
    def get_domain_by_name(self, domain_name):
        self.c.execute("SELECT * FROM checked_domain WHERE name=:name", {"name": domain_name})
        ret = self.c.fetchone()
        if ret == None:
            ret = "Nicht vorhanden"
        return ret

    def remove_domain(self, domain_name):

        self.c.execute("DELETE from checked_domain WHERE name = :name",
                    {"name": domain_name})
        self.basedb.commit()

"""
def setup_table():
    c.execute("CREATE TABLE checked_domain(
                name text,
                com integer,
                net integer,
                org integer,
                info integer,
                me integer,
                io integer,
                link integer,
                click integer,
                help integer,
                global integer,
                biz integer,
                co integer,
                us integer,
                uk integer,
                couk integer,
                ru integer,
                de integer
                )")
    basedb.commit()

def check_domain(name):
    basedb = sqlite3.connect("checkdb.db")
    c = basedb.cursor()
    c.execute("SELECT * FROM checked_domain WHERE name = :name", {"name": name})
    basedb.close()
    #print("l1",len(c.fetchall()))
    #print("p1", c.fetchall())
    ret = len(c.fetchall())
    basedb.close()
    return ret

def insert_domain(name, results):
    basedb = sqlite3.connect("checkdb.db")
    c = basedb.cursor()
    print("l2",check_domain(name))
    if check_domain(name) == 0:
        with basedb:
            c.execute("INSERT INTO checked_domain VALUES (:name, :com, :net, :org, :info, :me, :io, :link, :click, :help, :global, :biz, :co, :us, :uk, :couk, :ru, :de)", {"name": name,"com":results[0],"net":results[1],"org":results[2],"info":results[3],"me":results[4],"io":results[5],"link":results[6],"click":results[7],"help":results[8],"global":results[9],"biz":results[10],"co":results[11],"us":results[12],"uk":results[13],"couk":results[14],"ru":results[15],"de":results[16]})
    else:
        print("Eintrag bereits vorhanden")
    basedb.commit()
    basedb.close()

def get_domain_by_name(name):
    basedb = sqlite3.connect("checkdb.db")
    c = basedb.cursor()
    c.execute("SELECT * FROM checked_domain WHERE name=:name", {"name": name})
    ret = c.fetchone()
    if ret == None:
        ret = "Nicht vorhanden"
    basedb.close()
    return ret


def remove_domain(name):
    basedb = sqlite3.connect("checkdb.db")
    c = basedb.cursor()
    with basedb:
        c.execute("DELETE from checked_domain WHERE name = :name",
                  {"name": name})
    basedb.commit()
    basedb.close()

#insert_domain("testdomain", [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0])
#print(get_domain_by_name("testdomain"))
#basedb.close()
"""
#sd = searchdb("checkdb.db")
#print(sd.get_domain_by_name("school"))
#sd.close_db()