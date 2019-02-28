from bs4 import BeautifulSoup

# with open(r"D:\Backup\Desktop\hello\1502013.html","r", encoding='UTF-8') as file:
# #对 try finally的简化
#     fcontent = file.read()
#     sp = BeautifulSoup(fcontent, 'lxml')
#     t = 'x82 '
#
#     sp.replace(sp.find({"class='x82 x199'":"class='x82 '"}).string,t)

with open(r"D:\Backup\Desktop\rljb.css", "r", encoding='UTF-8') as file:
    fcontent = file.read()
    for lines in fcontent:
        if "x"

