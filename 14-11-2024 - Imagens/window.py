from PIL import Image
import random

def window(pathImages,imagem):
    pixelMap = imagem.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            if j < 10 or j > imagem.height-10:
                pixelMap[i,j] = (0,0,255)
            elif j > ((imagem.height/2)-5) and j < ((imagem.height/2)+5):
                pixelMap[i,j] = (0,0,255)
            elif i < 10 or i > imagem.width-10:           
                pixelMap[i,j] = (0,0,255)
            elif i > ((imagem.width/2)-5) and i < ((imagem.width/2)+5):
                pixelMap[i,j] = (0,0,255)
            
    imagem.show()
    imagem.save(pathImages+'window.jpg')

pathImages = ".\\Images\\"
newSize = (400,400)
imagem = Image.open(pathImages+'img1.jpg')

window(pathImages,imagem)

