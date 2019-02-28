##此为最终程序

import pdfkit,os,glob, pdf2image
options = {
        #'zoom': '1.2',
        #  'disable-smart-shrinking':'',    智能自动缩放
        # 'collate':'1',
        'page-size': 'B4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        # 'orientation':'Landscape',#横向
        'encoding': "UTF-8",
        'no-outline': None,
        # 'quiet':'',
          # 'footer-right':'[page]' 设置页码
   }
# wkhtmltopdf=/usr/bin/wkhtmltopdf


html_dir = ""
# 为html文件的路径
pdf_dir = ""
#此为pdf文件的输出路径
img_dir = ""
#此为png文件的输出路径

css_dir = html_dir+"modules/bjkcb/rlkb/"
css_file = css_dir+"rljb.css"
if os.path.exists(css_dir):
    pass
else:
    os.makedirs(css_dir)
    print("Copy rljb.css file to modules/bjkcb/rlkb/")

config = pdfkit.configuration(wkhtmltopdf = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')



def html_to_pdf(html_dir, pdf_dir, options, config, css):
    for filename in os.listdir(html_dir):
        if filename[-5:] == '.html':
            #判断文件类型为html
            name = filename[:-5]
            #取出文件名
            html_abs_path = os.path.join(html_dir, filename)
            pdf_abs_path = os.path.join(pdf_dir, name + '.pdf')
            pdfkit.from_file(html_abs_path, pdf_abs_path, options=options, configuration=config, css=css)

        else:
            print("Failed")


def pdf_to_png(pdf_dir, img_dir):
    img_out_dir = img_dir + "/dir"
    if os.path.exists(img_out_dir):
        pass
    else:
        os.makedirs(img_out_dir)
    for filename in os.listdir(pdf_dir):
        if filename[-4:] == '.pdf':
            name = filename[:-4]
            pdf_abs_path = os.path.join(pdf_dir, filename)
            pdf2image.convert_from_path(pdf_abs_path, dpi=200, output_folder=img_dir, fmt="png")

            pngdir = glob.glob(img_dir + "*.png")


            newname = str(img_out_dir + "/"+name + ".png")


            os.rename(str(pngdir[0]), str(newname))
        else:
            print("failed")

html_to_pdf(html_dir=html_dir, pdf_dir=pdf_dir, options=options, config=config, css=css_dir)
pdf_to_png(pdf_dir=pdf_dir, img_dir=img_dir)

pdf_count = 0
pdf_count += 1
print("Now we have convert %s pdf file"%pdf_count)

img_count = 0
img_count += 1
print("Now we have convert %s png file"%pdf_count)


