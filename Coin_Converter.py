from currency_converter import CurrencyConverter
import tkinter as tk
c=CurrencyConverter()
#print(c.convert(12,"USD","MAD"))

window = tk.Tk()
window.geometry("500x360")
window.title("Coin Conversion")

def clicked():
    amount = float(entry1.get())
    currency1= entry2.get()
    currency2=entry3.get()
    data= c.convert(amount,currency1,currency2)
    lbl4= tk.Label(window,text=data,font="Times 16 bold").place(x=200, y=300)


lbl = tk.Label(window,text="Coin Conversion",font ="Times 20 bold").place(x=120, y=40)

lbl1=tk.Label(window,text="Enter the amount: ",font="Times 16 bold").place(x=65, y=100)
entry1 =tk.Entry(window)

lbl2=tk.Label(window,text="Enter currency: ",font="Times 16 bold").place(x=65, y=145)
entry2 =tk.Entry(window)

lbl3=tk.Label(window,text="Enter currency desired: ",font="Times 16 bold").place(x=40, y=195)
entry3 =tk.Entry(window).place(x=210,y=195)

button = tk.Button(window,text= "press",font="Times 16 bold",command=clicked).place(x=220, y=250)
entry1.place(x=210,y=100)
entry2.place(x=210,y=150)

window.mainloop()


