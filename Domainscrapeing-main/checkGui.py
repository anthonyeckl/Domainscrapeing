from tkinter import *
from checkdb import *

window = Tk()
window.geometry("500x500")
window.title("Check Domains")

result_label = Label(window)
result_label.pack()


def printdomain():
    sd = searchdb("checkdb.db")
    result_label.configure(text=(sd.get_domain_by_name(single_name_entry.get())))
    sd.close_db()


single_name_entry = Entry(window)
single_name_entry.pack()

get_print_button = Button(window, text="Suchen", command=printdomain)
get_print_button.pack()



window.mainloop()
