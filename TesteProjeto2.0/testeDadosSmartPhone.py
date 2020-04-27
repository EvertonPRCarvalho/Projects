from testeControlador import Controlador

class DadosSmartphone(Controlador):
    def __init__(self, nome='', contatos='', chamadas=''):
        Controlador.__init__(self, listaDadosSmartphone=list())
        self.__nome_do_suspeito = nome
        self.__contato_do_suspeto = ''
        self.__agenda_do_suspeito = contatos
        self.__chamadas = chamadas
        self.__dados_smartphone_do_elemento = dict()
        
    def adicionar_elemento_lista_dadosSmartphone(self):
           pass
        
    def nome_numero_agenda(self):#Usar o método seek() para obter a posição do ponteiro
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
   
            
#dados = DadosSmartphone()
#dados.abrirArquivo('agenda.txt')
#dados.nome_numero_agenda()
#dados.get_listaDadosSmartphone()
