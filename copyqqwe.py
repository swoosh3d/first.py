from PIL import Image

SOURCE_DIR = (r'C:\Users\s1mple\Pictures\Saved Pictures\special4py/')

run = True

def help():
    print ("""
    Для подробной информации о фото используйте команду "info"
    Для сжатия изображения используйте команду "compress"
    Для изменения размера фото используйте команду "resize"
    Для создания картинки размером 800x600 используйте команду "preview"
    Для сжатия и создания превью одного и того же изображения используйте команду "compress and preview"
    Для завершения программы используйте "exit"
    """)

def info():
    print(myimage.size)
    print(myimage.mode)
    print(myimage.format)
    print(myimage.info)
    myimage.show()

def resize():
    width0 = int(input("размер в пикселях ширины: "))
    width1 = int(input("размер в пикселях высоты: "))
    newimage = myimage.resize((width0, + width1))
    rgbnewim = newimage.convert('RGB')
    rgbnewim.save(SOURCE_DIR + "NEWIMG.jpeg")
    rgbnewim.show()

def compress():
    newimage = myimage.quantize(method=2)
    compressedimg = newimage.convert('RGB')
    compressedimg.save(SOURCE_DIR + "COMPRESSED.jpeg")
    compressedimg.show()

def preview():
    preview = myimage.resize((800, 600))
    preview = preview.convert('RGB')
    preview.save(SOURCE_DIR + "PREVIEW.jpeg")
    preview.show()

def comress_and_preview():
    preview = myimage.resize((800, 600))
    preview = preview.convert('RGB')
    preview.save(SOURCE_DIR + "PREVIEW.jpeg")
    compressedimg = myimage.quantize(method=2)
    compressedimg.save(SOURCE_DIR + "COMPRESSED.jpeg")
        
while run:
    file_name = input("название файла: ")

    myimage = Image.open(SOURCE_DIR + file_name)

    command = input("Введите команду: ")

    if command == "info":
        info()
    elif command == "help":
        help()
    elif command == "resize":
        resize()
    elif command == "compress":
        compress()
    elif command == "preview":
        preview()
    elif command == "compress_and_preview":
        comress_and_preview()
    elif command == "exit":
        print("удачи!")
        break
    else:
        help()