from tkinter import *
import math


def print_result():
    global entry1,entry2,entry3,entry4
    income = float(entry1.get())
    rate = float(entry2.get())
    tax = (rate/100)*income
    amount = income-tax
    entry3.insert(0,str(tax))
    entry4.insert(0,str(amount))
def clear_all():
    global entry1,entry2,entry3,entry4
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)



root = Tk()
root.title("Tax calculator")
root.config(bg="#808080")

label1 = Label(root,text = "Income",font=("Arial", 18),fg = "white",bg ="#808080")
label1.grid(row=1,column=0)
entry1 = Entry(root,font=("Arial", 18),borderwidth = 10,fg = "white",bg ="#808080",relief="ridge", justify="right")
entry1.grid(row=1,column=1,columnspan= 4,padx= 23,pady=5)

label2 = Label(root,text = "Tax rate",font=("Arial", 18),fg = "white",bg ="#808080")
label2.grid(row=2,column=0)
entry2 = Entry(root,font=("Arial", 18),borderwidth = 10,fg = "white",bg ="#808080",relief="ridge", justify="right")
entry2.grid(row=2,column=1,columnspan= 4,padx= 23,pady=5)

label3 = Label(root,text = "Tax",font=("Arial", 18),fg = "white",bg ="#808080")
label3.grid(row=3,column=0)
entry3 = Entry(root,font=("Arial", 18),borderwidth = 10,fg = "white",bg ="#808080",relief="ridge", justify="right")
entry3.grid(row=3,column=1,columnspan= 4,padx= 23,pady=5)

label4 = Label(root,text = "Amount left",font=("Arial", 18),fg = "white",bg ="#808080")
label4.grid(row=4,column=0)
entry4 = Entry(root,font=("Arial", 18),borderwidth = 10,fg = "white",bg ="#808080",relief="ridge", justify="right")
entry4.grid(row=4,column=1,columnspan= 4,padx= 23,pady=5)

button_submit = Button(root,text="submit",font=("Arial", 17),borderwidth = 10,width=9,fg = "white",bg ="black",relief="ridge",command = print_result)
button_submit.grid(row=5,column=1,pady= 10)
button_clear =Button(root,text="clear",font=("Arial", 17),borderwidth = 10,width=9,fg = "white",bg ="black",relief="ridge",command = clear_all)
button_clear.grid(row=5,column=3,pady= 10)






root.mainloop()