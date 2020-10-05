from tkinter import*
from tkinter import messagebox
import re
import os
import coonection
conn = coonection.connect()
cursor = conn.cursor()


sql = "select email, password from registration"
cursor.execute(sql)
results = cursor.fetchall()


def callNewScreen():
    window.destroy()
    os.system('python gui.py') #connection to gui page



def validateUser(user_fname, user_pwd):

    for row in results:
        email = row[0]
        pwd = row[1]
        if user_fname == email and user_pwd == pwd:
            return True
    return False



#function to validate user inputs

def validateAllFields():
    if v_fname.get() == "":
        messagebox.showinfo('Information', 'Please enter fullname before proceeding')
    elif v_pwd.get() == "":
        messagebox.showinfo('Information','Please enter password before proceeding')
    else:
        status = validateUser(v_fname.get(), v_pwd.get())
        if(status):
            callNewScreen()
        else:
            messagebox.showinfo('Information', 'Invalid Credentials')

#messagebox.showinfo('Information', 'Congratulations, Login sucess')
def clearAllFields():
    v_fname.set("")
    v_pwd.set("")



window = Tk()
window.title("Welcome to Login Screen")


window.geometry('500x500')
window.configure(background = "light blue");

v_fname = StringVar()
v_pwd = StringVar()

lb_heading=Label(window,text="Login Screen", width=20, font=("bold",20), bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="Email Id", width=20, font=("bold",10), bg="light blue")
lb_fullname.place(x=90,y=130)

entry_fullname=Entry(window, textvariable = v_fname)
entry_fullname.place(x=240,y=130)

lb_pwd=Label(window,text="Password", width=20, font=("bold",10), bg="light blue")
lb_pwd.place(x=90,y=170)

entry_pwd=Entry(window, textvariable = v_pwd)
entry_pwd.place(x=240,y=170)


btn_login = Button(window, text="Login", command = validateAllFields, bg="dark blue", fg="white", font=("bold",10)).place(x=120,y=210)
btn_clear = Button(window,text="Clear", command = clearAllFields, bg="dark blue", fg="white", font=("bold",10)).place(x=200,y=210)
btn_newuser = Button(window,text="New User", command = callNewScreen, bg="dark blue", fg="white", font=("bold",10)).place(x=280,y=210)

window.mainloop()

conn.commit()