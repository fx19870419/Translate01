from wand.image import Image

'''
pdf = Image(filename='guoyan.pdf',resolution =300)
jpeg = pdf.convert('jpg')


images=[]
for i in jpeg.sequence:
    page = Image(image=i)
    images.append(page.make_blob('jpg'))



i = 0
for img in images:
    ff = open(str(i)+'.jpg','wb')
    ff.write(img)
    ff.close()
    i += 1
'''
filename="guoyan.pdf"
with(Image(filename=filename, resolution=120)) as source: 
    images = source.sequence
    pages = len(images)
    for i in range(pages):
        n = i + 1
        newfilename = filename[:-4] + str(n) + '.jpeg'
        Image(images[i]).save(filename=newfilename)
