from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

#Definindo Funções de cálculos
def calcular():
    
    salario = float(e_valor_quantia.get())

    porcentagemdizimo = (salario / 100) * 10
    porcentagem50 = (salario / 100) * 50
    porcentagem30 = (salario / 100) * 30
    porcentagem10 = (salario / 100) * 10


    necessidades_valor_["text"] = (f"R$ {porcentagem50:.2f}")
    gastos_valor_["text"] = (f"R$ {porcentagem30:.2f}")
    inv_valor_["text"] = (f"R$ {porcentagem10:.2f}")
    dizimo_valor_["text"] = (f"R$ {porcentagemdizimo:.2f}")


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
janela.geometry("250x500")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")



#Definindo Frames
frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=300, height=90, bg=co1, relief="flat")
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=300, height=360, bg=co9, relief="flat")
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

#Frame do Meio
valor_quantia = Label(frameMeio, text="Qual a sua renda mensal?", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
valor_quantia.place(x=7, y=15)
e_valor_quantia = Entry(frameMeio, width=10, font=("Ivy 14"), justify="center", relief="solid")
e_valor_quantia.place(x=10, y=40)

botao_calcular = Button(frameMeio,command=calcular, text="Calcular", width=10, height=1, font=("Ivy 10 bold"), relief="solid", overrelief="ridge")
botao_calcular.place(x=150, y=40)

#Frame de Baixo
textofixo_ = Label(frameBaixo, text="Seu orçamento organizado:  ", relief=FLAT, width=45, anchor=NW, font=("Verdana 10"), bg=co3, fg=co1)
textofixo_.place(x=0, y=0)

#Total necessidades
necessidades_ = Label(frameBaixo, text="Necessidades:  ", relief=FLAT, width=45, anchor=NW, font=("Verdana 10"), bg=co9, fg=co0)
necessidades_.place(x=10, y=40)

necessidades_valor_ = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=("Verdana 12"), bg=co1, fg=co4)
necessidades_valor_.place(x=10, y=75)

#Total gastos
gastos_ = Label(frameBaixo, text="Gastos:  ", relief=FLAT, width=45, anchor=NW, font=("Verdana 10"), bg=co9, fg=co0)
gastos_.place(x=10, y=115)

gastos_valor_ = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=("Verdana 12"), bg=co1, fg=co4)
gastos_valor_.place(x=10, y=145)

#Total investimento
investimentos_ = Label(frameBaixo, text="Investimentos:  ", relief=FLAT, width=45, anchor=NW, font=("Verdana 10"), bg=co9, fg=co0)
investimentos_.place(x=10, y=185)

inv_valor_ = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=("Verdana 12"), bg=co1, fg=co4)
inv_valor_.place(x=10, y=215)

#Total dizimo
dizimo_ = Label(frameBaixo, text="Dízimo:  ", relief=FLAT, width=45, anchor=NW, font=("Verdana 10"), bg=co9, fg=co0)
dizimo_.place(x=10, y=255)

dizimo_valor_ = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=("Verdana 12"), bg=co1, fg=co4)
dizimo_valor_.place(x=10, y=285)






janela.mainloop()