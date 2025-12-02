import matplotlib.pyplot as plt
from math import *
from random import choice, randrange

#Projeto-Funções

'''
def media (nota1, nota2, nota3) -> float:
        Cálculo de média
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

print(notas_atualizadas)'''

#Exercícios
'''
#1
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

lista_tamanho = len(lista)
lista_somada = sum(lista)
lista_maximo = max(lista)
lista_minimo = min(lista)

print(f"\nA lista possui {lista_tamanho} números\n em que o maior número é {lista_maximo} \n e o menor número é {lista_minimo}.\n A soma dos valores presentes nela é igual a {lista_somada}")

#2

lista_tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def tabuada_lista (valor: int = [0]) -> list:
    lista = lista_tabuada
    resultado = list(map(lambda lst: lst*valor, lista))
    return resultado

print(f"\n RESULTADO: {tabuada_lista(7)} \n")

def tabuada (valor: int = [0]) -> int:
    for i in range(11):
        print (f"\n{valor} X {i} = {valor*i}\n")

    return True

print(tabuada(9))


#3
lista_valores_1 = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos (lst: list = [0], mult: int = [0]) -> list:

    Calcula os múltiplos
    
    resultado = []    
    for i in range(len(lst)):
        if lst[i]%mult == 0:
            resultado.append(lst[i])

    return resultado

mult = multiplos(lista_valores_1, 2)

print(f"\n {mult}")

#4
lista_quadrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\n {list(map(lambda lst: lst*lst, lista_quadrada))} \n")
'''


#5
lista_nota_skate = [] 

def gerador_de_media_skate (lst: list = [0]) -> float:

    if len(lst) == 0 : 
        for i in range(len(lst)): lst.append(float(input(f"\n Digite a nota {i+1} do participante: ")))

    if len(lst) >= 3:
        lst.remove(max(lst))
        lst.remove(min(lst))

    return sum(lst)/len(lst)

resultado = gerador_de_media_skate(lista_nota_skate)

print(f"\n Resultado final: {resultado:.2f} \n")

