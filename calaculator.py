from tkinter import *



flag = True

def expand():
    hide_all_widgets(root)
    global e
    e =Entry(root,width= 55,borderwidth=10,fg ="blue")
    e.grid(row=0,column=0,columnspan= 5,padx=12,pady=10)
    
    buttons = [("(",1,0),(")",1,1),("7",2,1),("8",2,2),("9",2,3),("+",2,4),
           ("4",3,1),("5",3,2),("6",3,3),("-",3,4),
           ("3",4,1),("2",4,2),("1",4,3),("*",4,4),
           ("0",5,1),("/",5,4),(".",5,2),("%",5,3)]
    for i,row,col in buttons:
        button = Button(root,text=i,padx= 30,pady=10,command =lambda num = i:button_click(num),bg ="black",fg ="white")
        button.grid(row=row,column=col)
    
    button_clear = Button(root,text= "Clear",padx= 20,pady=10,command = clear_info,fg ="white",bg="black")
    button_equate = Button(root,text= "=",padx= 30,pady=10,command = result,fg ="white",bg="black")
    button_del = Button(root,text= "Del",padx= 25,pady=10,command = del_fun,fg ="white",bg="black")
    button_expand = Button(root,text= "N",padx= 29,pady=10,command = normal_mode,fg ="white",bg="black")

    button_clear.grid(row = 6,column=3)

    button_equate.grid(row= 6,column=4)
    button_del.grid(row=6,column= 2)
    button_expand.grid(row = 6,column= 1)

           
def hide_all_widgets(window):
    for widget in window.winfo_children():
        widget.grid_forget()




root = Tk()
root.title("Calculator")



def button_click(number):
    current_number = e.get()
    e.delete(0,END)
    e.insert(0,str(current_number)+number)

def clear_info():
    e.delete(0,END)


def result():
    try:
        data =  e.get()
        ans = str(eval(data))
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
    e =Entry(root,width= 43,borderwidth=10,fg ="blue")
    e.grid(row=0,column=0,columnspan= 4,padx=12,pady=10)
    
    buttons = [("7",1,0),("8",1,1),("9",1,2),("+",1,3),
           ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
           ("3",3,0),("2",3,1),("1",3,2),("*",3,3),
           ("0",4,0),("/",4,3),(".",4,1),("%",4,2)]
    
    for i,row,col in buttons:
        button = Button(root,text=i,padx= 30,pady=10,command =lambda num = i:button_click(num),bg ="black",fg ="white")
        button.grid(row=row,column=col)

    button_clear = Button(root,text= "Clear",padx= 20,pady=10,command = clear_info,fg ="white",bg="black")
    button_equate = Button(root,text= "=",padx= 30,pady=10,command = result,fg ="white",bg="black")
    button_del = Button(root,text= "Del",padx= 25,pady=10,command = del_fun,fg ="white",bg="black")
    button_expand = Button(root,text= "S",padx= 29,pady=10,command = expand,fg ="white",bg="black")

    button_clear.grid(row = 5,column=2)

    button_equate.grid(row= 5,column=3)
    button_del.grid(row=5,column= 1)
    button_expand.grid(row = 5,column= 0)



normal_mode()



root.mainloop()