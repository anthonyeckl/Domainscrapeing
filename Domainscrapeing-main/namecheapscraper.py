from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import *
import time
import datetime
from pyvirtualdisplay import Display

def main():
    display = Display(visible=0, size=(1280,720))
    display.start()
    
    try:
        # selenium setup
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        driver.get("https://www.namecheap.com/domains/marketplace/buy-domains/")
        
        all_results = []
        
        for i in range(10):
            print(20*"-")
            print(i)
            # soup setup
            html = driver.page_source
            
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find_all(class_="panel-body")
            table = table[0]
            trs = table.find_all("tr")
            print(len(trs))
            print("start tr parsing")
            for t in trs:
                # PACKAGE domainname, domainextension, timeleft, price, timestamp
                package = []
                tds = t.find_all("td")
                # Complete domain
                try:
                    whole_domain = tds[0].find("a").get_text()
                except:
                    print("could not identify whole domain")
                    whole_domain = "error.error"
                # domainname
                package.append(whole_domain[:whole_domain.find(".")])
                # domainextension
                package.append(whole_domain[whole_domain.find("."):])
                # timeleft
                #package.append(tds[1].get_text().replace("Closing On ",""))
                # price
                price = tds[2].find("span").get_text().replace("$","").replace("€","")
                price = price[:price.find(".")]
                price = price.replace(",","")
                try:
                    price = int(price)
                except:
                    price = 0
                package.append(price)

                #timestamp
                #date_time = datetime.datetime.now()
                #package.append(date_time.strftime("%c"))
                #print(package)
                all_results.append(package)
            print("Current amount:", len(all_results))
            print(20 * "-")
            try:
                cookie_box = driver.find_element_by_class_name("banner-close-button")
                cookie_box.click()
            except:
                pass
            page_bar = driver.find_element_by_tag_name("nc-grid-pager")
            page_bar.find_element_by_class_name("next").click()
            time.sleep(2)
            
        driver.close()
        display.stop()
        print(all_results)
        print(len(all_results))
        return all_results
    except Exception as e:
        print("Fehlgeschlagen")
        print(e)
        driver.close()
        display.stop()
        return []



if __name__ == "__main__":
    x = main()
    print(x)
