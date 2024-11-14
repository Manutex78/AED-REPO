from PIL import Image
import random

def window(pathImages,imagem):
    pixelMap = imagem.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            if j < 10 or j > imagem.height-10:
                red=random.randint(0,255)
                green=random.randint(0,255)
                blue =random.randint(0,255)
                pixelMap[i,j] = (red, green, blue)
            elif j > ((imagem.height/2)-5) and j < ((imagem.height/2)+5):
                red=random.randint(0,255)
                green=random.randint(0,255)
                blue =random.randint(0,255)
                pixelMap[i,j] = (red, green, blue)
            elif i < 10 or i > imagem.width-10:
                red=random.randint(0,255)
                green=random.randint(0,255)
                blue =random.randint(0,255)           
                pixelMap[i,j] = (red, green, blue)
            elif i > ((imagem.width/2)-5) and i < ((imagem.width/2)+5):
                red=random.randint(0,255)
                green=random.randint(0,255)
                blue =random.randint(0,255)
                pixelMap[i,j] = (red, green, blue)
            
    imagem.show()
    imagem.save(pathImages+'window.jpg')

pathImages = ".\\Images\\"
newSize = (400,400)
imagem = Image.open(pathImages+'img1.jpg')

window(pathImages,imagem)

