from tkinter import *
import math

allowed_functions = {
    "ln": math.log,         # Natural log (base e)
    "log2": math.log2,      # Log base 2
    "log10": math.log10,    # Log base 10
    "logx": lambda x, b: math.log(x, b),  "sqrt":math.sqrt, "exp": math.exp,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "sec": lambda x: 1 / math.cos(x),
    "cosec": lambda x: 1 / math.sin(x),
    "cot": lambda x: 1 / math.tan(x),
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "π": math.pi, "e": math.e,"pow":lambda x,y:math.pow(x,y)
}




def distroy_log():
    global log_func
    for i in log_func:
        i.grid_forget()
        

def create_log():
    global log_func
    log_func =[]
    buttons = (("ln(",2,3),("log2(",2,4),("log10(",3,3),("logx(",3,4))
    for i,row,col in buttons:
        button = Button(root,text=i,font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command =lambda num = i:button_click(num),bg ="black",fg ="white")
        button.grid(row=row,column=col)
        log_func.append(button)
    button_trigno = Button(root,text= "Log",font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command = distroy_log,fg ="white",bg="black")
    button_trigno.grid(row=1,column=4)
    log_func.append(button_trigno)
def distroy_inv():
    global inv_func
    for i in inv_func:
        i.grid_forget()


def create_inv():
    global inv_func
    inv_func =[]
    buttons = (("asin(",2,2),("acos(",2,3),("atan(",2,4))
    for i,row,col in buttons:
        button = Button(root,text=i,font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command =lambda num = i:button_click(num),bg ="black",fg ="white")
        button.grid(row=row,column=col)
        inv_func.append(button)
    button_trigno = Button(root,text= "Inv",font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command = distroy_inv,fg ="white",bg="black")
    button_trigno.grid(row=1,column=3)
    inv_func.append(button_trigno)


def distroy_trigno():
    global trig_func
    for i in trig_func:
        i.grid_forget()


def create_trigno():
    global trig_func
    trig_func =[]
    buttons = (("sin(",2,2),("cos(",2,3),("tan(",2,4),
           ("sec(",3,2),("cosec(",3,3),("cot(",3,4))
    for i,row,col in buttons:
        button = Button(root,text=i, font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command =lambda num = i:button_click(num),bg ="black",fg ="white")
        button.grid(row=row,column=col)
        trig_func.append(button)
    button_trigno = Button(root,text= "Trigno", font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command = distroy_trigno,fg ="white",bg="black")
    button_trigno.grid(row=1,column=2)
    trig_func.append(button_trigno)

def expand():

    hide_all_widgets(root)
    global e
    e =Entry(root,font=("Arial", 20),borderwidth=10,fg ="white",bg="black",relief="ridge", justify="right")
    e.grid(row=0,column=0,columnspan= 5,ipadx=8, ipady=10, padx=2, pady=5)
    
    buttons = [("(",1,0),(")",1,1),("7",2,1),("8",2,2),("9",2,3),("+",2,4),
           ("4",3,1),("5",3,2),("6",3,3),("-",3,4),
           ("3",4,1),("2",4,2),("1",4,3),("*",4,4),
           ("0",5,1),("/",5,4),(".",5,2),("%",5,3),
           ("π",2,0),("e",3,0),(",",4,0),("pow(",5,0),("sqrt(",6,0)]
    for i,row,col in buttons:
        button = Button(root,text=i,font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command =lambda num = i:button_click(num),bg ="black",fg ="white")
        button.grid(row=row,column=col)
    
    button_clear = Button(root,text= "Clear",font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command = clear_info,fg ="white",bg="black")
    button_equate = Button(root,text= "=",font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command = result,fg ="white",bg="black")
    button_del = Button(root,text= "Del",font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command = del_fun,fg ="white",bg="black")
    button_expand = Button(root,text= "⥯",font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command = normal_mode,fg ="white",bg="black")
    button_trigno = Button(root,text= "Trigno",font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command = create_trigno,fg ="white",bg="black")
    button_inverse =Button(root,text= "Inv",font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command = create_inv,fg ="white",bg="black")
    button_log =Button(root,text= "log",font=("Arial", 14),relief="ridge", borderwidth=3,width=6, height=2,command = create_log,fg ="white",bg="black")
    button_clear.grid(row = 6,column=3)
    button_trigno.grid(row=1,column=2)
    button_inverse.grid(row=1,column=3)
    button_log.grid(row=1,column=4)

    button_equate.grid(row= 6,column=4)
    button_del.grid(row=6,column= 2)
    button_expand.grid(row = 6,column= 1)

           
def hide_all_widgets(window):
    for widget in window.winfo_children():
        widget.grid_forget()




root = Tk()
root.title("Calculator")
root.configure(bg="#808080")



def button_click(number):
    current_number = e.get()
    e.delete(0,END)
    e.insert(0,str(current_number)+number)

def clear_info():
    e.delete(0,END)

def safe_eval(expression):
    try:
        return eval(expression, {"__builtins__": None}, allowed_functions)
    except Exception:
        return "ERROR"

def result():
    try:
        data =  e.get()
        ans = str(safe_eval(data))
        e.delete(0,END)
        e.insert(0,ans)
    except: 
        e.delete(0,END)
        
        e.insert(0,"ERROR")


def del_fun():
    number  = e.get()
    e.delete(0,END)
    e.insert(0,number[:-1])

def normal_mode():
    
    hide_all_widgets(root)
    global e
    e =Entry(root,borderwidth=10,font=("Arial", 20),fg ="white",bg="black",relief="ridge", justify="right")
    e.grid(row=0,column=0,columnspan= 4)
    
    buttons = [("7",1,0),("8",1,1),("9",1,2),("+",1,3),
           ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
           ("3",3,0),("2",3,1),("1",3,2),("*",3,3),
           ("0",4,0),("/",4,3),(".",4,1),("%",4,2)]
    
    for i,row,col in buttons:
        button = Button(root,text=i,font=("Arial", 14), bg="black", fg="white",
                       relief="ridge", borderwidth=3, width=6, height=2,command =lambda num = i:button_click(num))
        button.grid(row=row,column=col)

    button_clear = Button(root,text= "Clear",font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command = clear_info,fg ="white",bg="black")
    button_equate = Button(root,text= "=",font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command = result,fg ="white",bg="black")
    button_del = Button(root,text= "Del",font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command = del_fun,fg ="white",bg="black")
    button_expand = Button(root,text= "⥯",font=("Arial", 14),relief="ridge", borderwidth=3, width=6, height=2,command = expand,fg ="white",bg="black")
    

    button_clear.grid(row = 5,column=2)

    button_equate.grid(row= 5,column=3)
    button_del.grid(row=5,column= 1)
    button_expand.grid(row = 5,column= 0)



normal_mode()



root.mainloop()