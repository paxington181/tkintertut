import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("Grid Layout Tutorial")
window.geometry('600x400')

label1 = ttk.Label(main, text = "Label 1", background = "red")
label2 = ttk.Label(main, text = "Label 2", background = "blue")
label3 = ttk.Label(main, text = "Label 3", background = "green")
label4 = ttk.Label(main, text = "Label 4", background = "yellow")
button1 = ttk.Button(main, text = "Button 1")
button2 = ttk.Button(main, text = "Button 2")
entry = ttk.Entry(window)

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(0, weight = 1)

main.mainloop()