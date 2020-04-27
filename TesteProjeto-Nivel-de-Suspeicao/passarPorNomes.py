'''ESSA FUNÇÃO IRÁ PERCORRER A LISTA DE NOMES E APLICAR À FUNÇÃO listarRelacaoEntreSuspeitos.
ESSA FUNÇÃO TAMBÉM ME RETORNA UMA LISTA CONTENDO A RELAÇÃO ENTRE AGENDA DE SUSPEITO E SEU(S) RESPECTIVO(S)'''

def passar_por_nomes():
    lista = []
    for i, e in enumerate(nomes):
        a = listarRelacaoEntreSuspeitos(e)
        lista.append(a)
        print(listarRelacaoEntreSuspeitos(e))
    return lista
