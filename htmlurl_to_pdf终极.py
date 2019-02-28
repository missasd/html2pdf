import pdfkit,os,glob, pdf2image
from PIL import Image, ImageOps
options = {
        'page-height':"350mm",
        'page-width':"210mm",
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'encoding': "UTF-8",
        'no-outline': None,
        'zoom':'0.75',
   }


html_dir = "/root/html/"
pdf_dir = "/root/pdf/"
img_dir = "/root/img/"
css_dir = html_dir+"modules/bjkcb/rlkb/"
css_file = css_dir+"rljb.css"
if os.path.exists(css_dir):
    pass
else:
    os.makedirs(css_dir)
    print("Copy rljb.css file to modules/bjkcb/rlkb/")
config = pdfkit.configuration(wkhtmltopdf = r'/usr/bin/wkhtmltopdf')


def html_to_pdf(html_dir, pdf_dir, options, config, css ):
    pdf_count = 0
    for filename in os.listdir(html_dir):
        if filename[-5:] == '.html':
            pdf_count += 1
            name = filename[:-5]
            html_abs_path = os.path.join(html_dir, filename)
            pdf_abs_path = os.path.join(pdf_dir, name + '.pdf')
            pdfkit.from_file(html_abs_path, pdf_abs_path, options=options, configuration=config ,css=css)

        else:
            print("Failed")
        print("Now we have convert %s pdf file"%pdf_count)


def pdf_to_png(pdf_dir, img_dir):

    img_count = 0
    img_out_dir = img_dir + "dir"
    if os.path.exists(img_out_dir):
       pass
    else:
       os.makedirs(img_out_dir)
    for filename in os.listdir(pdf_dir):
        if filename[-4:] == '.pdf':
            img_count += 1
            name = filename[:-4]
            pdf_abs_path = os.path.join(pdf_dir, filename)
            pdf2image.convert_from_path(pdf_abs_path, dpi=200, output_folder=img_dir, fmt="png")

            pngdir = glob.glob(img_dir + "*.png")
            newname = str(img_out_dir + "/"+name + ".png")

            os.rename(str(pngdir[0]), str(newname))

            print("Now we have generat %s img file" %img_count)
        else :
            print("failed")
    img_convert(img_dir=img_out_dir)



def img_convert(img_dir):
    format_list = ["png", "jpg", "gif"]
    format_in = input("please choose format:  1.jpg, 2.gif, 3.png   : ")
    format = format_list[int(format_in)]
    padding = (65, 65, 65, 65)
    out_dir = img_dir+"/"+format
    img_count = 0  #
    if os.path.exists(out_dir):

        pass
    else:
        os.makedirs(out_dir)
    for imgfilename in os.listdir(img_dir):
        if imgfilename[-4:] == '.png':
            img_count += 1  #
            print(imgfilename)
            img_abs_dir = os.path.join(img_dir, imgfilename)
            format_out_dir = (out_dir+"/"+imgfilename[:-4])
            print(format_out_dir)
            with open(img_abs_dir, 'rb') as f:
                image = Image.open(f).convert('RGB')
                ivt_image = ImageOps.invert(image)
                bbox = ivt_image.getbbox()
                left = bbox[0] - padding[0]
                top = bbox[1] - padding[1]
                right = bbox[2] + padding[2]
                bottom = bbox[3] + padding[3]
                cropped_image = image.crop([left, top, right, bottom])
                cropped_image.save(format_out_dir+".%s"%format)
                # print"Now we have convert %s img file to %s file" %(img_count, format) #
        else:
            pass

html_to_pdf(html_dir=html_dir, pdf_dir=pdf_dir, options=options, config=config, css=css_file)
pdf_to_png(pdf_dir=pdf_dir, img_dir=img_dir)

    # format_list = ["png", "jpg", "gif"]
    # format_in = input("please choose format:  1.jpg, 2.gif, 3.png   : ")
    # format = format_list[int(format_in)]
    # img_out_dir = img_dir+"/."+format







