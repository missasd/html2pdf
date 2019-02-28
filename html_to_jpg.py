import pdfkit
import os
import os.path
import wkhtmltopdf

# coding: utf-8
root_dir = r'/root'
import pdfkit
import os
import os.path

# coding: utf-8
root_dir = r'/root/html/'
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        print("The parent path is :"+dirpath)
        print('filename is :' + filename)
        currentPath = os.path.join(dirpath, filename)
        currentname = os.path.splitext(str(filenames))[0]
        currentname = currentname[2:]
        pdfpath = os.path.join(dirpath, currentname)

        print('The full name of the file is:'+currentPath)
        print('The pdf name is '+currentname)
        pdfkit.from_file("%s" % currentPath, '%s.pdf' % pdfpath, css='rljb.css')



# 指明被遍历的文件夹
# rootdir = r'D:\FFOutput'
# for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
#     for filename in filenames:
#         print('parent is :' + parent)
#         print('filename is :' + filename)
#         currentPath = os.path.join(parent, filename)
#         print('the fulll name of the file is :' + currentPath)
#
#         img = Image.open(currentPath)
#         print(img.format, img.size, img.mode)
#         # img.show()
#         box1 = (0, 50, 1243,2000)  # 设置左、上、右、下的像素
#         image1 = img.crop(box1)  # 图像裁剪
#         image1.save(r"D:\FFOutput\Output" + '\\' + filename)  # 存储裁剪得到的图像



