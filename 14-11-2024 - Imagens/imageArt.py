from PIL import Image
import random
"""
Cria uma imagem 400x400 pixels
"""

pathImages = ".\\Images\\"

newSize = (400,400)

imagem = Image.new(size=newSize, mode = "RGB", color="white")

pixelMap = imagem.load()

for i in range(imagem.width):
    for j in range(imagem.height):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue =random.randint(0,255)
        pixelMap[i,j] = (red, green, blue)

imagem.show()
imagem.save(pathImages+'teste.jpg')



