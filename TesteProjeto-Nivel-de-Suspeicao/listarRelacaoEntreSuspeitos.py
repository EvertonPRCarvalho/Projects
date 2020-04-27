def listarRelacaoEntreSuspeitos(nomedeContato):
    nomes_da_lista = ''
    for posicao, string in enumerate(agenda):
        separando = ('%s' % agenda[posicao].split(':'))
        separado = separando.split(',')

        if separando.find('%s' % nomedeContato) != -1:
            nome = str(string[:string.find('-')])
            edicao_nome = (nome[:1].upper()) + nome[
                                               1:]  # O que fiz aqui foi apenas deixar a primeira letra do nomeContato maiúscula.
            numero_s = list(('%s' % (string[string.find(':') + 1:])).split(','))

            for i in range(len(numeros)):
                for x in range(len(numero_s)):
                    if numeros[i] == numero_s[x]:
                        nomes_da_lista += ('%s ' % nomes[i])

            break
    return('%s: %s' % (edicao_nome, nomes_da_lista))