#Projeto-Funções

def media (nota1, nota2, nota3):
    calculo = (nota1+nota2+nota3)/3
    return calculo

print (media(1,2,3))

notas = [1,2,3,4,5,6,7,8,9]

def media_com_lista (lista):
    calculo = sum(lista)/len(lista)
    return calculo

print(media_com_lista(notas))

