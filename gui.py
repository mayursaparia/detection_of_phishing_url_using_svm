#importing libraries
from sklearn.externals import joblib
import inputScript
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Phishing Website")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open(r'C:\Users\Mayur\Desktop\100% Phising Website\Phishing_Website/bg3.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# import pymsgbox as ms
# from pymsgbox import *
from tkinter import messagebox as ms

w = tk.Label(root, text="Enter Url", fg = "white", bg = "black", font = "Helvetica 25 bold ")
w.pack()
w.place(x=600,y=190)
url = tk.Text(root,width=70,height=1,font=("Times New Roman",18,"italic"))
url.place(x=300,y=250)


def BROWSE():
    import webbrowser
    link = url.get('1.0', 'end-1c')
    webbrowser.open(link)


def CHECK():
    link = url.get('1.0', 'end-1c')
    checkprediction = inputScript.main(link)
    # load the pickle file
    classifier = joblib.load('final_models/svm_final1.pkl')

    # checking and predicting

    prediction = classifier.predict(checkprediction)


    print(prediction)
    if prediction == 1:
        yes = tk.Label(root, text="! Web Site Looks Phishing Site, Browse at your OWN RISK !", background="red",
                       foreground="white", font=('times', 18, 'italic'), width=60)
        yes.place(x=300, y=350)
        button2 = tk.Button(root, command=BROWSE, foreground="white", background="black",
                            font=("Times New Roman", 14, "italic"), text="Browse Anyway", width=14, height=1)
        button2.place(x=600, y=400)
    else:
        no = tk.Label(root, text="! Site Seems Safe Site !", background="green", foreground="white",
                      font=('times', 18, ' italic '), width=60)
        no.place(x=300, y=350)
        button2 = tk.Button(root, command=BROWSE, foreground="white", background="black",
                            font=("Times New Roman", 14, "italic"), text="Browse", width=14, height=1)
        button2.place(x=600, y=400)


def Exit():
    root.destroy()


button1 = tk.Button(root, foreground="white", background="black", font=("Times New Roman", 14, "italic"), text="Exit",
                    command=Exit, width=15, height=1)
button1.place(x=600, y=600)

button2 = tk.Button(root, text="Check Site Info", font=('times', 14, ' italic '), foreground="white",
                    background="black", command=CHECK, width=15, height=1)
button2.place(x=600, y=300)


root.mainloop()