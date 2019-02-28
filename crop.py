from io import BytesIO
from PIL import Image, ImageOps
png_path = r"D:\Backup\Desktop\1801019.png"
padding = (70, 70, 70, 70)
with open(png_path,'rb') as f:
    image = Image.open(f).convert('RGB')
    ivt_image = ImageOps.invert(image)
    bbox = ivt_image.getbbox()
    left = bbox[0]- padding[0]
    top = bbox[1]- padding[1]
    right = bbox[2]+ padding[2]
    bottom = bbox[3]+ padding[3]
    cropped_image = image.crop([left, top, right, bottom])
    cropped_image.save(r"D:\Backup\Desktop\1801019.jpg")
    # f.save(r"D:\Backup\Desktop\222.png")

def img_convert(img_dir, format):



