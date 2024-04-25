from tkinter import Tk, ttk
from tkinter import *
import requests
import json

window = Tk()
window.geometry('700x550')
window.configure(bg="white")


def convert():
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
        cur_1 = from_combo.get()
        cur_2 = to_combo.get()
        amt = amount.get()
        querystring = {"from": cur_1, "to": cur_2, "amount":amt}

        headers = {
            "X-RapidAPI-Key": "8d71d6105amsh0cee3698480ac43p185889jsn96cbf8f82b3b",
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        final_result = json.loads(response.text)
        a = final_result["result"]["convertedAmount"]
        result = Label(main, text=a, width=36, height=2, pady=7, relief="solid", anchor=CENTER,
                       font=("Arial", 15, " bold"), bg="white", fg="black")
        result.place(x=130, y=270)

def clear():
    result = Label(main, text="", width=36, height=2, pady=7, relief="solid", anchor=CENTER,
                   font=("Arial", 15, " bold"), bg="white", fg="black")
    result.place(x=130, y=270)


logo = Frame(window, width=700, height=90,bg="black")
logo.grid(row=0, column=0)

main = Frame(window, width=700,height=550,bg="grey")
main.grid(row=1, column=0)

app_name = Label(logo,text="CURRENCY CONVERTER",padx=0,pady=30,anchor=CENTER,font=("Times new roman",22,"bold"),bg="black",fg="white")
app_name.place(x=200,y=0)

currency = ['INR','DXB','ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD ','BMD','BOB','BAM','BWP','BGN','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP','SVC','EUR','FKP','FJD','GHS','GIP','GTQ','GGP','USD','GYD','HNL','HKD','HUF','ISK']

from_label = Label(main, text="From ",width=8,height=1, pady=0,padx=0, relief="flat", anchor=NW, font=("Arial",12,"bold"),bg="white",fg="black")
from_label.place(x=130, y=55)
from_combo = ttk.Combobox(main, width=8,  font=("Arial",11,"bold"))
from_combo['values'] = currency
from_combo.place(x=130,y=95)

to_label = Label(main, text="To ",width=8,height=1, pady=0,padx=0, relief="flat", anchor=NW, font=("Arial",12,"bold"),bg="white",fg="black")
to_label.place(x=480, y=55)
to_combo = ttk.Combobox(main, width=8,justify=CENTER, font=("Arial",11,"bold"))
to_combo['values'] = currency
to_combo.place(x=480,y=95)

amount = Entry(main, width=36, font=("Arial",10,"bold"),relief=SOLID)
amount.place(x=230,y=160)

convert_button = Button(main, text="Converter", width=20, height=2, bg="light green", fg="white", font=("Arial",10,"bold"),relief=SOLID,activebackground="grey",command=convert)
convert_button.place(x=130,y=200)

clear_button = Button(main, text="Clear", justify=CENTER,width=20, height=2, bg="#552334", fg="white", font=("Arial",10,"bold"),relief=SOLID,activebackground="#552355",command=clear)
clear_button.place(x=390,y=200)



window.mainloop()