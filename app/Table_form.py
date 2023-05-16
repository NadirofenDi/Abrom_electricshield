import tkinter as tk
import app_helper as ah
from tkinter import ttk


class TableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        heads = ["module_id", "module_amount", "row_id"]
        table = ttk.Treeview(self, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for row in ah.read_data():
            table.insert('', tk.END, values=row)

        polosa_prokrutki = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=polosa_prokrutki.set)
        polosa_prokrutki.pack(side=tk.RIGHT, fill=tk.Y)

        table.pack(expand=tk.YES, fill=tk.BOTH)
