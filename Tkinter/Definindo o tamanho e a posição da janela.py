import tkinter as tk

#Agora irei creiar uma instância 'janela'.
janela = tk.Tk() #tk é o nome da biblioteca (por isso foi colocado 'import tkinter AS tk' e Tk é o nome da classe).
janela.title('Janela principal') #A função title é reponsável por nomear o título a instância, neste caso, janela.

janela["bg"]        = "lightblue"#Para mundar a cor de fundo alteramos a chave bg do dicionário janela (tratando a janela com um dicionário).
janela["background"]="light blue"

#DEFININDO LARGURA, ALTURA E POSIÇÃO DA JANELA PRINCIPAL (CONTEINER PRINCIPAL)
#LaruraxAltura+Distancia da esquerda+Distancia do topo do vídeo
#Ex.: 300x300+100+100
janela.geometry("720x300+100+100")#A função geometry permite alterar o tamanho e a posição da janela (do conteiner principal)
janela.mainloop() #Essa é a janela principal ou um conteiner (ainda sem widget).
#A função mainloop é um laço de repetição até algum evento acontecer.
