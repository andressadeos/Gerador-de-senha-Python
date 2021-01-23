import string
from string import *
import random
import tkinter 
from tkinter import * #importando o pacote

app=Tk() #instanciando a classe
app.title("TBank") #definindo o titulo do app
app.geometry("800x600") #definindo o tamanho da tela do app

texto = Label(app, text="Bem-vindo ao TBank!", font="ArialBlack 20 bold")
texto.pack()

texto = Label(app, text="Selecione uma opção", font="Arial 16")
texto.pack()


#criar checkbox 01 tela
#Caixa
#Gerencia PJ
#Gerencia PF

#associar uma função a checkbox 01 tela

botao = Button(app, text="Próximo")
botao.pack()

#criar checkbox 02 tela
#Preferencial
#Não Preferencial

#associar uma função a checkbox 02 tela


#botao = Button(app, text="Próximo")
#botao.pack()

#criar 03 tela
#imput numero celular
#botao = Button(app, text="Enviar")
#botao.pack()

#associar uma função a checkbox 03 tela

app.mainloop() #colocando o app em loop para permanecer aberto até que o usuario o feche    



#determinar senha aleatória
#NUMBER = strings.digits