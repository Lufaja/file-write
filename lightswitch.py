import tkinter as tk
from tkinter import ttk
import datetime


window = tk.Tk()
event = 0
state = 0
# schijf hier tussen je code

def log(state):
    if state == 0:
        state = "on"
    else:
        state = "off"
    with open("actions.log", "a") as file:
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        file.write(f"{now} ) lights {state}\n")
    return


def button_pressed(event):
    global state, button
    if state == 0:
        log(state)
        button.config(text= 'Switch lights off')
        window.config(bg="yellow")
        state = 1
    else:
        log(state)
        button.config(text = 'Switch lights on')
        window.config(bg="black")
        state = 0

def txtChange():
    global button
    if button == "Switch lights on":
        button.config(text= "Switch lights off")
    else:
        button.config(text= "Switch lights on")

button = tk.Button(text='Lights off', bg="white", fg="black")
button.pack(pady = 20, padx = 20)
button.bind('<Button>', button_pressed)

button.focus()
button.pack(expand=True)
txtChange()
button_pressed(event)
# schijf hier tussen je code

window.mainloop()