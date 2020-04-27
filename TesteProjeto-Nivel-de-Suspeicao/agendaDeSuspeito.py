
'''ESTÁ FUNCIONANDO'''
def agendaDeSuspeito(nomedeContato):
    contatos_em_agenda = []
    for posicao, string in enumerate(agenda):
        separando = ('%s' % agenda[posicao].split(':'))
        y = separando.find('%s' % nomedeContato)

        if y != -1:
            numeros = list(('%s'% (string[string.find(':') + 1:])).split(','))
            separado = string.split(',')

            for i in range(len(separado)):
                contatos_em_agenda += str(numeros[i])
        else:
            print('Contato não encontrado!')

