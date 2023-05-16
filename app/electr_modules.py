from PIL import ImageTk, Image


def background():
    image = Image.new('RGB', (2800, 5200), color='white')
    border = Image.open("models/borders.png")
    image.paste(border, (0, 0), mask=border)
    return image.save("models/RESULT_TEMPLATE.png")


def klemma_yellow():
    with Image.open("models/0.png") as klemma_yellow:
        width, height = klemma_yellow.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        klemma_yellow = klemma_yellow.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        klemma_yellow.save('models_named/klemma_yellow.png')

        return klemma_yellow


def WB_MR6C_v2():
    with Image.open("models/1.png") as WB_MR6C_v2:
        width, height = WB_MR6C_v2.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        WB_MR6C_v2 = WB_MR6C_v2.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        WB_MR6C_v2.save('models_named/WB_MR6C_v2.png')

        return WB_MR6C_v2


def WB_MRGBW_D():
    with Image.open("models/2.png") as WB_MRGBW_D:
        width, height = WB_MRGBW_D.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        WB_MRGBW_D = WB_MRGBW_D.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        WB_MRGBW_D.save('models_named/WB_MRGBW_D.png')

        return WB_MRGBW_D


def HTS_400_24_LS():
    with Image.open("models/3.png") as HTS_400_24_LS:
        width, height = HTS_400_24_LS.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        HTS_400_24_LS = HTS_400_24_LS.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        HTS_400_24_LS.save('models_named/HTS_400_24_LS.png')

        return HTS_400_24_LS


def klemma_6_wb_mr6c():
    with Image.open("models/4.png") as klemma_6_wb_mr6c:
        width, height = klemma_6_wb_mr6c.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        klemma_6_wb_mr6c = klemma_6_wb_mr6c.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        klemma_6_wb_mr6c.save('models_named/klemma_6_wb_mr6c.png')

        return klemma_6_wb_mr6c


def klemma_4_wb_led():
    with Image.open("models/5.png") as klemma_4_wb_led:
        width, height = klemma_4_wb_led.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        klemma_4_wb_led = klemma_4_wb_led.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        klemma_4_wb_led.save('models_named/klemma_4_wb_led.png')

        return klemma_4_wb_led


def klemma_2_wb_mwac():
    with Image.open("models/6.png") as klemma_2_wb_mwac:
        width, height = klemma_2_wb_mwac.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        klemma_2_wb_mwac = klemma_2_wb_mwac.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        klemma_2_wb_mwac.save('models_named/klemma_2_wb_mwac.png')

        return klemma_2_wb_mwac


def WBIO_DO_R10A_8():
    with Image.open("models/7.png") as WBIO_DO_R10A_8:
        width, height = WBIO_DO_R10A_8.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        WBIO_DO_R10A_8 = WBIO_DO_R10A_8.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        WBIO_DO_R10A_8.save('models_named/WBIO_DO_R10A_8.png')

        return WBIO_DO_R10A_8


def klemma_8():
    with Image.open("models/8.png") as klemma_8:
        width, height = klemma_8.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        klemma_8 = klemma_8.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        klemma_8.save('models_named/klemma_8.png')

        return klemma_8


def power():
    with Image.open("models/9.png") as power:
        width, height = power.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        power = power.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        power.save('models_named/power.png')

        return power


def klemma_4():
    with Image.open("models/10.png") as klemma_4:
        width, height = klemma_4.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        klemma_4 = klemma_4.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        klemma_4.save('models_named/klemma_4.png')

        return klemma_4


def QFs3_QFs_avtomat():
    with Image.open("models/11.png") as QFs3_QFs_avtomat:
        width, height = QFs3_QFs_avtomat.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        QFs3_QFs_avtomat = QFs3_QFs_avtomat.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        QFs3_QFs_avtomat.save('models_named/QFs3_QFs_avtomat.png')

        return QFs3_QFs_avtomat


def skat():
    with Image.open("models/12.png") as skat:
        width, height = skat.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        skat = skat.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        skat.save('models_named/skat.png')

        return skat


def controller():
    with Image.open("models/13.png") as controller:
        width, height = controller.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        controller = controller.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        controller.save('models_named/controller.png')

        return controller


def WBIO_DI_WD_14():
    with Image.open("models/14.png") as WBIO_DI_WD_14:
        width, height = WBIO_DI_WD_14.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        WBIO_DI_WD_14 = WBIO_DI_WD_14.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        WBIO_DI_WD_14.save('models_named/WBIO_DI_WD_14.png')

        return WBIO_DI_WD_14


def avtomat():
    with Image.open("models/15.png") as avtomat:
        width, height = avtomat.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        avtomat = avtomat.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        avtomat.save('models_named/avtomat.png')

        return avtomat


def WB_MWAC():
    with Image.open("models/16.png") as WB_MWAC:
        width, height = WB_MWAC.size
        coef = 0.58  # коэффициент изменения размера
        new_width = int(width * coef)
        new_height = int(height * coef)
        # Вычисляем новый размер изображения с сохранением пропорций
        WB_MWAC = WB_MWAC.resize((new_width, new_height))
        # Сохраняем уменьшенное изображение
        WB_MWAC.save('models_named/WB_MWAC.png')

        return WB_MWAC


