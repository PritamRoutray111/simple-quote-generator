import random
import tkinter
from tkinter import *
from tkinter import ttk

with open("quote.txt","r") as q:
  quotes=q.readlines()
  print(random.choice(quotes))
def generate_quote():
  quote=random.choice(quotes)
  quote_var.set(quote)
  


root=Tk()
root.title("Quote Generator")
root.geometry("500x500")
root.minsize(400,400)
root.configure(background="light green")
top_label=Label(root,text="“QUOTE OF THE DAY”",font=("Helvetica",20),bg="light green")
top_label.pack(pady=20)
quote_var=StringVar()
quote_label=Label(root,text=", ,",font=("Helvetica",12),bg="light pink",wraplength=500,textvariable=quote_var).pack(pady=30,)

quote_btn=Button(root,text="Generate quote",font=("Helvetica",12),bg="pink",,command=generate_quote).pack(pady=20)



root.mainloop()
           


