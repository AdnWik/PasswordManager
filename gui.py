import tkinter as tk
from tkinter import ttk


class Credentials:
    def __init__(self, tab) -> None:
        self.tree = ttk.Treeview(
            tab,
            columns=(
                'id',
                'service',
                'login',
                'password'
                ),
            show='headings',
            height=8
        )
        self.configure_tree()

    def configure_tree(self):
        self.tree.heading('id', text='id')
        self.tree.heading('service', text='service')
        self.tree.heading('login', text='login')
        self.tree.heading('password', text='password')
        self.tree.pack()


class Login:
    def __init__(self, tab) -> None:
        self.login_label = ttk.Label(tab, text="Login")
        self.login_entry = ttk.Entry(tab)
        self.password_label = ttk.Label(tab, text="Password")
        self.password_entry = ttk.Entry(tab)
        self.button_sing_in = ttk.Button(tab, text="Sing In")
        self.button_quit = ttk.Button(tab, text="Quit")
        self.configure_tab()

    def configure_tab(self):
        self.login_label.grid(column=1, row=1, pady=5, padx=5)
        self.login_entry.grid(column=2, row=1)
        self.password_label.grid(column=1, row=2, pady=5, padx=5)
        self.password_entry.grid(column=2, row=2)
        self.button_sing_in.grid(column=0, row=3)
        self.button_sing_in.bind('<Button-1>', self.on_click_button_sing_in)
        self.button_quit.grid(column=1, row=3)
        self.button_quit.bind('<Button-1>', self.on_click_button_quit)

    def on_click_button_quit(self, event):
        root.destroy()

    def on_click_button_sing_in(self, event):
        print(self.login_entry.get())
        print(self.password_entry.get())


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
tabsystem.pack()

credentials_tab = Credentials(tab1)
login_tab = Login(tab2)
#frm = ttk.Frame(root, padding=10)
#frm.grid()

root.mainloop()
