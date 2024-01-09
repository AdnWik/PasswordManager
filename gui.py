import tkinter as tk
from tkinter import ttk


def on_click_button_quit(event):
    root.destroy()

def on_click_button_sing_in(event):
    print(login_entry.get())
    print(password_entry.get())


root = tk.Tk()
# APP TITLE
root.title('Password manager')

# APP SIZE IN PX
root.geometry('800x600')

tabsystem = ttk.Notebook(root)
tab1 = ttk.Frame(tabsystem)
tab2 = ttk.Frame(tabsystem)

tabsystem.add(tab1, text='Show credentials')
tabsystem.add(tab2, text='Add credential')
tabsystem.grid(column=0, row=0,)


#frm = ttk.Frame(root, padding=10)
#frm.grid()
login_label = ttk.Label(tab1, text="Login")
login_label.grid(column=1, row=1, pady=5, padx=5)

login_entry = ttk.Entry(tab1)
login_entry.grid(column=2, row=1)

password_label = ttk.Label(tab1, text="Password")
password_label.grid(column=1, row=2, pady=5, padx=5)

password_entry = ttk.Entry(tab1)
password_entry.grid(column=2, row=2)

button_sing_in = ttk.Button(tab1, text="Sing In")
button_sing_in.grid(column=0, row=3)
button_sing_in.bind('<Button-1>', on_click_button_sing_in)

button_quit = ttk.Button(tab1, text="Quit")
button_quit.grid(column=1, row=3)
button_quit.bind('<Button-1>', on_click_button_quit)

root.mainloop()
