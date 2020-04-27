from functools import partial
from tkinter import *

def bt_click(a,b):
    soma=a+b
    return(soma)
janela = Tk()
janela.title("SOMA")
janela["background"] = "light blue"
janela.geometry("200x300+400+300")

ed1 = Entry(janela)#Aqui é criado o primeiro widget
ed1.place(x=50, y=100)

ed2 = Entry(janela)#Aqui é criado o segundo widget
ed2.place(x=50, y=130)

bt=Button(janela, width=15, text="SOMA")
bt.place(x=55, y=155)
bt["command"]= partial(bt_click,ed1,ed2)

lb = Label(janela,width=5 ,text="")#Aqui trataremos da mensagem que ficará abaixo do botão. Label é uma mensagem mostrada no conteiner, neste caso no principal
lb.place(x=100, y=180)
janela.mainloop()
