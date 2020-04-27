from tkinter import*

janela=Tk()
def bt_click(): #Definindo função para interagir com o botão
    print("bt_click")
bt = Button(janela, width=20, text="OK", command=bt_click)#Criação do botão. Devemos definir o parent do child botão, a largura e a mensagem
#desejada respectivamente (essa ordem vale para este exemplo).
#O parâmetro command é responsável por fazer a ligação entre o botão e a função bt_click toda vez que esse for precionado
#Sendo assim, oa instância Botton invoca a função bt_click toda vez que o botão for precionado
bt.place(x=100, y=100)
lb = Label(janela, text="Teste")
lb.place(x=100, y=150)

janela.title("Janela principal")

janela["background"] = "light blue"

janela.geometry("400x320+200+200")

janela.mainloop()
