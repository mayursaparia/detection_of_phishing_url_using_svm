from tkinter import *
from tkinter import messagebox
import re
import os
import coonection



def data():
    fname = v_fname.get()
    pwd = v_pwd.get()
    ph = v_phoneNo.get()
    id = v_emailId.get()
    gen = v_gender.get()
    coun = v_country.get()

    conn = coonection.connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO registration (fullname,password,phone,email,gender,country) VALUES(%s,%s,%s,%s,%s,%s)',(fname,pwd,ph,id,gen,coun,))
    conn.commit()




#to create main window of our application we use tk class
window = Tk()

#callback function to validate user phone number
def validate_phoneno(user_phoneno):
    if user_phoneno.isdigit():
        return True
    elif user_phoneno == "":
        return True
    else:
        messagebox.showinfo('Information','Only digits are allowed for phoneno')
        return False
#function for validating uder email id
def isValidEmail(user_email):
    if len(user_email)>7:
        if re.match("^.+0(\[?)[a-zA-Z0-9.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$",user_email) !=None:
            return True
        return False
    else:
        messagebox.showinfo('Information','this is not a valid email id')
        return False

#function for validating other input fields
def validateAllFields():
    flag = 0
    if v_fname.get() == "":
        messagebox.showinfo('Information','please enter full name before proceeding')
    elif v_pwd.get() == "":
        messagebox.showinfo('Information','please enter password before proceeding')
    elif v_confirmPwd.get() == "":
        messagebox.showinfo('Information','please confirm passwordbefore proceeding')
    elif v_phoneNo.get() == "":
        messagebox.showinfo('Information','please enter phone number before proceeding')
    elif len(v_phoneNo.get()) != 10:
        messagebox.showinfo('Information','please enter 10 digit phone number before proceeding')
    elif v_emailId.get() == "":
        messagebox.showinfo('Information','please enter email id before proceeding')
    elif v_gender.get() == "":
        messagebox.showinfo('Information','please enter gender before proceeding')
    elif v_country.get() == "" or v_country.get() == "Select your Country":
        messagebox.showinfo('Information','please enter country before proceeding')
    elif v_pwd.get() != v_confirmPwd.get():
        messagebox.showinfo('Information','password doesnt match')
    elif v_phoneNo.get() != "":
        validate_phoneno(v_phoneNo.get())

    data()
    messagebox.showinfo('Information', 'registered successfully')

    callNewScreen()





#function clear all inputs in the feilds
def clearAllFields():
    v_fname.set("")
    v_pwd.set("")
    v_confirmPwd.set("")
    v_phoneNo.set("")
    v_emailId.set("")
    v_gender.set("")
    v_country.set("")

def callNewScreen():
    window.destroy()
    os.system('python Login1.py') #connection to login page

window.title("Welcome to registration Screen")

#window.geometry to set window size
#window.configure to set bacground color
window.geometry('500x500')
window.configure(background = "light blue");


v_fname = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = StringVar()
v_country = StringVar()
    
#label allows to display box where text or images can be entered
  
lb_heading=Label(window,text="Registration Screen", width=20, font=("bold", 20), bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="Fullname", width=20, font=("bold", 10), bg="light blue")
lb_fullname.place(x=80,y=130)
entry_fullname=Entry(window, textvariable = v_fname)
entry_fullname.place(x=240,y=130)

lb_pwd=Label(window,text="Password", width=20, font=("bold", 10), bg="light blue")
lb_pwd.place(x=80,y=170)
entry_pwd=Entry(window, textvariable = v_pwd)
entry_pwd.place(x=240,y=170)

lb_confirm_pwd=Label(window,text="Confirm Password", width=20, font=("bold", 10), bg="light blue")
lb_confirm_pwd.place(x=80,y=210)
entry_confirm_pwd=Entry(window, textvariable = v_confirmPwd)
entry_confirm_pwd.place(x=240,y=210)

lb_phoneno=Label(window,text="Phone no", width=20, font=("bold", 10), bg="light blue")
lb_phoneno.place(x=80,y=250)
entry_phoneno=Entry(window, textvariable = v_phoneNo)
entry_phoneno.place(x=240,y=250)

#function to validate phone number
valid_phoneno = window.register(validate_phoneno) #pass option value to call back function
entry_phoneno.config(validate="key", validatecommand=(validate_phoneno, '%P'))


lb_email=Label(window,text="Email", width=20, font=("bold", 10), bg="light blue")
lb_email.place(x=80,y=290)
entry_email=Entry(window, textvariable = v_emailId)
entry_email.place(x=240,y=290)

lb_gender=Label(window,text="Gender", width=20, font=("bold", 10), bg="light blue")
lb_gender.place(x=80,y=330)
Radiobutton(window, text="Male", bg="light blue", padx=5, variable=v_gender, value="Male").place(x=230,y=330)
Radiobutton(window, text="Female", bg="light blue", padx=20, variable=v_gender, value="Female").place(x=290,y=330)


lb_country=Label(window,text="Country", width=20, font=("bold", 10), bg="light blue")
lb_country.place(x=80,y=370)
entry_country=Entry(window, textvariable = v_country)
entry_country.place(x=240,y=370)
list_country = {'India','China','USA','Germany','UK'};

droplist=OptionMenu(window,v_country, *list_country)
droplist.config(width=16, bg="light blue")
v_country.set('Select your Country')
droplist.place(x=240, y=370)

btn_register = Button(window, text="REGISTER", command = validateAllFields, bg="dark blue", fg = "white", font=("bold",10)).place(x=150,y=450)
btn_clear = Button(window, text="CLEAR", command = clearAllFields, bg="dark blue", fg = "white", font=("bold",10)).place(x=250,y=450)

window.mainloop() #function calls endless loop of the window
