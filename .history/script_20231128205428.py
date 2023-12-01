from tkinter import Tk, Button, Label, Canvas, BOTH, YES, NW, CENTER
from PIL import Image, ImageTk
from dados import PERGUNTAS

#variaveis do jogo
pontos = 0 
indice_atual = 0
pergunta_atual = PERGUNTAS[indice_atual]
lista_botoes = []

#criar janela no tkinter
root = Tk()
root.geometry("1400x1200")
root.title("Quiz")


#funçao ao precionar as alternativas
def CliqueNoBotao(indice_alternativa, pergunta_atual):
    global indice_atual, pontos
    if  indice_atual < len(PERGUNTAS)-1:
        indice_atual += 1 
        alternativa = pergunta_atual.alternativas[indice_alternativa]
        
        if alternativa.correta:
            pontos = pontos + 10

        pergunta_atual = PERGUNTAS[indice_atual]
        CarregarPergunta(pergunta_atual)
    else:
        AbrirResultados()

#carregar e converter uma imagem
def load_image(file_path, width, height):
    imagem = Image.open(file_path)
    imagem = imagem.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(imagem)

#varioaveis referentes as imagens
imagem_path = "QUIZ GEEK (1).png"
bg = load_image(imagem_path, 1400, 1000)
bg2 = load_image("bg_laranja.png", 1400, 1000)
imagem_flv = load_image("orange.png", 350, 100) 


#contruindo background
canvas = Canvas(root, width=1400, height=1200)
canvas.pack(fill=BOTH, expand=YES)
bg_questoes = canvas.create_image(0, 0, anchor=NW, image=bg2)
bg_menu = canvas.create_image(0, 0, anchor=NW, image=bg)


#menu inicial
btn_play = Button(root,text="PLAY",compound=CENTER,width=4, height=1,border=False,bg="#FAEA0C",command=lambda:comecar())
btn_play.place(x=248, y=795)
btn_play.configure(font=("Courier", 44, "italic"))

btn_quit = Button(root,text="QUIT",compound=CENTER,width=4, height=1,border=False,bg="#FAEA0C")
btn_quit.place(x=976, y=795)
btn_quit.configure(font=("Courier", 44, "italic"))

#fução que será executada ao clicar no botão play
def comecar():
    btn_play.destroy()
    btn_quit.destroy()
    canvas.delete(bg_menu)
    CarregarPergunta(pergunta_atual)
  

#alternativas/imagens do botão
def CarregarPergunta(pergunta_atual):
    lbpergunta = Label(root, text=pergunta_atual.enunciado, background="#c89546", foreground="#000000", width=75, height=12,font=("bold italic",17))
    lbpergunta.place(x=230, y=273)

    btn1 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[0].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(0, pergunta_atual),font=("bold italic",16))
    btn1.place(x=140, y=650)

    btn2 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[1].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(1, pergunta_atual),font=("bold italic",16))
    btn2.place(x=140, y=850)

    btn3 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[2].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(2, pergunta_atual),font=("bold italic",16))
    btn3.place(x=900, y=850)

    btn4 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[3].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(3, pergunta_atual),font=("bold italic",16))
    btn4.place(x=900, y=650)

    lista_botoes.append(lbpergunta)
    lista_botoes.append(btn1)
    lista_botoes.append(btn2)
    lista_botoes.append(btn3)
    lista_botoes.append(btn4)

def AbrirResultados():
    bg_menu = canvas.create_image(0, 0, anchor=NW, image=bg)
    for item in lista_botoes:
        item.destroy()
    
    LbResultado= Label(root, text="TESTE"+str(pontos))
    LbResultado.place(x=230, y=273)

    btn_play = Button(root,text="PLAY",compound=CENTER,width=4, height=1,border=False,bg="#FAEA0C",command=lambda:comecar())
    btn_play.place(x=248, y=795)
    btn_play.configure(font=("Courier", 44, "italic"))

    btn_quit = Button(root,text="QUIT",compound=CENTER,width=4, height=1,border=False,bg="#FAEA0C")
    btn_quit.place(x=976, y=795)
    btn_quit.configure(font=("Courier", 44, "italic"))

root.mainloop()