import tkinter as tk
from tkinter import ttk
import app_helper as ah
from SeeResult import SeeResult
from AddModule import AddModules
from KlientData import Klientdata


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My App')
        self.style = ttk.Style()
        self.style.configure('Err_Lbl.TLabel', foreground='red', padding=(10, 10, 60, 10))
        self.style.configure('Smpl_Lbl.TLabel', padding=(10, 10, 60, 10))
        self.style.configure('Bld_Lbl.TLabel', font='Helvetica 13 bold', padding=(0, 10, 0, 10))
        self['background'] = '#EBEBEB'
        self.put_frames()
        self.put_menu()

    def refresh(self):
        all_frames = [i for i in self.children]
        for i in all_frames:
            self.nametowidget(i).destroy()
        self.put_frames()
        self.put_menu()

    def update_func(self):
        child1 = AddModules(self)
        self.data = ah.get_data_from(child1.info_comb_entry)
        ah.clear_data()
        ah.insert_data(self.data)
        child2 = SeeResult(self)
        return child2.put_modules()

    def restart(self):
        ah.clear_data()
        child = SeeResult(self)
        return child.put_modules()

    def addmodules_row(self, floor):
        child = AddModules(self)
        row = child.list_of_labels(floor)
        return row

    def put_menu(self):
        self.config(menu=MainMenu(self))

    def put_frames(self):
        self.add_form_frame = AddModules(self)
        self.add_form_frame.grid(row=0, column=0, sticky='nswe')
        self.stat_frame = SeeResult(self)
        self.stat_frame.grid(row=0, column=2, sticky='nswe')
        # self.data_from_site = Klientdata(self)
        # self.data_from_site.grid(row=0, column=1, sticky='nswe')

    def delete_and_put_frame(self):
        self.stat_frame.destroy()  # удаление фрейма
        self.stat_frame = SeeResult(self)
        self.stat_frame.grid(row=0, column=1, sticky='nswe')

    def quit(self):
        self.destroy()

    def show_warning(self):
        self.popup.show('warning')


class MainMenu(tk.Menu):
    def __init__(self, mainwindow):
        super().__init__(mainwindow)

        file_menu = tk.Menu(self)
        options_menu = tk.Menu(self)
        help_menu = tk.Menu(self)

        self.add_cascade(label="File", menu=file_menu)
        self.add_cascade(label="Options", menu=options_menu)
        self.add_cascade(label="Help", menu=help_menu)

        file_menu.add_command(label='Refresh', command=mainwindow.refresh)
        file_menu.add_command(label='Quit', command=mainwindow.quit)

        options_menu.add_cascade(label='Switch language')
        options_menu.add_command(label='Switch theme')
        help_menu.add_command(label='About us')
        help_menu.add_command(label='FAQ')



app = App()
app.mainloop()


attributes = dir(app)
print(attributes)

