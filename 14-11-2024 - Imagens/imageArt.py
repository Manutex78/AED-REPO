from PIL import Image

"""
Cria uma imagem 400x400 pixels
"""

pathImages = ".\\Images\\"

newSize = (400,400)

imagem = Image.new(size=newSize, mode = "RGB", color="white")

pixelMap = imagem.load()

for i in range(imagem.width):
    for j in range(imagem.height):
        red=i
        green=j
        blue = 255-j
        pixelMap[i,j] = (red, green, blue)

imagem.show()
imagem.save(pathImages+'teste.jpg')



