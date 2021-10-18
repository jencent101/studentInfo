from tkinter import *

MyRootDialog=Tk()
#Set Tkinter Size And Location
MyRootDialog.geometry("400x400")

#Set Tkinter Title
MyRootDialog.title("Information")

rt = Toplevel()
rt.title("Information")
rt.geometry("450x450")
rt.iconify()
# Define Function for get Value
def Get_MyInputValue():
    name_ = full_name_entry.get()
    myTKlabel1['text'] = name_
    age_ = age_entry.get()
    myTKlabel2['text'] = age_
    gender_ = gender_entry.get()
    myTKlabel3['text'] = gender_
    bday_ = bday_entry.get()
    myTKlabel4['text'] = bday_
    school_ = school_entry.get()
    myTKlabel5['text'] = school_

    MyRootDialog.iconify()
    rt.deiconify()

def back():
    MyRootDialog.deiconify()
    rt.iconify()

myTKlabel1 = Label(rt, text="Full name ",borderwidth=1, relief="ridge", height=3, width=25)
myTKlabel1.grid(row=0, column=2)
myTKlabel2 = Label(rt, text="Age ",borderwidth=1, relief="ridge", height=3, width=25)
myTKlabel2.grid(row=1, column=2)
myTKlabel3 = Label(rt, text="Gender ",borderwidth=1, relief="ridge", height=3, width=25)
myTKlabel3.grid(row=2, column=2)
myTKlabel4 = Label(rt, text="Birthday ",borderwidth=1, relief="ridge", height=3, width=25)
myTKlabel4.grid(row=3, column=2)
myTKlabel5 = Label(rt, text="School ",borderwidth=1, relief="ridge", height=3, width=25)
myTKlabel5.grid(row=4, column=2)

back_button = Button(rt, text="< back", command=back).grid(row=5, column=0)

# Create Tkinter Entry Widget and Label
lbl_full = Label(MyRootDialog, text="Full name ").grid(row=0, column=0)
full_name_entry = Entry(MyRootDialog, width=17)
full_name_entry.grid(row=0, column=1)

lbl_age = Label(MyRootDialog, text="Age ").grid(row=1, column=0)
age_entry = Entry(MyRootDialog, width=17)
age_entry.grid(row=1, column=1)

lbl_gender = Label(MyRootDialog, text="Gender ").grid(row=2, column=0)
gender_entry = Entry(MyRootDialog, width=17)
gender_entry.grid(row=2, column=1)

lbl_bday = Label(MyRootDialog, text="Birthday ").grid(row=3, column=0)
bday_entry = Entry(MyRootDialog, width=17)
bday_entry.grid(row=3, column=1)

lbl_school = Label(MyRootDialog, text="School ").grid(row=4, column=0)
school_entry = Entry(MyRootDialog, width=17)
school_entry.grid(row=4, column=1)

#command will call the defined function

MyTkButton = Button(MyRootDialog, height=1, width=10, text="Show Info", command= Get_MyInputValue)
MyTkButton.grid(row=5, column=0)

mainloop()