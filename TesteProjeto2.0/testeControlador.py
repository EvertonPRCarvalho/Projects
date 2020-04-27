from testeDadosSmartPhone import*

class Controlador(DadosSmartphone):
    def __init__(self, listaDadosSmartphone=list()):
        self.__listaDadosSmartphone = listaDadosSmartphone
        self.__lista_de_agenda_no_smartphone = list()
    
    def get_listaDadosSmartphone(self):
        return self.__listaDadosSmartphone
    def set_listaDadosSmartphone(self, dados):
        self.__listaDadosSmartphone.append(dados)

    def get_lista_de_agenda_no_smartphone(self):
        return self.__lista_de_agenda_no_smartphone
    def set_lista_de_agenda_no_smartphone(self, dados):
        self.__lista_de_agenda_no_smartphone.append(dados)

    def abrirArquivo(self, arquivo):
        self.__arquivo = arquivo
        with open(self.__arquivo, 'r') as arquivoLer:
           self.set_listaDadosSmartphone(arquivoLer.read())

    def Nome_Numero_Agenda(self):#Usar o método seek() para obter a posição do ponteiro
        arquivo_completo = self.get_listaDadosSmartphone()
        
        for dados_elemento in arquivo_completo[0].split():

            agenda = None #Aqui ficará armazenada a agenda do suspeito até que o loop vá para outro suspeto dentro do arquivo agenda.txt
            chamdas = list()#Acontecerá algo similar nesta variável, pois aqui ficará sua lista de chamadas.
            
            if dados_elemento == 'agenda':
                continue
            elif dados_elemento != 'agenda' and dados_elemento != 'chamadas':
                print('Nome do suspeito: '+dados_elemento.split(':')[0].split('-')[0]) #Aqui o que fiz foi pegar o nome do suspeito para adicionar na lista de nomes
                print('Numero do suspeito: '+dados_elemento.split(':')[0].split('-')[1])
                print(('Agenda de %s: '+dados_elemento.split(':')[1]) % dados_elemento.split(':')[0].split('-')[0])
                agenda = dados_elemento.split(':')[1].split(',')
                print(agenda)
                print()
                
            elif dados_elemento == 'chamadas':
                break
            

agenda = Controlador()
agenda.abrirArquivo('agenda.txt')
agenda.nome_numero_agenda()
#agenda.set_listaDadosSmartphone(['agenda\n', 'joao-81987043487:81123456789,81987654321,11111111111,11222222222,8130221234\n', 'pedro-11111111111:81987043487,87987647389,11333333333,8234567896,11222222222\n', 'antonio-11222222222:11111111111,81988255065,2134321234\n', 'chamadas\n', 'joao:11111111111,81123456789,11222222222,8130221234,11111111111,11111111111,11222222222,81987654321\n', 'pedro:81987043487,8130221234,8130221234,8130221234,81987043487,81987043487,81987043487,81987043487\n', 'antonio:81988255065,2134321234,81988255065,8134323184,8130834316,11111111111,11111111111\n'])
#print(agenda.get_listaDadosSmartphone())

