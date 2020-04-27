from tkinter import*

#Um gerenciador de layout define a organização dos widget dentro de um container

janela = Tk()
janela.title("Pagina inicial")
janela["bg"]="light blue"

lb = Label(janela, text="Fala galera!")#É o child. Tem se que informar onde ele está contido (o parent).
#Sempre que for cirado um widget deve-se colocá-lo dentro de um conteiner. Neste cado text é o widget e janela o conteiner
#Foi criada a variável lb recebendo o Lable para aplicar o layout
lb.place(x=100, y=100)#Devi-se definir as coordenas x e y para a exibição do widget numa dada posição


#Definindo a geometria da janela
janela.geometry("300x300+200+200")

#Com a função place os widget são posicionados conforme suas coordenadas x e y
#Com a função pack empacota os widget na horizontal ou vertical
#Com a função grid os widget são inseridos num sistema de células de uma tabela

janela.mainloop()
