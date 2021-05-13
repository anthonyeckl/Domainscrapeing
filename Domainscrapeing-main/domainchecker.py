from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import *
import time

class DomainChecker():

    def __init__(self, cdomains):
        self.domains_to_be_checked = cdomains
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.domcomp.com/")

    def check_domains_print(self):

        for i, x in enumerate(self.domains_to_be_checked):

            domain_search_bar = self.driver.find_element_by_id("filter")
            domain_search_bar.clear()
            domain_search_bar.send_keys(self.domains_to_be_checked[i])
            domain_search_bar.send_keys(Keys.ENTER)

            self.driver.execute_script("window.scrollTo(0, 400)")

            time.sleep(2)

            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            # with open("page_source.html", "w") as f:
            # f.write(driver.page_source)
            inner_tlds = soup.find_all(class_="tld", limit=17)
            print("------------------------------------")
            print(self.domains_to_be_checked[i])
            # print(inner_tlds)
            # print(len(inner_tlds))
            parents = []
            for t in inner_tlds:
                parents.append(t.parent.get("class"))
            # print(parents)
            # print(len(parents))
            results = []
            for i, t in enumerate(inner_tlds):
                try:
                    results.append(parents[i][0])
                except:
                    results.append("ERROR")
                # print(t.find("a").get_text() + " - " + res)
            print(results)
            num_results = []
            for r in results:
                if r == "available":
                    num_results.append(1)
                elif r == "registered":
                    num_results.append(0)
                elif r == "ERROR":
                    num_results.append(2)
            print(num_results)

            print("------------------------------------")

        self.driver.close()

    def check_domains(self):

        final_result = []

        for i, x in enumerate(self.domains_to_be_checked):

            domain_search_bar = self.driver.find_element_by_id("filter")
            domain_search_bar.clear()
            domain_search_bar.send_keys(self.domains_to_be_checked[i])
            domain_search_bar.send_keys(Keys.ENTER)

            self.driver.execute_script("window.scrollTo(0, 400)")

            time.sleep(2)

            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            # with open("page_source.html", "w") as f:
            # f.write(driver.page_source)
            inner_tlds = soup.find_all(class_="tld", limit=17)
            #print("------------------------------------")
            #print(self.domains_to_be_checked[i])
            # print(inner_tlds)
            # print(len(inner_tlds))
            parents = []
            for t in inner_tlds:
                parents.append(t.parent.get("class"))
            # print(parents)
            # print(len(parents))
            results = []
            for i, t in enumerate(inner_tlds):
                try:
                    results.append(parents[i][0])
                except:
                    results.append("ERROR")
                # print(t.find("a").get_text() + " - " + res)
            #print(results)
            num_results = []
            for r in results:
                if r == "available":
                    num_results.append(1)
                elif r == "registered":
                    num_results.append(0)
                elif r == "ERROR":
                    num_results.append(2)
            #print(num_results)
            final_result.append(num_results)
            #print("------------------------------------")

        self.driver.close()
        return final_result

def main():
    domain_to_be_checked = ["amazon", "ebay", "musslos"]
    print(DomainChecker(domain_to_be_checked).check_domains())
    DomainChecker(domain_to_be_checked).check_domains_print()
if __name__ == "__main__":
   main()


"""




#driver = webdriver.Firefox()
#driver.get("https://www.domcomp.com/")


def check_domains(domain_list):

    for i, x in enumerate(domain_list):

        domain_search_bar = driver.find_element_by_id("filter")
        domain_search_bar.clear()
        domain_search_bar.send_keys(domain_list[i])
        domain_search_bar.send_keys(Keys.ENTER)

        driver.execute_script("window.scrollTo(0, 400)")

        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")


        #with open("page_source.html", "w") as f:
            #f.write(driver.page_source)
        inner_tlds = soup.find_all(class_="tld", limit=17)
        print("------------------------------------")
        print(domain_list[i])
        #print(inner_tlds)
        #print(len(inner_tlds))
        parents = []
        for t in inner_tlds:
            parents.append(t.parent.get("class"))
        #print(parents)
        #print(len(parents))
        results = []
        for i, t in enumerate(inner_tlds):
            try:
                results.append(parents[i][0])
            except:
                results.append("ERROR")
            #print(t.find("a").get_text() + " - " + res)
        print(results)
        num_results = []
        for r in results:
            if r == "available":
                num_results.append(1)
            elif r == "registered":
                num_results.append(0)
            elif r == "ERROR":
                num_results.append(2)
        print(num_results)

        print("------------------------------------")


check_domains(domain_to_be_checked)

driver.close()

"""