# Biblioteca Tkinter: UI
import customtkinter
import CTkMessagebox             # MessageBox
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
from PIL import ImageTk,Image    # Imagens .jpg ou .png
import os                        # diretório atual

# IDENTIFICAÇÃO DO ESTUDANTE    
# Numero :
# Ñome:

#Retorna o caminho absoluto do ficheiro Python atualmente em execução.
root_dir = os.path.dirname(os.path.abspath(__file__))
#Altera o diretório atual para o diretório do ficheiro python
os.chdir(root_dir)

def lerFicheiro(ficheiro):
    """
    Função que lê o ficheiro de texto e retorna uma lista com os dados lidos
    """
    file = open(ficheiro, "r", encoding="utf-8")
    lista = file.readlines()
    file.close()
    return lista

def textBoxFavoritos():
    """
    Função que lê o ficheiro favoritos.txt e retorna o conteúdo do ficheiro
    """
    if not os.path.exists("ficheiros/favoritos.txt"):
        return ""
    else:
        file = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
        textBox = file.read()
        file.close()
        return textBox


# ESCREVER AQUI AS FUNÇÕES SOLICITADAS NO ENUNCIADO
#----------------------------------------------------

def ViewTrails(c1, c2):
    """
    Função que renderiza os trails e ultra trails na Treeview
    """

    tree.delete(*tree.get_children())

    if c1 == "1" and c2 == "0":                     # Trail Curto
        listaTrails = lerFicheiro("ficheiros/trails.txt")
        numProvas = len(listaTrails)
        for linha in listaTrails:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2], campos[3]))
    elif c1 == "0" and c2 == "1":                   # Ultra Trail
        listaUltraTrails = lerFicheiro("ficheiros/ultratrails.txt")
        numProvas = len(listaUltraTrails)
        for linha in listaUltraTrails:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2], campos[3]))
    elif c1 == "1" and c2 == "1":                   # Trail Curto e Ultra Trail
        listaTrails = lerFicheiro("ficheiros/trails.txt")
        numProvas = len(listaTrails)
        for linha in listaTrails:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2], campos[3]))
        listaUltraTrails = lerFicheiro("ficheiros/ultratrails.txt")
        numProvas += len(listaUltraTrails)
        for linha in listaUltraTrails:
            campos = linha.split(";")
            tree.insert("", "end", values=(campos[0], campos[1], campos[2], campos[3]))
    else:
        CTkMessagebox.CTkMessagebox(app, width=200, height=100, title="Erro", message="Selecione pelo menos uma opção", icon="cancel")

    txtNumProvas.configure(state="normal")
    txtNumProvas.delete(0, "end")
    txtNumProvas.insert(0, numProvas)
    txtNumProvas.configure(state="readonly")

def ordAsc(tree):
    """
    Função que ordena a treeview por ordem crescente
    """
    items = [(tree.set(k, "Prova"), k) for k in tree.get_children("")]
    items.sort()
    for index, (val, k) in enumerate(items):
        tree.move(k, "", index)
    
def ordDesc(tree):
    """
    Função que ordena a treeview por ordem decrescente
    """
    items = [(tree.set(k, "Prova"), k) for k in tree.get_children("")] 
    items.sort(reverse=True)
    for index, (val, k) in enumerate(items):
        tree.move(k, "", index)
    
def notificacoes(tree):
    """
    Função que deve abrir uma messagebox notificando o utilizador da prova
    mais próxima da data atual (de entre as provas renderizadas na Tree)
    """
    from datetime import datetime

    items = tree.get_children()
    if not items:
        CTkMessagebox.CTkMessagebox(app, width=200, height=100, title="Erro", message="Nenhuma prova disponível", icon="cancel")
        return

    closest_event = None
    closest_date = None

    for item in items:
        prova = tree.item(item)["values"]
        prova_date = datetime.strptime(prova[1], "%Y-%m-%d")
        if closest_date is None or prova_date < closest_date:
            closest_date = prova_date
            closest_event = prova

    if closest_event:
        CTkMessagebox.CTkMessagebox(app, width=200, height=100, title="Notificação", message=f"Prova mais próxima: {closest_event[0]}", icon="info")
    
def selecionarImagem():
    """
    Função que permite ao utilizador selecionar uma imagem da pasta Imagens
    e configurá-la no btnImagem
    """
    filename = filedialog.askopenfilename(initialdir = "./imagens", title = "Selecione uma imagem", filetypes = (("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    img = customtkinter.CTkImage(Image.open(f'{filename}'), size=(180, 180))
    btnImagem.configure(image=img)
    
def addFavoritos(linha):
    """
    Função que adiciona a prova selecionada na Tree à lista de favoritos.
    """
    prova = tree.item(linha)["values"]
    lboxFav.insert("end", f'{prova[0]}\n')

def filefavoritos(textBox):
    """
    Função que  deve criar o ficheiro favoritos.txt dentro da pasta ficheiros.
    O ficheiro favoritos.txt deve conter a lista de favoritos que está apresentada na TextBox de Favoritos.
    """
    file = open("ficheiros/favoritos.txt", "w", encoding="utf-8")
    file.write(textBox)
    file.close()
    
#----------------------------------------------------
# GUI  INTERFACE GRAFICA -----------------------------------------------
#----------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False) 


#-----Arranque da aplicação -------------------------------- 
app=customtkinter.CTk()                  # invoca classe Ctk , cria a "main window"
renderWindow(1000, 500, "Trails App")


# Tree onde são renderizados os trails e / opu UltraTrails
tree = ttk.Treeview(app, columns = ("Prova", "Data", "Local", "Km"), show = "headings", height = 8, selectmode = "browse")
tree.column("Prova", width = 150, anchor = "w")
tree.column("Data", width = 100, anchor = "c")
tree.column("Local", width = 150, anchor = "c")
tree.column("Km", width = 100, anchor = "c")

tree.heading("Prova", text = "Prova")
tree.heading("Data", text = "Data")
tree.heading("Local", text = "Local")
tree.heading("Km", text = "Km")

# 2.1  CheckBox - definir atributos / variáveis para as CheckBox.  A segunda deve estar ativa, por defeito

ckVar1 = customtkinter.StringVar(value="0")
ckVar2 = customtkinter.StringVar(value="1")
ckBox1 = customtkinter.CTkCheckBox(app, text = "Trail Curto", variable=ckVar1, onvalue="1", offvalue="0")
ckBox2 = customtkinter.CTkCheckBox(app, text = "Ultra Trail ",variable=ckVar2, onvalue="1", offvalue="0")
ckBox1.place(x=50, y=20)
ckBox2.place(x=150, y=20)




# 2.2 btnSearch - deve invocar a função viewTrails 
btnImage1 = customtkinter.CTkImage(Image.open(".\\imagens\\pesquisar.png"), size=(35, 35))
btnSearch = customtkinter.CTkButton(app, width=35, height=35, image = btnImage1, text = "", fg_color="transparent",  
                                    command = lambda: ViewTrails(ckVar1.get(), ckVar2.get()))   
btnSearch.place(x=300, y=12)


# 2.3 btnAsc - Deve invocar a função ordAsc
btnImage2 = customtkinter.CTkImage(Image.open(".\\imagens\\asc.png"), size=(35, 35))
btnAsc = customtkinter.CTkButton(app, width=35, height=35, image = btnImage2 , text = "", fg_color="transparent",
                                 command = lambda: ordAsc(tree))
btnAsc.place(x=400, y=12)


# 2.4 btnDesc - Deve invocar a função ordDesc 
btnImage3 = customtkinter.CTkImage(Image.open(".\\imagens\\desc.png"), size=(35, 35))
btnDesc = customtkinter.CTkButton(app, width=35, height=35, image = btnImage3,  text = "", fg_color="transparent", 
                                command = lambda: ordDesc(tree))
btnDesc.place(x=500, y=12)


# 2.5 btnNotificações  - Deve invocar a função notificacoes
btnImage4 = customtkinter.CTkImage(Image.open(".\\imagens\\notificacao.png"), size=(40, 40))
btnNotificacoes = customtkinter.CTkButton(app, width=48, height=48, image = btnImage4 , text = "", fg_color="transparent", 
                                command = lambda: notificacoes(tree))
btnNotificacoes.place(x=600, y=12)



lblCircuitos = customtkinter.CTkLabel(app, text = "Os meus circuitos", font = ("Helvetica", 14), text_color= "red")
lblCircuitos.place(x=200, y=50)


tree.place(x=20, y=100) # renderiza a treeview na janela principal


lblNumProvas = customtkinter.CTkLabel(app, text = "Nº de provas", font = ("Helvetica", 13))
lblNumProvas.place(x=50, y=320)

# 2.6 Nº DE PROVAS renderizadas na TREE deve aparecer nesta Entry

txtNumProvas = customtkinter.CTkEntry(app, width=50,state="readonly")
txtNumProvas.place(x=150, y=320)



# 2.7 btnSelecionarImg - Invoca  função selecionarImagem, que deve permitir ao utilizador selecionar uma imagem da pasta Imagens
#  e configurá-la no btnImagem  

btnSelecionarImg = customtkinter.CTkButton(app, width=45, height = 45, text = "Selecionar Imagem", fg_color="black", text_color="cyan", 
                        command = lambda: selecionarImagem())
btnSelecionarImg.place(x=180, y=430)

img = customtkinter.CTkImage(Image.open(".\\imagens\\img1.png"), size=(180, 180))
btnImagem = customtkinter.CTkButton(app, width=180, height=180, image = img , text = "", fg_color="transparent")
btnImagem.place(x=330, y=300)


# 2.8 Deve invocar a função addFavoritos
btnAddFav = customtkinter.CTkButton(app, text = "Adicionar >>\n Favoritos", height=45, fg_color="black", text_color="cyan", 
                                command = lambda: addFavoritos(tree.focus()))
btnAddFav.place(x=550, y=150)



frame1 = customtkinter.CTkFrame(app, width = 300, height = 500)
frame1.place(x=700, y=1)

lblFav= customtkinter.CTkLabel(frame1, text = "Favoritos", font = ("Helvetica", 14) )
lblFav.place(x=100, y=30)

lboxFav = customtkinter.CTkTextbox(frame1,width=250, height=250, fg_color="gray", text_color="white")
lboxFav.place(x=20, y=60)
lboxFav.insert("end", textBoxFavoritos())

# 2.9 Deve invocar a função filefavoritos 
imgFavorite = ImageTk.PhotoImage(file = ".\\imagens\\GuardarFile.png")
btnGuardarFav = customtkinter.CTkButton(frame1, image= imgFavorite, text = "Guardar Favoritos", height=90, width=250, fg_color="black", text_color="cyan",
                                        command = lambda: filefavoritos(lboxFav.get("0.0","end")), compound="top")
btnGuardarFav.place(x=20, y=320)





app.mainloop()   # event listening loop by calling the mainloop()