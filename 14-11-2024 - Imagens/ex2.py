from PIL import Image
import random
"""
Cria uma imagem 400x400 pixels
"""

pathImages = ".\\Images\\"

newSize = (240,240)

imagem = Image.new(size=newSize, mode = "RGB", color="white")

pixelMap = imagem.load()

for i in range(imagem.width):
    for j in range(imagem.height):
        if i<80:
            pixelMap[i,j] = (0,0,255)
        elif i<160:
            pixelMap[i,j] = (255,255,255)
        else:
            pixelMap[i,j] = (255,0,0)

imagem.show()
imagem.save(pathImages+'ex2.jpg')



