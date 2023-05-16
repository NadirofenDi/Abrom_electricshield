import tkinter as tk
from tkinter import ttk


class Klientdata(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def validate_amount(self, input):
        try:
            x = float(input)
            return True
        except ValueError:
            self.bell()
            return False

    def put_widgets(self):
        self.one_row = ttk.Label(self, text="Обычные группы освещения", style='Smpl_Lbl.TLabel')
        self.two_row = ttk.Label(self, text="Диммируемые группы освещения", style='Smpl_Lbl.TLabel')
        self.three_row = ttk.Label(self, text="Водяные контуры", style='Smpl_Lbl.TLabel')
        self.four_row = ttk.Label(self, text="Электрические", style='Smpl_Lbl.TLabel')
        self.five_row = ttk.Label(self, text="Электрические теплые полы", style='Smpl_Lbl.TLabel')
        self.six_row = ttk.Label(self, text="Электрические радиаторы", style='Smpl_Lbl.TLabel')
        self.seven_row = ttk.Label(self, text="Кондиционеры", style='Smpl_Lbl.TLabel')
        self.eight_row = ttk.Label(self, text="Модуль защиты от протечки", style='Smpl_Lbl.TLabel')
        self.nine_row = ttk.Label(self, text="wbio-di-wd-14", style='Smpl_Lbl.TLabel')
        self.ten_row = ttk.Label(self, text="клеммы RS485", style='Smpl_Lbl.TLabel')

        self.one_row.grid(row=1, column=0, sticky='w')
        self.two_row.grid(row=3, column=0, sticky='w')
        self.three_row.grid(row=7, column=0, sticky='w')
        self.four_row.grid(row=9, column=0, sticky='w')
        self.five_row.grid(row=12, column=0, sticky='w')
        self.six_row.grid(row=15, column=0, sticky='w')
        self.seven_row.grid(row=17, column=0, sticky='w')
        self.eight_row.grid(row=19, column=0, sticky='w')
        self.nine_row.grid(row=21, column=0, sticky='w')
        self.ten_row.grid(row=23, column=0, sticky='w')

        self.one_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                        validatecommand=(self.register(self.validate_amount), '%P'))
        self.two_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.three_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.four_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.five_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.six_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.seven_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.eight_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.nine_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))
        self.ten_f_amount = ttk.Entry(self, justify=tk.RIGHT, validate='key',
                                      validatecommand=(self.register(self.validate_amount), '%P'))


        self.one_f_amount.grid(row=1, column=1, sticky='e')
        self.two_f_amount.grid(row=3, column=1, sticky='w')
        self.three_f_amount.grid(row=7, column=1, sticky='w')
        self.four_f_amount.grid(row=9, column=1, sticky='w')
        self.five_f_amount.grid(row=12, column=1, sticky='w')
        self.six_f_amount.grid(row=15, column=1, sticky='w')
        self.seven_f_amount.grid(row=17, column=1, sticky='w')
        self.eight_f_amount.grid(row=19, column=1, sticky='w')
        self.nine_f_amount.grid(row=21, column=1, sticky='w')
        self.ten_f_amount.grid(row=23, column=1, sticky='w')

        # self.master.info_comb_entry.append((self.one_f_amount, 1))



