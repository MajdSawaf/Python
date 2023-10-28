import tkinter as tk
from tkinter import *
###Testing the below import to see if it works
###Clicking a button
###It turn out the below import works just fine!
from tkinter import messagebox
from tkinter import scrolledtext
import webbrowser
#from datetime import datetime
#import datetime as dt
#from datetime import timedelta, tzinfo, timezone
#from PIL import ImageTk, Image

ST = Tk()
ST.title("Sawaf Security Tool")
ST.geometry("700x500")
ST.configure(bg="Light Blue")

Label(ST, text = "Sawaf Security Tool", height = 2, width = 60, font = 'Consolas 10').pack()


#####
#Need more work on the below text!
#ST = Label(ST, width=50, height=50, text="Hello World")

button1 = tk.Button(ST, text = "Home", height = 1, width = 7)
button1.place(x=10, y=70)

button2 = tk.Button(ST, text = "Scan", height = 1, width = 7)
button2.place(x=10, y=100)

button3 = tk.Button(ST, text = "Backup", height = 1, width = 7)
button3.place(x=10, y=130)

button4 = tk.Button(ST, text = "Next", height = 1, width = 7)
button4.place(x=10, y=160)

button5 = tk.Button(ST, text = "Previous", height = 1, width = 7)
button5.place(x=10, y=190)

#button6 = tk.Button(ST, text = "C Drive", height = 1, width = 7)
#button6.place(x=10, y=200)

#def image(self):
#    img = ImageTk.Photoimage(Image.open("python.jpg"))
#    button7 = tk.Button(ST, text = "Image", image = PhotoImage, compound = LEFT).pack(side=TOP)

#THIS NEEDS MORE WORK!
#CLICK ON BUTTON TO OPEN C DRIVE
#def hello():
#        file=filedialog.askopenfilename(initialdir="C:/")
#        f=open(win.file, 'r')

#b1n_c = tk.Button(ST, text = "C1 Drive", command = open(C:\))
#b1n_c.place(x=80, y=200)

#def C_Drive():
#    btn_c = Button(ST, text = "C Drive", command = open(C:\))

#button_explore = Button(ST,
#                        text = "browseFiles",
#                        command = browseFiles)

def ButtonClick(self):
    messagebox.askyesnocancel(title="Congratulations!", message="Yay!")

class tkinter():

    def popup_msg():
        messagebox.askquestion(title="Alert!", message="Do you wish to continue?")
        messagebox.showwarning(title="Alert!", message="Are you sure?")
        messagebox.showerror(title="Alert!", message="You are now infected!!")

    Button(ST, text = "Click Here!", command=popup_msg).pack(pady=50)   

    def up_msg():
        messagebox.showwarning(title="Warning!", message="Warning, you have a virus!")

    Button(ST, width=30, height=2, text= "I'm Molly!", command=up_msg).pack(expand=1)

    def ask_msg():
        messagebox.askyesnocancel(title="Please choose!", message="Do you wish to proceed?")

    Button(ST, width=15, height=2, text= "Try this!", command=ask_msg).pack(expand=1)

###Testing these as from what I've learned from another prac
#a = tkinter
#a.popup_msg()
#a.up_msg()
#a.ask_msg()

#def popup_alert():
#    messagebox.showinfo("Alert", "This is malicious!")

#Button(ST, text = "Click Now!", command=popup_alert).pack(pady=5)

#btn1.place(x = 50, y = 5)
#btn2 = Button(text = "Awesome!", bg = "light green")

#This one did not work for some reason
#ST = label(ST, text="Hello World", width=20)

#This did not work!
#ST.Label(ST, Text = "Hello World", column = 5, row = 5)

#This did not work
#ST.label(ST. text = "Hello World").grid(column=0, row=0)

#The below configuration is paused to test different things
#Testing different ways to adjust Label

#But this one worked


btn1 = Button(height = 1, width = 10, text = "Hi", bg = "light yellow")
###
#This was testing to place the button around. I like the below configuration...
#better
#btn1.pack(side = LEFT, padx = 15, pady = 20)
###
#btn1.place(x = 50, y = 5)
#btn2 = Button(text = "Awesome!", bg = "light green")
#btn2.pack()

btn3 = Button(text = "Click Me!", bg = "light pink")
btn3.pack()
#The two prints to make spaces did not work!
#print()
#print()
btn4 = Button(text = "Next", bg = "orange")
btn4.pack()
#ST.Button(top, left, text="Hi")
#ST.pack()

def close():
    ST.quit()

Button(ST, text = "Exit", height = 2, width = 7, command = ST.destroy).pack(side=RIGHT)

def link():
    webbrowser.open_new("https://www.sawaf.com.au")

btn10 = tk.Button(ST, text="Contact Us", height = 1, width = 9, command = link)
btn10.place(x=10, y=450)

ST.mainloop()
