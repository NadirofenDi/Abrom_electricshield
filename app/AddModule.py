import tkinter as tk
import app_helper as ah
from tkinter import ttk


class AddModules(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.items = ah.get_all_items_names()
        self.put_widgets()
        self.info_comb_entry = []
        self.column_1 = 0
        self.column_2 = 0
        self.column_3 = 0
        self.column_4 = 0
        self.column_5 = 0
        self.column_6 = 0
        self.column_7 = 0

    def validate_amount(self, input):
        try:
            x = float(input)
            return True
        except ValueError:
            self.bell()
            return False

    def __str__(self):
        return 'hello'


    def put_widgets(self):
    #     self.one_row = ttk.Label(self, text="1 row", style='Err_Lbl.TLabel')
    #     self.two_row = ttk.Label(self, text="2 row", style='Smpl_Lbl.TLabel')
    #     self.three_row = ttk.Label(self, text="3 row", style='Smpl_Lbl.TLabel')
    #     self.four_row = ttk.Label(self, text="4 row", style='Smpl_Lbl.TLabel')
    #     self.five_row = ttk.Label(self, text="5 row", style='Smpl_Lbl.TLabel')
    #     self.six_row = ttk.Label(self, text="6 row", style='Smpl_Lbl.TLabel')
    #     self.seven_row = ttk.Label(self, text="7 row", style='Smpl_Lbl.TLabel')


        # self.one_btn_add = ttk.Button(self, text="Add module", command=self.one_btn_add)
        # self.two_btn_add = ttk.Button(self, text="Add module", command=self.two_btn_add)
        # self.three_btn_add = ttk.Button(self, text="Add module", command=self.three_btn_add)
        # self.four_btn_add = ttk.Button(self, text="Add module", command=self.four_btn_add)
        # self.five_btn_add = ttk.Button(self, text="Add module", command=self.five_btn_add)
        # self.six_btn_add = ttk.Button(self, text="Add module", command=self.six_btn_add)
        # self.seven_btn_add = ttk.Button(self, text="Add module", command=self.seven_btn_add)

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


        print('sekdmkosdf')
        print(dir(self))
        print('sekdmkosdf')
        # self.info_comb_entry.append(self.one_f_amount)

        self.update_button = ttk.Button(self, text="Update", command=self.master.update_func)
        self.restart_button = ttk.Button(self, text="Restart", command=self.master.restart)

        self.update_button.grid(row=27, column=0, sticky='w')
        self.restart_button.grid(row=29, column=0, sticky='w')

    #     self.one_btn_add.grid(row=2, column=0, sticky='w')
    #     self.two_btn_add.grid(row=4, column=0, sticky='w')
    #     self.three_btn_add.grid(row=8, column=0, sticky='w')
    #     self.four_btn_add.grid(row=10, column=0, sticky='w')
    #     self.five_btn_add.grid(row=13, column=0, sticky='w')
    #     self.six_btn_add.grid(row=16, column=0, sticky='w')
    #     self.seven_btn_add.grid(row=25, column=0, sticky='w')
    #
    #
    #
    #     self.one_row.grid(row=1, column=0, sticky='w')
    #     self.two_row.grid(row=3, column=0, sticky='w')
    #     self.three_row.grid(row=7, column=0, sticky='w')
    #     self.four_row.grid(row=9, column=0, sticky='w')
    #     self.five_row.grid(row=12, column=0, sticky='w')
    #     self.six_row.grid(row=15, column=0, sticky='w')
    #     self.seven_row.grid(row=24, column=0, sticky='w')
    #
    # def list_of_labels(self, floor):
    #     self.list_of_labels = [self.one_row, self.two_row, self.three_row, self.four_row, self.five_row, self.six_row]
    #     return self.list_of_labels[floor - 1]
    #
    #
    # def one_btn_add(self):
    #     self.column_1 += 1
    #     if self.column_1 <= 5:
    #         self.new_Combobox_1 = ttk.Combobox(self, values=self.items['names'])
    #         self.new_f_amount_1 = ttk.Entry(self, justify=tk.RIGHT, validate='key',
    #                                         validatecommand=(self.register(self.validate_amount), '%P'))
    #         self.new_Combobox_1.grid(row=1, column=1 + self.column_1, sticky='e')
    #         self.new_f_amount_1.grid(row=2, column=1 + self.column_1, sticky='e')
    #         self.master.info_comb_entry.append((self.new_Combobox_1, self.new_f_amount_1, 1))
    #
    # def two_btn_add(self):
    #     self.column_2 += 1
    #     if self.column_2 <= 5:
    #         self.new_Combobox_2 = ttk.Combobox(self, values=self.items['names'])
    #         self.new_f_amount_2 = ttk.Entry(self, justify=tk.RIGHT, validate='key',
    #                                         validatecommand=(self.register(self.validate_amount), '%P'))
    #         self.new_Combobox_2.grid(row=3, column=1 + self.column_2, sticky='e')
    #         self.new_f_amount_2.grid(row=4, column=1 + self.column_2, sticky='e')
    #         self.master.info_comb_entry.append((self.new_Combobox_2, self.new_f_amount_2, 2))
    #
    # def three_btn_add(self):
    #     self.column_3 += 1
    #     if self.column_3 <= 5:
    #         self.new_Combobox_3 = ttk.Combobox(self, values=self.items['names'])
    #         self.new_f_amount_3 = ttk.Entry(self, justify=tk.RIGHT, validate='key',
    #                                         validatecommand=(self.register(self.validate_amount), '%P'))
    #         self.new_Combobox_3.grid(row=7, column=1 + self.column_3, sticky='e')
    #         self.new_f_amount_3.grid(row=8, column=1 + self.column_3, sticky='e')
    #         self.master.info_comb_entry.append((self.new_Combobox_3, self.new_f_amount_3, 3))
    #
    # def four_btn_add(self):
    #     self.column_4 += 1
    #     if self.column_4 <= 5:
    #         self.new_Combobox_4 = ttk.Combobox(self, values=self.items['names'])
    #         self.new_f_amount_4 = ttk.Entry(self, justify=tk.RIGHT, validate='key',
    #                                         validatecommand=(self.register(self.validate_amount), '%P'))
    #         self.new_Combobox_4.grid(row=9, column=1 + self.column_4, sticky='e')
    #         self.new_f_amount_4.grid(row=10, column=1 + self.column_4, sticky='e')
    #         self.master.info_comb_entry.append((self.new_Combobox_4, self.new_f_amount_4, 4))
    #
    # def five_btn_add(self):
    #     self.column_5 += 1
    #     if self.column_5 <= 5:
    #         self.new_Combobox_5 = ttk.Combobox(self, values=self.items['names'])
    #         self.new_f_amount_5 = ttk.Entry(self, justify=tk.RIGHT, validate='key',
    #                                         validatecommand=(self.register(self.validate_amount), '%P'))
    #         self.new_Combobox_5.grid(row=12, column=1 + self.column_5, sticky='e')
    #         self.new_f_amount_5.grid(row=13, column=1 + self.column_5, sticky='e')
    #         self.master.info_comb_entry.append((self.new_Combobox_5, self.new_f_amount_5, 5))
    #
    # def six_btn_add(self):
    #     self.column_6 += 1
    #     if self.column_6 <= 5:
    #         self.new_Combobox_6 = ttk.Combobox(self, values=self.items['names'])
    #         self.new_f_amount_6 = ttk.Entry(self, justify=tk.RIGHT, validate='key',
    #                                         validatecommand=(self.register(self.validate_amount), '%P'))
    #         self.new_Combobox_6.grid(row=15, column=1 + self.column_6, sticky='e')
    #         self.new_f_amount_6.grid(row=16, column=1 + self.column_6, sticky='e')
    #         self.master.info_comb_entry.append((self.new_Combobox_6, self.new_f_amount_6, 6))
    #
    # def seven_btn_add(self):
    #     self.column_7 += 1
    #     if self.column_7 <= 5:
    #         self.new_Combobox_7 = ttk.Combobox(self, values=self.items['names'])
    #         self.new_f_amount_7 = ttk.Entry(self, justify=tk.RIGHT, validate='key',
    #                                         validatecommand=(self.register(self.validate_amount), '%P'))
    #         self.new_Combobox_7.grid(row=24, column=1 + self.column_7, sticky='e')
    #         self.new_f_amount_7.grid(row=25, column=1 + self.column_7, sticky='e')
    #         self.master.info_comb_entry.append((self.new_Combobox_7, self.new_f_amount_7, 7))
    #
    #
