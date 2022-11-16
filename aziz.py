import time
from tkinter import *   
from tkinter import messagebox
import webbrowser
from colorama import Fore, init
import os
from getpass import getpass

def pas():
    os.system("color 5")
    os.system("cls")
    password="itachi315"
    j=getpass("[!] enter the password please: \n")
    if not (j==password):
        os.system("cls")
        print(Fore.RED + "incorect password\ntry again")
        time.sleep(1)
        pas()
pas()


init()
os.system("cls")
print(Fore.RED +"create by itachi")
time.sleep(0.7)
print(Fore.GREEN +"welcome to valorant aim bot")

f="https://www.facebook.com/brlxx.315/"
inst="https://www.instagram.com/itachi_315_96/"

def ex():
    os.system("cls")
    os.system("color 7")
    exit()

top = Tk()      
top.title("valorant by itachi")
top.geometry("270x150")




def fun():
    answer = messagebox.askokcancel("VALORANT AIM BOT","ON")
    if answer:
        print("aim bot has startesd")
    
    
def fac():
    webbrowser.open_new(f)
    
def ins():
    webbrowser.open_new(inst)
    

def MORE():
    aa = Tk()
    aa.geometry("400x120")
    bb= aa
    msge = Label(aa, text ='Contact Me', font = "90",fg="red")
    msge.pack()
    b2 = Button(aa,text = "Facebook",command =fac,activebackground = "lightblue",pady=10)
    b3 = Button(aa,text = "Instagram",command =ins,activebackground = "pink",pady=10)
    b5 = Button(aa,text = "Discord: 𝙄𝙏𝘼𝘾𝙃𝙄#0062",activebackground = "blue",pady=10)
    b5.place(x=140,y=50)
    b5.pack
    b2.pack(side = RIGHT)
    b3.pack(side = LEFT)
    bb.mainloop()
    
msg = Label(top, text ='Welcome', font = "90",fg="red") 

b1 = Button(top,text = "VALORANT AIM BOT",command =fun,activebackground = "green",pady=10)

b4 = Button(top, text = "MORE INFO",command=MORE,activeforeground = "yellow",activebackground = "blue",pady = 10)  

b6 = Button(top,text = "EXIT",command =ex,activebackground = "red",pady=10)

msg.pack()

b6.place(x=240,y=120)

b1.pack(side = TOP)  

b4.place(x=0,y=120)

b4.pack  

b6.pack

top.mainloop()  