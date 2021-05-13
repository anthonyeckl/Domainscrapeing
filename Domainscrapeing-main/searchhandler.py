import os.path
import colorama
from colorama import Fore, Fore, Style
from checkdb import *
from readdomainnames import FileReader
from domainchecker import DomainChecker

colorama.init(autoreset=True)

def start_multi_check():
    validation = False
    source = input("Source txt (No file extension(.txt))")
    if os.path.isfile(source + ".txt"):
        print(Fore.GREEN + "Success:" + Fore.RESET + " Source txt found")
        destination = input("Destination db (No file extension(.db))")
        if os.path.isfile(destination + ".db"):
            print(Fore.GREEN + "Success:" + Fore.RESET + " Destination db found")
            validation = True
        else:
            print(Fore.RED + "ERROR:" + Fore.RESET + " Destination db not found")
    else:
        print(Fore.RED + "ERROR:" + Fore.RESET + " Source txt not found")

    if validation:
        fr_names = FileReader(source).readFile()
        print("fr_names:")
        print(fr_names)
        dc_results = DomainChecker(fr_names).check_domains()
        print("dc_results:")
        print(dc_results)
        next_step = input("Continue with writing to DB (y/n)").lower()
        if next_step == "y":
            sdb = searchdb(destination + ".db")
            for i in range(len(fr_names)):
                sdb.insert_domain(fr_names[i], dc_results[i])
            sdb.close_db()

def single_search_domain():
    destination = input("Destination db (No file extention(.db))")
    validation = False
    if os.path.isfile(destination + ".db"):
        print(Fore.GREEN + "Success:" + Fore.RESET + " Destination db found")
        validation = True
    else:
        print(Fore.RED + "ERROR:" + Fore.RESET + " Destination db not found")


    if validation:
        target_domain = str(input("type in the domain you want to search (no extension): "))
        sdb = searchdb(destination + ".db")
        print(Fore.BLUE + str(sdb.get_domain_by_name(target_domain)))
        sdb.close_db()


def main():
    while True:
        try:
            ask = input("Multicheck(1)/Single DB check(2)")
            ask = int(ask)
            if ask == 1:
                start_multi_check()
            elif ask == 2:
                single_search_domain()
        except ValueError:
            print(Fore.RED + "ERROR:" + Fore.RESET + " Invalid instruction")


if __name__ == "__main__":
    main()
