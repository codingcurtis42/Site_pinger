import os #import os functions for pinging
import subprocess as sp #imports subprocesses as sp
import time #import time functions for the timestamp
import csv #imports functions for csv
from tkinter import *

root = Tk()
root.title("Site Pinger")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Quit", command=root.quit)

root.config(menu=menubar)

Google = Label(root, text="Google", relief = RIDGE, bg="white", width=6, height=2)
TD = Label(root, text="TD", relief = RIDGE, bg="white", width=6, height=2)
Costco = Label(root, text="Costco", relief = RIDGE, bg="white", width=6, height=2)
TestIP = Label(root, text="TestIP", relief = RIDGE, bg="white", width=6, height=2)
Starbucks = Label(root, text="Starbucks", relief = RIDGE, bg="white", width=6, height=2)
BMO = Label(root, text="BMO", relief = RIDGE, bg="white", width=6, height=2)
Ford = Label(root, text="Ford", relief = RIDGE, bg="white", width=6, height=2)
Toyota = Label(root, text="Toyota", relief = RIDGE, bg="white", width=6, height=2)

Google.grid(row=1, column=0)
TD.grid(row=1, column=1)
Costco.grid(row=1, column=2)
TestIP.grid(row=1, column=3)

Starbucks.grid(row=2, column=0)
BMO.grid(row=2, column=1)
Ford.grid(row=2, column=2)
Toyota.grid(row=2, column=3)

root.update_idletasks()
root.update()

while True:

    #Google
    Google.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 8.8.8.8')
    log = open("{}.csv".format("Google"), "a")
    if status == 0:
        Google.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System Google is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        Google.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System Google is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()

    #TD
    TD.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 23.78.212.225')
    log = open("{}.csv".format("TD"), "a")
    if status == 0:
        TD.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System TD is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        TD.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System TD is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()


    #Costco
    Costco.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 170.167.117.81')
    log = open("{}.csv".format("Costco"), "a")
    if status == 0:
        Costco.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System Costco is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        Costco.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System Costco is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()

    #TestIP
    TestIP.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 1.1.1.1')
    log = open("{}.csv".format("TestIP"), "a")
    if status == 0:
        TestIP.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System TestIP is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        TestIP.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System TestIP is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()

    #Starbucks
    Starbucks.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 104.81.188.243')
    log = open("{}.csv".format("Starbucks"), "a")
    if status == 0:
        Starbucks.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System Starbucks is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        Starbucks.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System Starbucks is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()

    #BMO
    BMO.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 23.14.168.109')
    log = open("{}.csv".format("BMO"), "a")
    if status == 0:
        BMO.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System BMO is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        BMO.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System BMO is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()

    #Ford
    Ford.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 136.1.107.78')
    log = open("{}.csv".format("Ford"), "a")
    if status == 0:
        Ford.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System Ford is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        Ford.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System Ford is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()

    #Toyota
    Toyota.config(bg="blue")
    root.update_idletasks()
    root.update()

    status, result = sp.getstatusoutput('ping -c 2 107.154.75.95')
    log = open("{}.csv".format("Toyota"), "a")
    if status == 0:
        Toyota.config(bg="green")
        log.write(time.strftime("%D %H:%M:%S System Toyota is UP!\n"))
        log.close()
        root.update_idletasks()
        root.update()
    else:
        Toyota.config(bg="red")
        log.write(time.strftime("%D %H:%M:%S System Toyota is Down!\n"))
        log.close()
        root.update_idletasks()
        root.update()


root.mainloop()
