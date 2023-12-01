from tkinter import Tk, Button, Label, Canvas, BOTH, YES, NW, CENTER
from PIL import Image, ImageTk
from dados import PERGUNTAS

pontos = 0 
indice_atual = 0
pergunta_atual = PERGUNTAS[indice_atual]

def CliqueNoBotao(indice_alternativa, pergunta_atual):
     
    global indice_atual, pontos
    indice_atual += 1 
    alternativa = pergunta_atual.alternativas[indice_alternativa]
    
    if alternativa.correta:
        pontos = pontos + 10

    pergunta_atual = PERGUNTAS[indice_atual]
    CarregarPergunta(pergunta_atual)


imagem_path = "bg_laranja.png"

def load_image(file_path, width, height):
    imagem = Image.open(file_path)
    imagem = imagem.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(imagem)

root = Tk()
root.geometry("1400x1200")
root.title("Quiz")

pontos = 0

bg = load_image(imagem_path, 1400, 1100)

canvas = Canvas(root, width=1400, height=1200)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, anchor=NW, image=bg)

imagem_flv = load_image("orange.png", 350,100 ) 

def CarregarPergunta(pergunta_atual):

    lbpergunta = Label(root, text=pergunta_atual.enunciado,background="#c89546", foreground="#000000", width=80, height=12,font=("Arial",14))
    lbpergunta.place(x=255, y=273)

    btn1 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[0].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(0, pergunta_atual))
    btn1.place(x=140, y=650)

    btn2 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[1].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(1, pergunta_atual))
    btn2.place(x=140, y=850)

    btn3 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[2].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(2, pergunta_atual))
    btn3.place(x=900, y=850)

    btn4 = Button(root, image=imagem_flv, text=pergunta_atual.alternativas[3].texto, compound=CENTER, width=400, height=60,border=False,bg="#c89546",command=lambda: CliqueNoBotao(3, pergunta_atual))
    btn4.place(x=900, y=650)

CarregarPergunta(pergunta_atual)

root.mainloop()