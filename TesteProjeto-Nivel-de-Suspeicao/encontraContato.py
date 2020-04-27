'''Essa função fará a busca pelo nome inserido na busca.'''


def encontraContato(nomedeContato):
    for posicao, string in enumerate(agenda):
        separando = ('%s' % agenda[posicao].split(':'))
        y = separando.find('%s' % nomedeContato)
        if y != -1:
            print('Contato encontrado!')
            return agenda[posicao]
            break
    else:
        print('Contato não encontrado!')
