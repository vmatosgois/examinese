from PIL import Image
import io
import os

image_path = "images"

# Ajuda

byte_class = io.BytesIO()
ajuda_b = Image.open(os.path.join(image_path, "Ajuda_branca.png"))
ajuda_b.save(byte_class, "PNG")
byte_class.seek(0)
ajuda_b = byte_class.read()
ajuda_b_final = io.BytesIO(ajuda_b)

byte_class = io.BytesIO()
ajuda_p = Image.open(os.path.join(image_path, "Ajuda_preta.png"))
ajuda_p.save(byte_class, "PNG")
byte_class.seek(0)
ajuda_p = byte_class.read()
ajuda_p_final = io.BytesIO(ajuda_p)

# Calc

byte_class = io.BytesIO()
calc_b = Image.open(os.path.join(image_path, "Calc_branca.png"))
calc_b.save(byte_class, "PNG")
byte_class.seek(0)
calc_b = byte_class.read()
calc_b_final = io.BytesIO(calc_b)

byte_class = io.BytesIO()
calc_p = Image.open(os.path.join(image_path, "Calc_preta.png"))
calc_p.save(byte_class, "PNG")
byte_class.seek(0)
calc_p = byte_class.read()
calc_p_final = io.BytesIO(calc_p)

# Config

byte_class = io.BytesIO()
config_b = Image.open(os.path.join(image_path, "Config_branca.png"))
config_b.save(byte_class, "PNG")
byte_class.seek(0)
config_b = byte_class.read()
config_b_final = io.BytesIO(config_b)

byte_class = io.BytesIO()
config_p = Image.open(os.path.join(image_path, "Config_preta.png"))
config_p.save(byte_class, "PNG")
byte_class.seek(0)
config_p = byte_class.read()
config_p_final = io.BytesIO(config_p)

# Home

byte_class = io.BytesIO()
home_b = Image.open(os.path.join(image_path, "Home_branca.png"))
home_b.save(byte_class, "PNG")
byte_class.seek(0)
home_b = byte_class.read()
home_b_final = io.BytesIO(home_b)

byte_class = io.BytesIO()
home_p = Image.open(os.path.join(image_path, "Home_preta.png"))
home_p.save(byte_class, "PNG")
byte_class.seek(0)
home_p = byte_class.read()
home_p_final = io.BytesIO(home_p)

# Lab

byte_class = io.BytesIO()
lab_b = Image.open(os.path.join(image_path, "Lab_branca.png"))
lab_b.save(byte_class, "PNG")
byte_class.seek(0)
lab_b = byte_class.read()
lab_b_final = io.BytesIO(lab_b)

byte_class = io.BytesIO()
lab_p = Image.open(os.path.join(image_path, "Lab_preta.png"))
lab_p.save(byte_class, "PNG")
byte_class.seek(0)
lab_p = byte_class.read()
lab_p_final = io.BytesIO(lab_p)

# Espiro

byte_class = io.BytesIO()
lung_b = Image.open(os.path.join(image_path, "lung_branca.png"))
lung_b.save(byte_class, "PNG")
byte_class.seek(0)
lung_b = byte_class.read()
lung_b_final = io.BytesIO(lung_b)

byte_class = io.BytesIO()
lung_p = Image.open(os.path.join(image_path, "lung_preta.png"))
lung_p.save(byte_class, "PNG")
byte_class.seek(0)
lung_p = byte_class.read()
lung_p_final = io.BytesIO(lung_p)

# UFs

byte_class = io.BytesIO()
ufs_b = Image.open(os.path.join(image_path, "ufs_horizontal_branca.png"))
ufs_b.save(byte_class, "PNG")
byte_class.seek(0)
ufs_b = byte_class.read()
ufs_b_final = io.BytesIO(ufs_b)

byte_class = io.BytesIO()
ufs_p = Image.open(os.path.join(image_path, "ufs_horizontal_preta.png"))
ufs_p.save(byte_class, "PNG")
byte_class.seek(0)
ufs_p = byte_class.read()
ufs_p_final = io.BytesIO(ufs_p)