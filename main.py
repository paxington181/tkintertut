import tkinter as tk
from tkinter import *

m = tk.Tk()

m.title("This is a triumpth")
m_label = Label(m, text = "I'm making a note here")
m_label.pack()



button = tk.Button(m, text = "Huge success", width = 30, command = m.destroy)
button.pack()

entry_window = Toplevel(m)

Label(entry_window, text = "Glad").grid(row = 0)
Label(entry_window, text = "OS").grid(row = 1)
user_entry_1 = Entry(entry_window)
user_entry_2 = Entry(entry_window)
user_entry_1.grid(row = 0, column = 1)
user_entry_2.grid(row = 1, column = 1)



m.mainloop()