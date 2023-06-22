from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import requests
import json 

root = Tk()
root.title("Currency Converter")
root.geometry("600x300")
root.resizable(0,0)
headlabel = Label(root, font=(21), text='Currency Converter')

label1 = Label(root, font=(15), text="Amount:")
label2 = Label(root, font=(15), text="From Currency:")
label3 = Label(root, font=(15), text="To Currency:")
label4 = Label(root,font=(15), text="Converted Amount:")

label0 = Label(root, text='\t').grid(row = 1, column=0)
headlabel.grid(row=2, column=1)
label0 = Label(root, text='\t').grid(row=3,column=0)
label1.grid(row=4, column=1, sticky=W)
label2.grid(row=5, column=1, sticky=W)
label3.grid(row=6, column=1, sticky=W)
label0 = Label(root).grid(row=7, column=0)
label4.grid(row=8, column=1, sticky=W)


url = "http://api.nbp.pl/api/exchangerates/tables/A/"
currency_list = []
timeout = 5
try:
    for i in range(0,len(requests.get(url).json()[0]["rates"])):
        currency_code = requests.get(url, timeout=timeout).json()[0]["rates"][i]["code"]
        currency_list.append(currency_code)
    rates_file = open(r"D:\studia\semestr 2\programowanie\lista_5\rates.json", 'w')
    json.dump(requests.get(url).json()[0], rates_file, indent = 6)
    rates_file.close()
except (requests.ConnectionError, requests.Timeout) as exception:
    rate_file = open(r"D:\studia\semestr 2\programowanie\lista_5\rates.json", 'r') 
    data = json.load(rate_file)
    for i in range(0,len(data["rates"])):
        currency_code = data["rates"][i]["code"]
        currency_list.append(currency_code)

currency_list.append('PLN')
currency_list_2 = sorted(currency_list)
currency1 = StringVar(root)
currency2 = StringVar(root)
currency1.set("currency")
currency2.set("currency")


from_currency = ttk.Combobox(root, values = tuple(currency_list_2), width = 10, textvariable = currency1)

to_currency = ttk.Combobox(root, values = tuple(currency_list_2), width = 10, textvariable = currency2)

from_currency.grid(row=5, column=2, ipadx=25, sticky=E)
to_currency.grid(row=6, column=2, ipadx=25, sticky=E)

amount_field_1 = Entry(root, width=12)
amount_field_1.grid(row=4, column=2, ipadx=28, sticky=E)

amount_field_2 = Label(root, font=(15))
amount_field_2.grid(row=8, column=2, ipadx=33)


def CurrencyConversion():
    from_currency = currency1.get()
    to_currency = currency2.get()
    if (amount_field_1.get() == ""):
        tkinter.messagebox.showinfo("error", "amount not entered")
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo('error', "currency not selected")
    else:
        url_template = "http://api.nbp.pl/api/exchangerates/rates/a/{}/"
        value = float(amount_field_1.get())
        try:
            rate_to_pln = requests.get(url_template.format(from_currency)).json()["rates"][0]["mid"] #rate z from_currency to PLN
            if to_currency != 'PLN':
                rate_from_pln = requests.get(url_template.format(to_currency)).json()["rates"][0]["mid"]
                new_amt = (rate_to_pln * float(value))/rate_from_pln
            else:
                new_amt = rate_to_pln * float(value)
            new_amount = float("{:.2f}".format(new_amt))
            amount_field_2.configure(text=str(new_amount))
        except:
            rates_file = open(r"D:\studia\semestr 2\programowanie\lista_5\rates.json", 'r') 
            data = json.load(rates_file)
            for i in range(0, len(data["rates"])):
                if from_currency==data["rates"][i]["code"]:
                    rate_to_pln = data["rates"][i]["mid"]
            if to_currency != 'PLN':
                for i in range(0, len(data["rates"])):
                    if to_currency==data["rates"][i]["code"]:
                        rate_from_pln = data["rates"][i]["mid"]
                new_amt = (rate_to_pln * float(value))/rate_from_pln
            else:
                for i in range(0, len(data["rates"])):
                    if to_currency==data["rates"][i]["code"]:
                        rate_to_pln = data["rates"][i]["mid"]
                new_amt = rate_to_pln * float(value)
            new_amount = float("{:.4f}".format(new_amt))
            amount_field_2.configure(text=str(new_amount))


def clear_all():
    amount_field_1.delete(0, END)
    amount_field_2.configure(text='')

label0 = Label(root, text='\t\t').grid(row=5, column=3)
convert_button = Button(root, font=(15), text='Convert', width=10, pady=3, bg="black", fg="white", command=CurrencyConversion)
convert_button.grid(row=5, column=4, sticky=E)
label0 = Label(root, text='\t').grid(row=9,column=0)
clear_all_button = Button(root, font=(15), text="Clear All", width=10, pady=3, bg="black", fg="white", command=clear_all)
clear_all_button.grid(row=10, column=2)

exit_button = Button(root, font=(15), text="Exit", width=10, pady=3, bg="dark red", fg="white", command=root.destroy)
exit_button.grid(row=10, column=4)


root.mainloop()