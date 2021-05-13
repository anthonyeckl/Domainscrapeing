from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import *
from selenium.webdriver.chrome.options import Options
import time
from godaddyauctiondb import datapackage_encrypter
from pyvirtualdisplay import Display

"""
def raw_converter(package):
    indices = [2, 3, 4, 5]
    for x in indices:
        if package[x] == "-":
            package[x] = 0
        elif package[x] != "ERROR":
            package[x] = int(package[x])
    return package
"""
def tr_processing(tr_html):
    results = []
    no = 0
    for singletr in tr_html:
        # extract list of td's
        tds = singletr.find_all("td")
        ###########################################################
        # ---------[domainname, bids, traffic, estimated_value, price, time_left] ----------
        # get all the information
        try:
            raw_domain = tds[3].find("span").get_text().replace("\xa0", "")
            domainext = raw_domain[raw_domain.find("."):]
            domainname = raw_domain[:raw_domain.find(".")]
        except Exception as e:
            domainname = "ERROR"
            domainext = "ERROR"
            print(e)
        try:
            bids = tds[4].find("a").get_text().replace("\xa0", "")
        except Exception as e:
            bids = -1
            print(e)

        try:
            traffic = tds[5].get_text().replace("\xa0", "")
        except Exception as e:
            traffic = 0
            print(e)


        try:
            estimated_value = tds[6].find("span").get_text().replace("\xa0", "").replace(".", "").replace("€", "").replace("Weniger als ", "")
        except Exception as e:
            estimated_value = 0
            print(e)

        try:
            price = tds[7].get_text().replace("\xa0", "").replace(" *", "").replace("€", "").replace(".", "")
        except Exception as e:
            price = -1
            print(e)

        try:
            time_left = tds[9].get_text().replace("\xa0", "").replace("Extended", "")
        except Exception as e:
            time_left = "ERROR"
            print(e)

        #############################################################################

        # insert into a list
        info_list = [domainname, domainext, bids, traffic, estimated_value, price, time_left]
        results.append(info_list)
        #print(info_list)
        #print(no)
        no += 1
    return results

def main():
    display = Display(visible=0, size=(1280,720))
    display.start()
    try:
        # selenium setup
        options = Options()
        options.add_argument("window-size=1600,1000")
        driver = webdriver.Chrome(options=options ,executable_path=r'/usr/lib/chromium-browser/chromedriver')
        driver.get("https://de.auctions.godaddy.com/")

        # table length configuration
        dropdown = driver.find_element_by_id("ddlRowsToReturn")

        drp = Select(dropdown)
        sel500 = drp.select_by_visible_text("500")
        print("number clicked")

        #try:
            #WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "search-table")))
        #except Exception as e:
            #print("warten fehlgeschlagen")
            #print(e)
            
        w = True
        while w:
            gray_overlay = driver.find_element_by_id("divOverlaySRA")
            if gray_overlay.value_of_css_property('display') == "none":
                w = False
            print("--1-- overlay still there")
            time.sleep(2)
            
        #element = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.ID, "search-table"))
        #)
        
        #print("wait20")
        #time.sleep(20)
        w = True
        while w:
            gray_overlay = driver.find_element_by_id("divOverlaySRA")
            if gray_overlay.value_of_css_property('display') == "none":
                w = False
            print("--2-- overlay still there")
            time.sleep(2)
        
        # table time sorting configuration
        table = driver.find_element(By.ID,"search-table")
        timesorting = table.find_element_by_tag_name("tbody")
        tr = timesorting.find_element_by_tag_name("tr")
        sort = tr.find_elements_by_tag_name("td")
        sort[-1].click()
        print("time clicked")
        print("time target \n", sort[-1].get_attribute("innerHTML"))
        


        time.sleep(10)

        # process html code
        html = driver.page_source
        driver.close()
        soup = BeautifulSoup(html, "html.parser")
        resulttable = soup.find(id="tblSearchResults")
        #srRow1s = resulttable.find_all(class_ = "srRow1")
        #srRow2s = resulttable.find_all(class_ = "srRow2")
        srRows = resulttable.findAll(True, {'class': ['srRow1', 'srRow2']})

        #print(resulttable.prettify())
        all_results = tr_processing(srRows) 
        print(all_results)
        print(len(all_results))
        
        display.stop()
        
        return all_results
    except Exception as e:
        print("Fehlgeschlagen")
        print(e)
        driver.close()
        display.stop()
        return []


if __name__ == "__main__":
    main()
