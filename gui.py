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

tree = ttk.Treeview(tab1, columns=('id', 'service', 'login', 'password'), show='headings', height=8)
tree.heading('id', text='id')
tree.heading('service', text='service')
tree.heading('login', text='login')
tree.heading('password', text='password')
tree.grid(column=0, row=0)

login_label = ttk.Label(tab2, text="Login")
login_label.grid(column=1, row=1, pady=5, padx=5)

login_entry = ttk.Entry(tab2)
login_entry.grid(column=2, row=1)

password_label = ttk.Label(tab2, text="Password")
password_label.grid(column=1, row=2, pady=5, padx=5)

password_entry = ttk.Entry(tab2)
password_entry.grid(column=2, row=2)

button_sing_in = ttk.Button(tab2, text="Sing In")
button_sing_in.grid(column=0, row=3)
button_sing_in.bind('<Button-1>', on_click_button_sing_in)

button_quit = ttk.Button(tab2, text="Quit")
button_quit.grid(column=1, row=3)
button_quit.bind('<Button-1>', on_click_button_quit)

root.mainloop()
