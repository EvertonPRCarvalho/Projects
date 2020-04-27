from FileHelper import lerArquivo

agenda = lerArquivo("agendasuspeitos.txt")
nomes = []
numeros = []

listaAgenda = []  # Aqui os elementos de agenda serão uma lista.
chamadas = []
'''Aqui foi feito apenas uma reorganização da lista para que cada elemento da agenda passasse a ser uma nova lista.'''



def organizaListas():
    for i, e in enumerate(agenda):
        x = [e]
        if x not in listaAgenda:
            listaAgenda.append(x)

            if e == 'chamadas':
                break

            elif e != 'agenda': # Nada mais irei fazer no próximo passo do que apontar os nomes e numeros dentro da agenda
                separa = e.split(':')
                separando = str(separa[0]).split('-')
                nomes.append(separando[0])
                numeros.append(separando[1])

organizaListas()


def agendaDeSuspeito(nomedeContato):
    contatos_em_agenda = []
    for posicao, string in enumerate(agenda):
        separando = ('%s' % agenda[posicao].split(':'))
        y = separando.find('%s' % nomedeContato)

        if y != -1:
            numeros = list(('%s' % (string[string.find(':') + 1:])).split(','))
            separado = string.split(',')

            for i in range(len(separado)):
                contatos_em_agenda += str(numeros[i])
        else:
            print('Contato não encontrado!')


def pesquisaNome(nome):
    for temp in agenda:
        if nome not in temp:
            return 'Nome não encontrado! Tente novamente.'
        else:
            return nome


'''Aqui apenas separei os elementos da lista de contato de uma pessoa.'''


def mostraAgenda(nomedeContato):
    for posicao, string in enumerate(agenda):
        separando = ('%s' % agenda[posicao].split(':'))

        if separando.find('%s' % nomedeContato) != -1 and nomedeContato in nomes:
            '''O que será feito a seguir se trata de manipulação de string ( do nome em questão)'''
            nome = str(string[:string.find('-')])
            edicao_nome = (nome[:1].upper()) + nome[1:]  # O que fiz aqui foi apenas deixar a primeira letra do nomeContato maiúscula.
            print('Agenda do suspeito %s:' % edicao_nome)
            numeros = list(('%s\n' % (string[string.find(':') + 1:])).split(','))
            separado = string.split(',')

            for i in range(len(separado)):
                print(numeros[i])
            break
    else:
        print('Contato não encontrado!')


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


def nomeNumero():  # Aqui criar uma lista com os nomes ligados ao seu respectivo número.

    for linha in agenda:
        if linha != "agenda" and linha != "chamadas":
            pedacos = linha.split(":")
            # print(pedacos)
            dadosDono = str(pedacos[0]).split("-")
            nomes.append(dadosDono[0])
            numeros.append(dadosDono[1])

        if linha == "chamadas":
            break
    return nomes, numeros


def listarAgendaDeSuspeitos(listaNmes, listaNumeros):
    temp = 0
    lista = []
    for i, e in enumerate(listaAgenda):
        if e != ['agenda'] and e != ['chamadas']:
            lista.append(e)
            for cont in e:
                separa = cont.split(':')
                x = separa[0].split('-')
                nomes.append(x[0])
                numeros.append(x[1])
            if numeros[temp] in numeros:
                print(numeros[temp])
                print(numeros)
            temp += 1

        if e == ['chamadas']:
            break


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

    return ('%s: %s' % (edicao_nome, nomes_da_lista))


def passar_por_nomes(opcao):
    lista = []
    for i, e in enumerate(nomes):
        a = listarRelacaoEntreSuspeitos(e)
        lista.append(a)
        if opcao == 2:
            print(listarRelacaoEntreSuspeitos(e))
    return lista


def contatosEmAgenda(opcao):
    lista = passar_por_nomes(opcao)
    for e in range(len(lista)):
        for i in range(len(nomes)):
            if nomes[e] in lista[i] and nomes[i] in lista[e]:
                print('%s <-> %s' % (nomes[e], nomes[i]))
                break


def criarListaChamadas():

    for i in range(len(agenda)):
        if agenda[i] == 'chamadas':
            lista_de_chamadas = agenda[i:]  # Aqui é feita a fatia da lista agenda. Pegando da lista agenda de chamadas até seu último elemento, pois não há outra classificação de elemento em agenda alem de agenda e chamadas.
            break
    '''O proximo passo será apenas para criar a lista chamadas'''
    for posicao in range(len(lista_de_chamadas) - 1):
        separa = (lista_de_chamadas[posicao + 1]).split(',')
        separou = str(separa[0]).split(':')
        junta_tudo = separou + separa


        chamadas.append(list(junta_tudo[1:]))
        # Como tudo está ordenado de uma mesma forma posso retirar os nomes-numeros correspondentes a cada lista em chamadas.
                                        # Ex.: O nome João e seu número estão alocados em uma mesma posição dentroo da lista nomes e numeros respectivamente. O
    return chamadas                     # O mesmo ocorrerá para a lista que contém as chamadas de João, ou seja, esta lista de chamadas de João estára na posicao em que seu nome estiver.



def niveldeSuspeicao(numero_de_chamadas):
    lista_de_chamadas = criarListaChamadas()
    print('Lista de reciprocidade de chamadas desejadas:')
    print('----------------------------------------------')
    for i, e in enumerate(numeros):
        for x in range(len(numeros)):
            if (chamadas[x]).count(e) >= numero_de_chamadas:
                print('%s <-> %s (Nível alto de suspeicao)'% (nomes[i], nomes[x]))
                break
        else:
            print(('%s <-> %s '% (nomes[i], nomes[x])))
            break

def menu():
    try:
        while True:
            print('''
    ==========================================
    PESQUISA DE SUSPEITOS EM AGENDA TELEFONICA
    ==========================================
    
    1 - Ver agenda de um suspeito 
    2 - Listar agendas apenas com suspeitos incluídos
    3-  Visualizar reciprocidade
    4 - Visualizar contatos com altos nível de suspeição
    
    5 - Sair
    ''')

            opcao = int(input('Digite uma das opções acima: '))
            if opcao == 1:
                nome = str(input('Digite o nome do suspeito para obter sua agenda: '))
                mostraAgenda(nome)
            elif opcao == 2:
                passar_por_nomes(opcao)
            elif opcao == 3:
                contatosEmAgenda(opcao)
            elif opcao == 4:
                n = int(input('Informe a quantidade de chamadas desejadas: '))
                niveldeSuspeicao(n)
            elif opcao == 5:
                print('\n' * 50 + 'VOCÊ SAIU DO PROGRAMA!' + '\n' * 2)
                print('''                 Polícia Federalis do Brasilis
                009º Vara / Combate ao crime organizado
                    Operação ficha limpa''')
                break
    except:
        print('Erro')
        menu()
