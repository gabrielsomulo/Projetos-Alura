from random import randint

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

notas = [[1,2,3], [4,5,6], [7,8,9], [0,9,8], [7,6,5]]

def gera_codigo():
    return str(randint(0,999))

def gera_media(notas_estudantes: list=[0]):
    return sum(notas_estudantes)/len(notas_estudantes)

codigo_estudantes = []

medias_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

nomes_estudantes = [nome[0] for nome in codigo_estudantes]

notas_medias_estudantes = [round(gera_media(nota), 1) for nota in notas]

print(codigo_estudantes)

print(nomes_estudantes)

print (notas_medias_estudantes)

estudantes_dados = list(zip(nomes_estudantes, notas_medias_estudantes))

print(estudantes_dados)

candidatos = [ estudante[0] for estudante in estudantes_dados if estudante[1] >= 8]

print(candidatos)

