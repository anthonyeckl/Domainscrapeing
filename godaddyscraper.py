from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import *
import time
from godaddyauctiondb import datapackage_encrypter

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
            bids = "ERROR"
            print(e)

        try:
            traffic = tds[5].get_text().replace("\xa0", "")
        except Exception as e:
            traffic = "-"
            print(e)


        try:
            estimated_value = tds[6].find("span").get_text().replace("\xa0", "").replace(".", "").replace("€", "").replace("Weniger als ", "")
        except Exception as e:
            estimated_value = "-"
            print(e)

        try:
            price = tds[7].get_text().replace("\xa0", "").replace(" *", "").replace("€", "").replace(".", "")
        except Exception as e:
            price = "ERROR"
            print(e)

        try:
            time_left = tds[9].get_text().replace("\xa0", "").replace("Extended", "")
        except Exception as e:
            time_left = "ERROR"
            print(e)

        #############################################################################

        # insert into a list
        info_list = [domainname, domainext, bids, traffic, estimated_value, price, time_left]
        results.append(datapackage_encrypter(info_list))
        print(info_list)
        print(no)
        no += 1
    return results

def main():
    # selenium setup
    driver = webdriver.Firefox()
    driver.get("https://de.auctions.godaddy.com/")

    # table length configuration
    dropdown = driver.find_element_by_id("ddlRowsToReturn")

    drp = Select(dropdown)
    sel500 = drp.select_by_visible_text("500")

    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-table")))
    except:
        print("fehlgeschlagen")

    # table time sorting configuration
    table = driver.find_element(By.ID,"search-table")
    timesorting = table.find_element_by_tag_name("tbody")
    tr = timesorting.find_element_by_tag_name("tr")
    sort = tr.find_elements_by_tag_name("td")
    print(sort[-1].click())


    time.sleep(5)

    # process html code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    resulttable = soup.find(id="tblSearchResults")
    #srRow1s = resulttable.find_all(class_ = "srRow1")
    #srRow2s = resulttable.find_all(class_ = "srRow2")
    srRows = resulttable.findAll(True, {'class': ['srRow1', 'srRow2']})

    #print(resulttable.prettify())
    print(tr_processing(srRows))
    print(len(srRows))
    #print(tr_processing(srRow2s))
    #temp1 = srRow1s[0].find_all("td")
    #temp1 = temp1[2]
    #print(srRow1s[0].find_all("td"))

    #print(soup)
    #print(srRow1s)
    #print(srRow2s)
    #dropdown.click()
    #print(driver.title)
    #print(driver.current_url)


if __name__ == "__main__":
    main()
