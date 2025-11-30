#import matplotlib
import matplotlib.pyplot as plt
from math import *
from random import choice, randrange

# matplotlib.__version__


#Primeiro Passo

estudantes = ["João", "Maria", "José"]
estudantes_2 = ["João", "Maria", "José", "Ana"]

notas = [8.5, 9, 6.5]

plt.bar(x = estudantes, height = notas)

plt.show()

estudante = choice(estudantes_2)

#Exercício 1
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

escolha = choice(lista)

#Exercício 2
aleatorio = randrange(100)

#Exercício 3
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

elevado = pow(num1, num2)

print(f"\n resultado: {elevado} \n", )

#Exercicio 4
sort1 = int(input("Quantidade de pessoas participantes: "))
print(f"\n Sorteado: {randrange(sort1)+1} \n")

#Exercicio 5
nome = input("Digite o seu nome: ")
token = randrange(1000, 9998, 2)
print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")

#Exercicio 6
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

fruta1 = frutas[randrange(len(frutas))]
fruta2 = frutas[randrange(len(frutas))]
fruta3 = frutas[randrange(len(frutas))]

print(f"Frutas: {fruta1, fruta2, fruta3}")


#Exercicio 7
numeros = [2, 8, 15, 23, 91, 112, 256]


for i in range(len(numeros)):
    num = sqrt(numeros[i])
    print(f"{num} é inteiro? : ", num//1 == num)

    
#Exercicio 8
raio = int(input("Digite o raio da área: "))

area = pi*pow(raio, 2)
preco = 25*area

print(f"\n Área total: {area:.4f} \n Preço total: {preco:.2f} \n")

