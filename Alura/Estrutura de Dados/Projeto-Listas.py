from random import randint

'''estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

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
'''

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Media Final", "Situação"]

cadastro = {coluna[i]: lista_completa[i+1] for i  in range(len(coluna))}

print(cadastro)

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]

print(cadastro)