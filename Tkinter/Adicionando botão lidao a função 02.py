from functools import partial
from tkinter import*

def bt_click(botao):
    print(botao["text"])
    
janela = Tk()
janela.title("Janela Inicial")
janela.geometry("300x300+500+200")
janela["background"]="orange"
lb = Label(janela, width=20, text="Olá!")
lb.place(x=101, y=190)
bt1 = Button(janela, width=20, text="Botão 1")
bt1.place(x=100, y=100)
bt1["command"] = partial(bt_click,bt1)#o partial chama a função bt_click e o bt1 assume o botao da função.
bt2 = Button(janela, width=20, text="Butão 2")
bt2.place(x=100, y=150)



janela.mainloop()
