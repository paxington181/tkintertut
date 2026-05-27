import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("Grid Layout Tutorial")
main.geometry('600x400')

label1 = ttk.Label(main, text = "Label 1", background = "red")
label2 = ttk.Label(main, text = "Label 2", background = "blue")
label3 = ttk.Label(main, text = "Label 3", background = "green")
label4 = ttk.Label(main, text = "Label 4", background = "yellow")
button1 = ttk.Button(main, text = "Button 1")
button2 = ttk.Button(main, text = "Button 2")
entry = ttk.Entry(main)

main.columnconfigure((0, 1, 2), weight = 1)
main.columnconfigure(3, weight = 10)
main.rowconfigure(0, weight = 1)
main.rowconfigure(1, weight = 1)
main.rowconfigure(2, weight = 1)
main.rowconfigure(3, weight = 3)

label1.grid(row = 0, column = 0, sticky = "nsew")
label2.grid(row = 1, column = 1, sticky = "nsew")
label3.grid(row = 0, column = 3, sticky = "ew")

main.mainloop()