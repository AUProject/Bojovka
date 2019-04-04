import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#FFAAFF', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="dickpic.png")
        btn_open_dlg = tk.Button(toolbar, text="хуй", command=self.open_dialogue, bg='#FF77FF', bd=0,
                                 compound=tk.TOP, image=self.add_img)
        btn_open_dlg.pack(side=tk.LEFT)
        self.tree = ttk.Treeview(self, columns=('ID', 'name', 'HP', 'attack', 'orders', 'skills'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=50, anchor=tk.CENTER)
        self.tree.column('attack', width=30, anchor=tk.CENTER)
        self.tree.column('orders', width=30, anchor=tk.CENTER)
        self.tree.column('skills', width=40, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('name', text='Имя')
        self.tree.heading('attack', text='плюс к кубу атаки')
        self.tree.heading('orders', text='куб приказов')
        self.tree.heading('skills', text='номера скиллов')

        self.tree.pack()

    def open_dialogue(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Впихнуть имбу")
        self.geometry("400x220+400+300")
        self.resizable(False, False)

        data1 = tk.StringVar()
        label_desc = tk.Label(self, text="Hooey")
        label_desc.place(x=50, y=50)

        label_select = tk.Label(self, text="Yooh")
        label_select.place(x=50, y=80)

        label_smth = tk.Label(self, text="Foo")
        label_smth.place(x=50, y=110)

        self.entry_desc = ttk.Entry(self)
        self.entry_desc.place(x=200, y=50)

        self.entry_hp = ttk.Entry(self)
        self.entry_hp.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=['ID', 'HP'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cncl = ttk.Button(self, text='Close', command=self.destroy)
        btn_cncl.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Add')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()



if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Admeen Ыnterfэйce")
    root.geometry("640x480+300+200")
    root.resizable(False, False)
    root.mainloop()