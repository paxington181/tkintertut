import tkinter as tk
from tkinter import *

m = tk.Tk()

m.title("This is a triumpth")
m_label = Label(m, text = "I'm making a note here")
m_label.pack()

button = tk.Button(m, text = "Huge success", width = 30, command = m.destroy)
button.pack()

m.mainloop()