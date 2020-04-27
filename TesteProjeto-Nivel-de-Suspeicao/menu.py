'''FUNCIONANDO'''


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
