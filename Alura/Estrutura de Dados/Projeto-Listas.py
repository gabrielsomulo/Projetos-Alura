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
'''

'''
#1
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

lista_somada =  [sum(lista_de_listas[i]) for i in range(len(lista_de_listas))]

print(lista_somada)

#2
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista_terceiro_elemento = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]

print(lista_terceiro_elemento)


#3
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_tuplas_nomes = [(i, lista[i]) for i in range(len(lista))]

print(lista_tuplas_nomes)

#4
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

lista_aluguel_apartamento = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento']

print(lista_aluguel_apartamento)

#5
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] 

despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dicionario_despesas = {meses[i]: despesa[i] for i in range(len(meses))}

dicionario_despesas_v2 = dict(zip(meses, despesa))

print(dicionario_despesas_v2)

#6
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

lista_maiores_vendas_2022 = [vendas[i] for i in range(len(vendas)) if vendas[i][0] == '2022' and vendas[i][1]>6000]

print(lista_maiores_vendas_2022)
'''

'''
#7 
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

glicose = [None]*len(glicemia)

estado = ''
for i in range(len(glicemia)):
    if glicemia[i] <= 70:
        estado = 'Hipoglicemia'

    elif glicemia[i] >= 69 and glicemia[i] <= 99:
        estado = 'Normal'

    elif glicemia[i] >= 100 and glicemia[i] <= 125:
        estado = 'Alterada'

    else:
        estado = 'Diabetes'
        
    glicose[i] = estado

lista_resultados_glicemia = list(zip(glicemia, glicose))

print(lista_resultados_glicemia)
'''


'''
#8

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

lista_dados_total = [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]

lista_dados_total.insert(0, ('Id', 'Quantidade', 'Preço', 'Total'))

print(lista_dados_total)
'''

#9
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

lista_estados = ['SP', 'MG', 'RJ', 'ES']

'''lista_estados_contagem = {lista_estados[i]: estados.count(lista_estados[i]) for i in range(len(lista_estados))}

print(lista_estados_contagem)'''

#10
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

dicionario_funcionarios = {lista_estados[i]: [funcionarios[j][1] for j in range(len(funcionarios)) if funcionarios[j][0]==lista_estados[i]] for i in range(len(lista_estados))}

print(dicionario_funcionarios)

dicionarios_funcionarios_soma = {lista_estados[i]: sum(dicionario_funcionarios[lista_estados[i]]) for i in range(len(lista_estados))}

print(dicionarios_funcionarios_soma)

