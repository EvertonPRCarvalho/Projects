from tkinter import*

janela = Tk()

def click_button_one():
    print("Funcionou!")
    lb1["text"]="Funcionou!"
def click_button_two():
    print("Correto!")
    lb2["text"]="Correto!"
    
janela.title("Janela principal")

janela["background"]="light green"

janela.geometry("300x300+200+200")

bt1 = Button(janela, width=20, text="OK", command=click_button_one)
bt1.place(x=100, y=150)

bt2 = Button(janela, width=20, text="Cancel", command=click_button_two)
bt2.place(x=100, y=180)

lb1 = Label(janela, text= "Teste1")
lb1.place(x=50, y=150)

lb2 = Label(janela, text="Teste2")
lb2.place(x=50, y=180)

janela.mainloop()
