from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

#Definindo Cores
co0 = "#2e2d2b" #Preto
co1 = "#feffff" #Branco
co2 = "#4fa882" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letras
co5 = "#e06636" # - profit
co6 = '#038cfc' #Azul
co7 = "#3fbfb9" #Verde 
co8 = "263238" #Verde 1
co9 = "#e9edf5" #Verde 2
co10 = "#6e8faf"
co11 = "#f2f4f2"



#Criando Janela
janela = Tk()
janela.title("")
janela.geometry("250x400")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")



#Definindo Frames
frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=300, height=90, bg=co1, relief="flat")
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
frameBaixo.grid(row=2, column=0)


#Logo
app_ = Label(frameCima, text="Orçamento", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=("Verdana 20"), bg=co1, fg=co4)
app_.place(x=0, y=0)

#Imagens
app_img = Image.open("logo.png")
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=160, y=0)

linha = Label(frameCima, width=295, height=1, anchor=NW, font=("Verdana 1"), bg=co3, fg=co1)
linha.place(x=0, y=47)





janela.mainloop()