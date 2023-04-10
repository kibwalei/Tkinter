import tkinter as tk
from tkinter import *
import pandas as pd
name_list=[]
id_list=[]

def entry_func():
    name_list.append(name_entry)
    id_list.append(id_no_entry)
def new_Window_func():
    new_Window= Tk()
    new_Window.title("My New Window")
    new_Window.geometry("200x100")
    label_one = Label(new_Window , text= "Details Updated Sucessfully")
    label_one.pack()
    return_button= tk.Button(new_Window, text="Return" , fg="black", bg= "gray", command= new_Window.destroy )
    return_button.pack()
    new_Window.mainloop()
    
def add_member():
    
    def apply_button ():
        Label(my_Window, text= "Apllied succesfully!",bg = "gray" , fg= "black").grid(row=7, column=1)
    my_Window= Tk()

    my_Window.title("ADD")
    my_Window.geometry("450x450")
    name=Label(my_Window, bd=10 ,fg= "black" ,text="Enter Name")
    id_no= Label(my_Window, bd=10 ,fg= "black" ,text="Enter ID_NO:")
    name.grid(row=0, column=0)
    id_no.grid(row=1, column=0)

    #Menu
    mb = Menubutton ( my_Window, text = "...")
    mb.menu = Menu ( mb, tearoff = 0 )
    mb["menu"] = mb.menu
    mb.menu.add_checkbutton ( label ='Contact')
    mb.menu.add_checkbutton ( label = 'About' )
    mb.place(x=430,y=0)

    #Entry of name and ID NO.
    name_entry= Entry(my_Window)
    id_no_entry =Entry(my_Window)
    name_entry.grid(row=0 , column=1)
    id_no_entry.grid(row=1 ,column=1)
    #Gender
    gender_label= Label(my_Window,text="Gender:").grid(row=2,column=0)
    male_check =Checkbutton(my_Window,text="Male").grid(row=2,column= 1 ) #sticky E -> sticks the check button to East side
    female_check =Checkbutton(my_Window, text="Female").grid(row=2, column=2 ,sticky=W)

    #listBox
    Lb =tk.Listbox(my_Window)
    Lb.insert(1,"Married")
    Lb.insert(2,'Single')
    Lb.insert(3,'Divorced')
    Lb.insert(4,'Rather not say')
    m_status=Label(my_Window,text="Marital Status" , fg="black", font="Calibri")
    m_status.place(x=300 ,y=0)
    Lb.place(x=300,y=30)
    
    #Buttons
    button1= tk.Button(my_Window ,fg="black" , bg="white" , text="Cancel" , command=my_Window.destroy)
    button2= tk.Button(my_Window ,fg="black" , bg="white" , text="OK",command=new_Window_func )
    button3= tk.Button(my_Window,text= "Apply" , bg= "white" , fg= "black", command=apply_button)
    button1.grid(row=5 , column=0)
    button2.grid(row=5 ,column=2)
    button3.grid(row=5 ,column=1)
    my_Window.mainloop()
    
def remove_member():
    remove_Window= Tk()
    
    remove_Window.title("Removing")
    remove_Window.geometry("450x450")
    name=Label(remove_Window, bd=10 ,fg= "black" ,text="Enter Name")
    id_no= Label(remove_Window, bd=10 ,fg= "black" ,text="Enter ID_NO:")
    name.grid(row=0, column=0)
    id_no.grid(row=1, column=0)
    
    #Entry of name and ID NO.
    name_entry= Entry(remove_Window)
    id_no_entry =Entry(remove_Window)
    name_entry.grid(row=0 , column=1)
    id_no_entry.grid(row=1 ,column=1)

    gender_label= Label(remove_Window,text="Gender:").grid(row=2,column=0)
    male_check =Checkbutton(remove_Window,text="Male").grid(row=2,column= 1 ) #sticky E -> sticks the check button to East side
    female_check =Checkbutton(remove_Window, text="Female").grid(row=2, column=2 ,sticky=W)

    #Buttons
    button1= tk.Button(remove_Window ,fg="black" , bg="white" , text="Cancel" , command=remove_Window.destroy)
    button2= tk.Button(remove_Window ,fg="black" , bg="white" , text="Remove")
    button1.grid(row=5 , column=0)
    button2.grid(row=5 ,column=2)
    remove_Window.mainloop()
    
#MAIN WINDOW
main_Window= Tk()
main_Window.title("Main Window")
main_Window.geometry("400x400")
    #Buttons    
add_member_button=tk.Button(main_Window , text= "Add Member" , bg="gray" , fg= "black",font="calibri", command= add_member)
remove_member_button=tk.Button(main_Window , text= "Remove Member" , bg="gray" ,font="calibri", fg= "black", command=remove_member)
exit_button=tk.Button(main_Window , text= "Exit" , bg="gray" ,font="calibri", fg= "black" , command= main_Window.destroy)

add_member_button.place(x=20 , y= 20)
remove_member_button.place(x=20 , y= 80)
exit_button.place(x=20 , y=140)
main_Window.mainloop()