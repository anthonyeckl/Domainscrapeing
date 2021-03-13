import sqlite3 as lite

conn = lite.connect('godaddyauction.db')
cur = conn.cursor()

def get_posts():
    cur.execute("SELECT * FROM godaddy_auction_scrape")
    all_domains = cur.fetchall()
    for x in all_domains:
        print(x)

get_posts()