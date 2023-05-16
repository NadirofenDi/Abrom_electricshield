import tkinter as tk
import os
import app_helper as ah
from PIL import ImageTk, Image
import electr_modules
from tkinter import messagebox


class SeeResult(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.items = ah.get_all_items_names()
        self.stick_image()

    def put_modules(self):
        data = ah.read_data()
        bord = Image.open('models/RESULT_TEMPLATE.png')
        x_allowed = 250
        if len(data) == 0:
            image = Image.open("models/RESULT_TEMPLATE.png")
            if os.path.isfile('RESULT.png'):  # проверяем, существует ли файл
                os.remove('RESULT.png')
            image.save('RESULT.png')
            self.master.refresh()
        else:
            for i in range(len(data)):
                function_name = data[i][0]
                module_quantity = int(data[i][1])
                floor = data[i][2]
                if data[i][2] != data[i-1][2]:
                    x_allowed = 250
                if hasattr(electr_modules, function_name):
                    func = getattr(electr_modules, function_name)
                    width, height = func().size
                    for q in range(module_quantity):
                        if x_allowed + width >= 2550:
                            self.bell()
                            messagebox.showwarning("Внимание!", "Невозможно добавить модули - нет места на полке.")
                            break
                        else:
                            if function_name == 'HTS_400_24_LS':
                                bord.paste(func(), (x_allowed, (493 - int((height - 700)/2) + 700 * (floor - 1))),
                                           mask=func())
                                x_allowed += width
                            else:
                                bord.paste(func(), (x_allowed, (493 - int(height/2) + 700 * (floor-1))), mask=func())
                                x_allowed += width
                    if os.path.isfile('RESULT.png'):  # проверяем, существует ли файл
                        os.remove('RESULT.png')  # удаляем файл
                    bord.save('RESULT.png')
            self.master.delete_and_put_frame()

    def stick_image(self):
        image = Image.open("RESULT.png")
        width, height = image.size
        coef = 0.12  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        new_size = (new_width, new_height)
        # Вычисляем новый размер изображения с сохранением пропорций
        image_to_stick = image.resize(new_size, resample=Image.BOX)
        self.image_tk = ImageTk.PhotoImage(image_to_stick)
        self.label = tk.Label(self, image=self.image_tk)
        self.label.grid(row=0, column=0, sticky='w', padx=50, pady=50)





