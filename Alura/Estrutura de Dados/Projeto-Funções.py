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

'''
#5
lista_nota_skate = [1, 2, 3] 

def gerador_de_media_skate (lst: list = [0]) -> float:
    match len(lst):
        case 0:
            for i in range(5): lst.append(float(input(f"\n Digite a nota {i+1} do participante: ")))
            
        case 1:
            lst.append(min(lst)-1)
            lst.append(max(lst)+1)
            
        case 2:
            lst.append(min(lst)-1)
            
    lst.remove(max(lst))
    lst.remove(min(lst))

    return sum(lst)/len(lst)

resultado1 = gerador_de_media_skate(lista_nota_skate)

#resultado2 = gerador_de_media_skate([30, 2.3, 78.76, 34.456, 98, 578])

print(f"\n Resultado final: {resultado1:.2f} \n")

#print(f"\n Resultado final: {resultado2:.2f} \n")
'''

#6
lista_nota_escola = [6.5, 8.4, 5.4, 7.9]

def resultados_de_notas(lst: list[float]) -> tuple[float, float, float, str]:
    maior = max(lst)
    menor = min(lst)
    media = sum(lst)/len(lst)
    avaliacao = "reprovado" if media < 7 else "aprovado"
    return maior, menor, media, avaliacao

maior, menor, media, avaliacao = resultados_de_notas(lista_nota_escola)

print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {avaliacao}")

#7
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

def ajustar_nomes(lst_nome: list[str], lst_sobrenome: list[str]) -> list[str]:
    nomes = list(map(lambda nome, sobrenome: nome.capitalize() + " " + sobrenome.capitalize(), lst_nome, lst_sobrenome))
    return nomes

lista_nomes_completos = ajustar_nomes(nomes, sobrenomes)

for i in range(len(lista_nomes_completos)): print(f"\n Nome completo: {lista_nomes_completos[i]}")


