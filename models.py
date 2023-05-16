from PIL import Image
from pathlib import Path
list_images = []

klemma2 = Image.open('app/models/0.png')
klemma2 = klemma2.crop((1001, 829, 1240, 1440))
klemma2_path = Path("app/models_named/klemma2.png")
list_images.append(klemma2_path.name.replace('.png', ''))
width_klemma2, height_klemma2 = klemma2.size


WB_MR6C_v2 = Image.open('app/models/1.png')
WB_MR6C_v2 = WB_MR6C_v2.crop((382, 744, 793, 1632))
WB_MR6C_v2_path = Path("app/models_named/WB_MR6C_v2.png")


WB_MR6C_v2.show()