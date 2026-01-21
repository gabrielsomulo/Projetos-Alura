'''
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
else:
    print(resultado)
finally:
    print("Hello World!!!")
'''



def media(lista: list=[0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista

    lista: list, default[0]
        Lista com as notas para calcular a média
        return calculo: float
        Média calculada
    '''
    try:
        calculo = sum(lista) / len(lista)

        if len(lista)>4:
            raise ValueError("A lista de notas deve possuir dez elementos \n")
        
    except TypeError:
        print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos! \n")
        
    except ValueError as e:
        print(e)

    else:
        print("Leitura Correta!!! \n")  
        return calculo   
    finally:
        print("Operação finalizada \n")
        

numeros1 = [1,2,3,4,5,6,7]

numeros2 = [1,2,"1"]

numeros3 = [1,2,3]

print(media(numeros1))
print(media(numeros2))
print(media(numeros3))