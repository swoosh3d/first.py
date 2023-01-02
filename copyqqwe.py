from PIL import Image
run = True
SOURCE_DIR = (r'C:\Users\s1mple\Pictures\Saved Pictures\special4py/')
p1 = input("название файла: ")
myimage = Image.open(SOURCE_DIR + p1)
command = input("и че мне с этим делать?: ")

if command == "дать инфу":
    print(myimage.size)
    print(myimage.mode)
    print(myimage.format)
    print(myimage.info)
    myimage.show()

if command == "изменить размер":
    width0 = int(input("размер в пикселях ширины: "))
    width1 = int(input("размер в пикселях высоты: "))
    newimage = myimage.resize((width0, + width1))
    rgbnewim = newimage.convert('RGB')
    rgbnewim.save(SOURCE_DIR + "NEWIMG.jpeg")
    rgbnewim.show()

if command == "сжать":
    newimage = myimage.quantize(method=2)
    compressedimg = newimage.convert('RGB')
    compressedimg.save(SOURCE_DIR + "COMPRESSED.jpeg")
    compressedimg.show()

if command == "превьюшка":
    preview = myimage.resize((800, 600))
    preview = preview.convert('RGB')
    preview.save(SOURCE_DIR + "PREVIEW.jpeg")
    preview.show()

if command == "превью и сжатие":
    preview = myimage.resize((800, 600))
    preview = preview.convert('RGB')
    preview.save(SOURCE_DIR + "PREVIEW.jpeg")
    compressedimg = myimage.quantize(method=2)
    compressedimg.save(SOURCE_DIR + "COMPRESSED.jpeg")
    
    