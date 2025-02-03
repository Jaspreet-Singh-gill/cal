from tkinter import *

number = 0
root = Tk()
root.title("Calculator")
e =Entry(root,width= 35,borderwidth=10,fg ="blue")

e.grid(row=0,column=0,columnspan= 3,padx=10,pady=10)

def button_click(number):
    current_number = e.get()
    e.delete(0,END)
    e.insert(0,str(current_number)+str(number))

def clear_info():
    e.delete(0,END)
    global number
    number = 0


def button_add():
    global number
    global math 
    math = "add"
    first_number = float(e.get())
    number += first_number
    e.delete(0,END)

def result():
    global number
    global math
    if(math == "add"):
        number += float(e.get())
    elif(math == "multiply"):
        number *= float(e.get())
    elif(math == "substract"):
        number -= float(e.get())
    elif(math == "divide"):
        number /= float(e.get())
    e.delete(0,END)
    e.insert(0,number)
    number = 0

def multiply():
    global number
    global math 
    math = "multiply"
    
    first_number =float(e.get())
    number += first_number
    e.delete(0,END)

def substraction():
    global number
    global math 
    math = "substract"
    first_number = float(e.get())
    number += first_number
    e.delete(0,END)

def division():
    global number
    global math 
    math = "divide"
    
    first_number = float(e.get())
    
    number += first_number
    e.delete(0,END)
def add_point():
    num = e.get()
    e.delete(0,END)
    e.insert(0,str(num)+".")


button_1 = Button(root,text="1",padx= 30,pady=10,command =lambda:button_click(1),bg ="black",fg ="white")
button_2 = Button(root,text="2",padx= 30,pady=10,command = lambda:button_click(2),bg ="black",fg ="white")
button_3 = Button(root,text="3",padx= 30,pady=10,command = lambda:button_click(3),bg ="black",fg ="white")
button_4 = Button(root,text="4",padx= 30,pady=10,command =lambda:button_click(4),bg ="black",fg ="white")
button_5 = Button(root,text="5",padx= 30,pady=10,command = lambda:button_click(5),bg ="black",fg ="white")
button_6 = Button(root,text="6",padx= 30,pady=10,command = lambda:button_click(6),bg ="black",fg ="white")
button_7 = Button(root,text="7",padx= 30,pady=10,command = lambda:button_click(7),bg ="black",fg ="white")
button_8 = Button(root,text="8",padx= 30,pady=10,command = lambda:button_click(8),bg ="black",fg ="white")
button_9 = Button(root,text="9",padx= 30,pady=10,command = lambda:button_click(9),bg ="black",fg ="white")
button_0 = Button(root,text="0",padx= 30,pady=10,command = lambda:button_click(0),bg ="black",fg ="white")

button_1.grid(row =3,column=0)
button_2.grid(row =3,column=1)
button_3.grid(row =3,column=2)
button_4.grid(row =2,column=0)
button_5.grid(row =2,column=1)
button_6.grid(row =2,column=2)
button_7.grid(row =1,column=0)
button_8.grid(row =1,column=1)
button_9.grid(row =1,column=2)
button_0.grid(row =4,column=0)
button_point = Button(root,text =".",padx= 31,pady= 10,command=add_point,fg ="white",bg="black")


button_add = Button(root,text ="+",padx= 28,pady=10,command= button_add,fg ="white",bg="black")
button_clear = Button(root,text= "Clear",padx= 20,pady=10,command = clear_info,fg ="white",bg="black")
button_equate = Button(root,text= "=",padx= 71,pady=10,command = result,fg ="white",bg="black")
button_multiply = Button(root,text="*",padx = 30,pady = 10,command = multiply,fg ="white",bg="black")
button_substract = Button(root,text="-",padx = 30,pady = 10,command = substraction,fg ="white",bg="black")
button_division = Button(root,text="/",padx = 30,pady = 10,command = division,fg ="white",bg="black")
button_multiply.grid(row=6,column=0)
button_substract.grid(row=6,column=1)
button_division.grid(row=6,column=2)
button_clear.grid(row = 4,column=2,columnspan=1)
button_point.grid(row = 4,column=1)
button_add.grid(row = 5,column=0)
button_equate.grid(row= 5,column=1,columnspan=2)



root.mainloop()