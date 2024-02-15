from PIL import Image, ImageFilter
import sys
import os

# first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
