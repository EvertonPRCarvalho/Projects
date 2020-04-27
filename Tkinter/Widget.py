from functools import partial
from tkinter import *


def bt_click(botao):
    print(botao["text"])


janela = Tk()
janela.title("Janela principal")
janela["background"] = "light gray"
janela.geometry("600x600+200+200")
bt = Button(janela, width=20, text="Botão 1")
bt.place(x=270, y=50)
bt["command"] = partial(bt_click, bt)
lb = Label(janela, width=20, text="Teste..................1")
lb.place(x=275, y=10)

janela.mainloop()
