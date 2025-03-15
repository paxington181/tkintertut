import tkinter as tk
from tkinter import *

m = tk.Tk()

m.title("This is a triumpth")
m_label = Label(m, text = "I'm making a note here")
m_label.pack()



button = tk.Button(m, text = "Huge success", width = 30, command = m.destroy)
button.pack()

entry_window = Toplevel(m)
entry_window.title("Grid organized instead of pack")

Label(entry_window, text = "Glad").grid(row = 0)
Label(entry_window, text = "OS").grid(row = 1)
user_entry_1 = Entry(entry_window)
user_entry_2 = Entry(entry_window)
user_entry_1.grid(row = 0, column = 1)
user_entry_2.grid(row = 1, column = 1)

check_butt_1 = IntVar()
Checkbutton(entry_window, text = "Pistachio", variable = check_butt_1).grid(row = 3, sticky = W) 
check_butt_2 = IntVar()
Checkbutton(entry_window, text = "Peanut", variable = check_butt_2).grid(row = 4,sticky = W)

# https://www.geeksforgeeks.org/python-gui-tkinter/ - at Radio Button lesson


m.mainloop()