import tkinter as tk
from tkinter import *
from tkinter import ttk

m = tk.Tk()

m.title("This is a triumpth")
m_label = Label(m, text = "I'm making a note here")
m_label.pack()

menu = Menu(m)
m.config(menu = menu)
filemenu = Menu(m)
menu.add_cascade(label = "Files", menu = filemenu)
filemenu.add_command(label = "New")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = m.quit)
helpmenu = Menu(m)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "You're on your own")


button = tk.Button(m, text = "Huge success", width = 30, command = m.destroy)
button.pack()


portal = IntVar()
portal_2 = IntVar()
Radiobutton(m, text = "Red portal", variable = portal, value = 1).pack(anchor = W)
Radiobutton(m, text = "Blue portal", variable = portal, value = 2).pack(anchor=W)
Radiobutton(m, text = "Green portal", variable = portal_2, value = 3).pack(anchor = W)
Radiobutton(m, text = "Yellow portal", variable = portal_2, value = 4).pack(anchor = W)


Lb = Listbox(m)
for i in range(0, 10):
    Lb.insert(i, f"Index {i}, list item {i + 1}")
#Lb.insert(0, "Index 0")
#Lb.insert(1, "Index 1")
#Lb.insert(2, "Index 2")
#Lb.insert(3, "Index 3")
#Lb.insert(4, "Index 4")
#Lb.insert(5, "Index 5")
Lb.pack(side = LEFT)


scrollbar = Scrollbar(m)
scrollbar.pack(side = RIGHT, fill = Y)
mylist = Listbox(m, yscrollcommand = scrollbar.set)

for line in range(70):
    if line == 69:
        mylist.insert(END, "Nice")
    else:
        mylist.insert(END, "Line" + str(line))

mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)


#Everything underneath this is for grid, everything above is pack organizing.
#They cannot be mixed in the same frame


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

# https://www.geeksforgeeks.org/python-gui-tkinter/ - 

m.mainloop()