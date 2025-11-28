#Projeto-Funções

def media (nota1, nota2, nota3) -> float:
    '''
        Cálculo de média
    '''
    calculo = (nota1+nota2+nota3)/3
    return calculo

print (media(1,2,3))

notas = [1,2,3,4,5,6,7,8,9]

def media_com_lista (lista: list=[0]) -> float:
    calculo = sum(lista)/len(lista)
    return calculo

print(media_com_lista(notas))

subtracao_lambda  = lambda media_valor : media_valor -1

print(subtracao_lambda(media(1,2,3)))

#notas
notas_1 = [1,1,2,3,46,78,1.2]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas_1)

notas_atualizadas = list(notas_atualizadas)

print(notas_atualizadas)