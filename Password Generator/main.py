import random
import tkinter
from tkinter import *
from tkinter.scrolledtext import *

lowercase = "abcdefghijklmnopqrstuwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
numbers = "1234567890"
characters = "!@#$%^&*()_+"
mixed = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUwWxXyYzZ"

#user-interface

# width of X

window = tkinter.Tk()
window.title("PASSWORD GENERATOR")
tkinter.Label(window, text = "Choose your password type", fg = "white", bg = "green",anchor=CENTER).pack(fill = "x")

S = tkinter.Scrollbar(window)
T = tkinter.Text(window, height=4, width=140)
S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
T.pack(side=tkinter.RIGHT, fill=tkinter.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

#GUI

# default window width and height 
# textPad = ScrolledText(window, width=100, height=80)

def Weak():
    file = open("H:\Python Projects\Password Generator\data\EightChar.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    password = username
    T.insert(tkinter.END,"Weak - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\Weak.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()

def NotSoWeeak():
    file = open("H:\Python Projects\Password Generator\data\SixChar.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    password = random.choice(uppercase) + username + random.choice(numbers)
    T.insert(tkinter.END,"Can be better - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\NotSoWeak.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()    

def Normal():
    file = open("H:\Python Projects\Password Generator\data\SixChar.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    password =  random.choice(uppercase) + username + random.choice(numbers)                
    T.insert(tkinter.END,"Normal - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\Normal.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()

def Fair():
    file = open("H:\Python Projects\Password Generator\data\FiveChar.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    password = random.choice(uppercase) +  username + random.choice(numbers) + random.choice(characters)
    T.insert(tkinter.END,"Fair - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\Fair.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()

def CanBeStrong():
    file = open("H:\Python Projects\Password Generator\data\FiveChar.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    password = username + random.choice(uppercase) + random.choice(characters) + random.choice(numbers)   
    T.insert(tkinter.END,"Good - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\CanBeStrong.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()

def Strong():
    file = open("H:\Python Projects\Password Generator\data\ThreeChar.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    password = username + random.choice(numbers) + random.choice(lowercase) + random.choice(numbers) + random.choice(characters) + random.choice(mixed)
    T.insert(tkinter.END,"Strong - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\Strong.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()

def YouCant():
    file = open("H:\Python Projects\Password Generator\data\dictionary.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    password = username + random.choice(uppercase) + random.choice(characters) + random.choice(lowercase)   
    T.insert(tkinter.END,"Strong Enough - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\YouCant.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()

def Recommended():
    
    file = open("H:\Python Projects\Password Generator\data\ThreeChar.txt")
    reading = file.read().splitlines()
    username = random.choice(reading)
    file.close()
    password = username  + random.choice(characters) + random.choice(mixed)+ random.choice(lowercase) + random.choice(characters) + random.choice(lowercase)  
    #tkinter.Label(window, anchor=NE,text = "").pack()
    T.insert(tkinter.END,"Unbreakable - " + password + "\n")
    f= open(r"H:\Python Projects\Password Generator\Password Storage\Recommended.txt","a+")
    #password = password.encode('base-64', 'strict')
    f.write(password + "\n")
    f.close()

# Frame and Positioning



btns_frame = Frame(window, width = 800, height = 600, bg = "grey")
btns_frame.pack(side = "left", fill = "y")

button1 = Button(btns_frame, text = "Weak", fg = "black", width = 32, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Weak()).grid(row = 0, column = 0, columnspan = 3, padx = 2, pady = 2)
button2 = Button(btns_frame, text = "Not Weak", fg = "black", width = 32, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: NotSoWeeak()).grid(row = 1, column = 0, columnspan = 3, padx = 2, pady = 2)
button3 = Button(btns_frame, text = "Normal", fg = "black", width = 32, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Normal()).grid(row = 2, column = 0, columnspan = 3, padx = 2, pady = 2)
button4 = Button(btns_frame, text = "Fair", fg = "black", width = 32, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Fair()).grid(row = 3, column = 0, columnspan = 3, padx = 2, pady = 2)
button5 = Button(btns_frame, text = "Can Be Strong", fg = "black", width = 32, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: CanBeStrong()).grid(row = 4, column = 0, columnspan = 3, padx = 2, pady = 2)
button6 = Button(btns_frame, text = "Strong", fg = "black", width = 32, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Strong()).grid(row = 5, column = 0, columnspan = 3, padx = 2, pady = 2)
button7 = Button(btns_frame, text = "You can't even try", fg = "black", width = 32, height = 5, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: YouCant()).grid(row = 6, column = 0, columnspan = 3, padx = 2, pady = 2)
button8 = Button(btns_frame, text = "Recommended", fg = "black", width = 32, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Recommended()).grid(row = 7, column = 0, columnspan = 3, padx = 2, pady = 2)

 

