from PIL import Image

def imageGrayScale(pathImages,imagem1):
    pixelMap = imagem1.load()
    for i in range(imagem1.width):
        for j in range(imagem1.height):
            p = pixelMap[i,j]
            red = p[0]
            green = p[1]
            blue = p[2]
            red = green = blue = int(0.299 * red + 0.587 * green + 0.114 *blue)
            pixelMap[i,j] = (red,green,blue)
    imagem1.show()
    imagem1.save(pathImages+'ImgGray.jpg')


pathImages = ".\\images\\"
imagem1 = Image.open(pathImages + "img1.jpg")
imageGrayScale(pathImages,imagem1)