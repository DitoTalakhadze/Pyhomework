from tkinter import *
from tkinter import ttk

PI = 3.14

WIDTH = 1024
HEIGHT = 720

print(WIDTH + HEIGHT)

root = Tk()
frm = ttk.Frame(root, padding=10)
root.geometry(f'{WIDTH}x{HEIGHT}')
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
