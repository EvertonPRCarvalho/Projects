
'''FUNCIONANDO'''

def mostraAgenda(nomedeContato):
    for posicao, string in enumerate(agenda):
        separando = ('%s' % agenda[posicao].split(':'))
        y = separando.find('%s' % nomedeContato)

        if y != -1:
            '''O que será feita a seguir se trata de manipulação de string (nome)'''
            nome = str(string[:string.find('-')])
            edicao_nome = (nome[:1].upper()) + nome[1:]  # O que fiz aqui foi apenas deixar a primeira letra do nomeContato maiúscula.
            print('Agenda do suspeito %s:' % edicao_nome)
            numeros = list(('%s\n' % (string[string.find(':') + 1:])).split(','))
            separado = string.split(',')
            a = len(separado)

            for i in range(a):
                print(numeros[i])

            break
    else:
        print('Contato não encontrado!')
