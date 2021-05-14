from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import webbrowser
#linux only | ^ import loop
root = tk.Tk()
def helloCallBack():
  messagebox.showinfo( "Hello Python", "Hello World")
# ^ makes new window with title hello python, and hello world.
def update():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
def power():
    os.system('sudo shutdown now')
def restart():
    os.system('sudo reboot now')
def learn_more():
    webbrowser.open("https://sites.google.com/view/learn-more-1/home")
B = tk.Button(root, text ="Hello", command = helloCallBack)
updateb = tk.Button(root, text ="Update Linux", command = update)
powerb = tk.Button(root, text = "Toggle Power", command = power)
restartb = tk.Button(root, text = "Restart", command = restart)
learn = tk.Button(root, text = "Learn More", command = learn_more)
def pack():
    B.pack()
    updateb.pack()
    powerb.pack()
    restartb.pack()
    learn.pack()
pack()
root.mainloop()
