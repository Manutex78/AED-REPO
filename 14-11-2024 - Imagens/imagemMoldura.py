from PIL import Image
import random

def imagemModlura(pathImages,imagem):
    pixelMap = imagem.load()
    for i in range(imagem.width):  
        for j in range(imagem.height):
            if i < 20 or i > imagem.width-20:
                red=random.randint(0,255)
                green=random.randint(0,255)
                blue =random.randint(0,255)           
                pixelMap[i,j] = (red, green, blue)
            if j < 20 or j > imagem.height-20:
                red=random.randint(0,255)
                green=random.randint(0,255)
                blue =random.randint(0,255)
                pixelMap[i,j] = (red, green, blue)
            
    imagem.show()
#imagem.save(pathImages+'teste.jpg')

pathImages = ".\\Images\\"
newSize = (400,400)
imagem = Image.open(pathImages+'img1.jpg')

imagemModlura(pathImages,imagem)

