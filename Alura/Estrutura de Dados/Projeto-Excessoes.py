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

#1
try:
    valor1 = float(input("Insira o valor 1: "))
    valor2 = float(input("Insira o valor 2: "))

    try:
      print(valor1/valor2)
    except ZeroDivisionError as e:
        print(f"Erro - {e}")

except ValueError as e:
    print(f"Erro - {e}")

#2
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

nome = str(input("Insira o nome desejado: "))

try:
    nome_buscado = idades[nome]
    print(nome_buscado)
except KeyError:
    print("Nome não achado")


#3
def conversor_float(lista_int = list[0]) -> list:
    try:
        lista_convertida = [float(lista_int[i]) for i in range(len(lista_int))]
        
        return lista_convertida

    except TypeError:
        print("\n A variável precisa ser uma lista de inteiros. \n")

    except ValueError:
        print("\n Os valores dentro da lista precisam inteiros ou floats. \n")

    finally:
        print("\n Fim da execução da função. \n")

print(conversor_float([3, 1, 2]))


#4
def misturar_listas(lista_1 = list[0], lista_2 = list[0]) -> list:
    try:
        if(len(lista_1) != len(lista_2)):
            raise IndexError

        lista_misturada = list(zip(lista_1, lista_2))

        try:
            lista_soma = [(lista_misturada[i][0], lista_misturada[i][1], lista_misturada[i][0]+lista_misturada[i][1]) for i in range(len(lista_misturada))]

            return lista_soma
        
        except TypeError:
            print('As listas devem conter apenas valores inteiros.')

    except IndexError:
        print('A quantidade de elementos em cada lista é diferente.')


lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]

lista_misturada_soma = misturar_listas(lista1, lista2)

print(lista_misturada_soma)


#5
gabarito = ['D', 'A', 'B', 'C', 'A']

def gerar_nota(lista_alunos = list[0]) -> list:
    try:
        alternativa = ''
        lista_notas = [0]*len(lista_alunos)

        for i in range(len(lista_alunos)):
            if(len(lista_alunos[i])!=len(gabarito)): 
                raise IndexError
    
            for j in range(len(gabarito)):
            
                if (lista_alunos[i][j] not in gabarito): 
                    alternativa = lista_alunos[i][j]
                    raise ValueError

                if (lista_alunos[i][j]==gabarito[j]):
                    lista_notas[i] += 1
    
    except IndexError:
         print("Quantidade de respostas não condizentes com a quantidade do gabarito")

         return None
    
    except ValueError:
        print(f"A alternativa {alternativa} não é uma opção de alternativa válida")

        return None

    else:
        return lista_notas


testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

testes_com_erro = [['A','D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

print(gerar_nota(testes_com_erro))


#6
pontuacoes = [',', ';', '!', '?']

palavras = []

lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

def leitor_de_palavras(lista_palavras = list[0]) -> bool:
    achou = False

    try:
        for i in range(len(lista_palavras)):
            for j in range(len(lista_palavras[i])):
                if (lista_palavras[i][j] in pontuacoes): 
                    palavras.append(lista_palavras[i])
                    achou = True
            
        if (achou): raise ValueError
        
        return True
    
    except ValueError:
         print(f"O texto apresenta pontuações na(s) palavra(s) \"{palavras}\".")

         return False

print(leitor_de_palavras(lista_tratada))
'''

#7
posicoes_t = []

def divide_colunas(lista_pressao = list[0], lista_temperatura = list[0]) -> list:
    achou_zero = False
    lista_completa = []
    try:
        if(len(lista_pressao)!=len(lista_temperatura)): raise IndexError

        for i in range(len(lista_pressao)):

            if(lista_temperatura[i]==0):
                posicoes_t.append(i+1)
                achou_zero = True

            else:
                pressao = lista_pressao[i]
                temperatura = lista_temperatura[i]

                lista_completa.append((pressao, temperatura, pressao/temperatura))

        if (achou_zero): raise ZeroDivisionError

        return lista_completa
    
    except IndexError:
        print("As listas contêm tamanhos diferentes")
        
        return None

    except ZeroDivisionError:
        print(f"A lista de temperatura contêm valores iguais a zero na(s) posição(ões): ")

        return posicoes_t

pressoes = [60, 120, 140, 0, 180]

temperaturas = [1, 5, 30, 35, 12]

print(divide_colunas(pressoes, temperaturas))