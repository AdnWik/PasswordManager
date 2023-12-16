import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root_frm = ttk.Frame(root, padding=10)
root_frm.grid()
ttk.Label(root_frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(root_frm, text="Quit", command=root.destroy).grid(column=1, row=0)

testForm = tk.Tk()
test_frm = ttk.Frame(root, padding=10)
test_frm.grid()
ttk.Label(test_frm, text="TEST").grid(column=0, row=0)
ttk.Button(test_frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()