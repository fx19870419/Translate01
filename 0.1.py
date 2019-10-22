import sys,fitz
import os
from PIL import Image
import pytesseract


#读取PDF
pdf = fitz.open('guoyan.pdf')


#将PDF的每一页都存放在images文件夹中
for pg in range(pdf.pageCount):
    print('正在转换第'+str(pg+1)+'页')
    page = pdf[pg]
    zoom_x = 1.3333333
    zoom_y = 1.3333333
    mat = fitz.Matrix(zoom_x,zoom_y).preRotate(0)
    pix = page.getPixmap(matrix = mat,alpha = False)
    if not os.path.exists('images'):
        os.makedirs('images')
    pix.writePNG('images' + '/'+'images_%s.png'%str(pg).rjust(2,'0'))
    print('第' + str(pg+1) + '页已转换完成')
print('全部PDF已转换完成')
print('-----------------')

#从images文件夹中读取文件并识别
if not os.path.exists('txts'):
    os.makedirs('txts')
png_list = os.listdir('images')
for i in png_list:
    print('正在识别第' + str(int(i[7:9]) + 1).rjust(2,'0') + '页')
    txt = pytesseract.image_to_string(Image.open('images/'+i),'eng')
    txt_file = open(('txts/txt_'+str(int(i[7:9]) + 1).rjust(2,'0')+'.txt'),'w',encoding = 'utf-8')
    txt_file.write(txt)
    txt_file.close()
    print('第' + str(int(i[7:9]) + 1).rjust(2,'0') + '页已识别完毕并保存')
