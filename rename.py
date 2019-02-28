# from pdf2image import *
# from PIL import *
# import os
# import glob
# direc = "/root/"
# filename = "1603014.pdf"
# name = filename[:-4]
# pngname = direc+name+".png"
#
#
# pdfdir = direc+filename
# pngdir = direc+filename[:-4]+".png"
#
# images = convert_from_path(pdfdir, dpi=200, output_folder=direc, fmt="png" )
# print type(images)
# print(images)
#
# pngdir = glob.glob(direc+"*.png")
# newname = str(direc+name+".png")
# print pngdir[0]
# print newname
# os.rename(str(pngdir[0]), str(newname))
#
# # def pdf_to_img(root_dir, img_dir):
#
#
#
#

import os
path = r"D:\Backup\Desktop\hello\16029113.html"
path_1 = r"D:\Backup\Desktop\hello\modules\16029113.html"
os.rename(path,path_1)

