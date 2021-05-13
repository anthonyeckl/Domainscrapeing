import sqlite3
basedb = sqlite3.connect("testdb.db")

c = basedb.cursor()

# c.execute("""CREATE TABLE domain(
#             name text,
#             end text,
#             price integer
#             )""")
#c.execute("INSERT INTO domain VALUES ('amazon', '.com', 1000)")

def check_new_domain(name, end, price):
    c.execute("SELECT * FROM domain WHERE name = :name AND end = :end AND price = :price", {"name": name, "end": end, "price": price})
    #print("l1",len(c.fetchall()))
    #print("p1", c.fetchall())
    return len(c.fetchall())


def insert_domain(name, end, price):
    print("l2",check_new_domain(name, end, price))
    if check_new_domain(name, end, price) == 0:
        with basedb:
            c.execute("INSERT INTO domain VALUES (:name, :end, :price)", {"name": name, "end": end, "price": price})
    else:
        print("Eintrag bereits vorhanden")


def get_domain_by_name(name):
    c.execute("SELECT * FROM domain WHERE name=:name", {"name": name})
    return c.fetchone()

def update_domain_price(name, end, newprice):
    with basedb:
        c.execute("UPDATE domain SET price = :price WHERE name = :name AND end = :end", {"name": name, "end": end, "price": newprice})

def remove_domain(name, end):
    with basedb:
        c.execute("DELETE from domain WHERE name = :name AND end = :end",
                  {"name": name, "end": end})

#insert_domain("ebay3", ".com", 10)
#remove_domain("musslos", ".com")

c.execute("SELECT * FROM domain WHERE end='.com'")
print(c.fetchall())


basedb.commit()
basedb.close()