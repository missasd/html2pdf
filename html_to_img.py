import imgkit
root_dir = "D:\Backup\Desktop\hello"
img_dir = "D:\Backup\Desktop\kebiao\day_old_img"
css = "D:/Backup/Desktop/hello/modules/bjkcb/rlkb/rljb.css"
# config = imgkit.config(wkhtmltopdf = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
config = imgkit.config(wkhtmltoimage=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
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
img = imgkit.from_file(r"D:\Backup\Desktop\hello\16029113.html", r"D:\Backup\Desktop\kebiao\day_old_img\1.jpg", config=config, options=options,)
print(img)


