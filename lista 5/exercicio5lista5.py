'''5 – Programe um algoritmo com mais algumas funções úteis para a manipulação de listas
numéricas:
a) uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso
possua um ou mais elementos;
b) uma função que receba uma lista e retorne o maior valor;
c) uma função que receba uma lista e retorne o menor valor;
d) uma função que receba uma lista e retorne o valor médio.
As funções dos itens b, c e d devem retornar -1 caso a lista esteja vazia. No seu
programa principal, crie duas listas (uma vazia e outra com alguns elementos) e teste
(comprove) o funcionamento de cada uma das funções.'''

def listafalsa(lista):
    
    if len(lista) == 0:
        falsa = True
    else:
        falsa = False
        
    return falsa
    
    
def listamaior(lista):
    if len(lista) == 0:
        return -1
    else: 
        result = max(lista)
        return result
    
def listamenor(lista):
    if len(lista) == 0:
        return -1
    else: 
        result = min(lista)
        return result
    
def listamedio(lista):
    if listafalsa(lista):
        return -1
    else:
        s = 0
        for elemento in lista:
            s = s + elemento
        s = s / len(lista)
        return s
    
    
listavazia = []

listacheia = [2, 4, 4, 6]

print ("lista vazia")

print (f"A lista está vazia? {listafalsa(listavazia)}")

print (f"Maior número da lista {listamaior(listavazia)}")

print (f"Menor número da lista {listamenor(listavazia)}")

print (f"Média aritmetica da lista {listamedio(listavazia)}")

print ("lista cheia")

print (f"A lista está vazia? {listafalsa(listacheia)}")

print (f"Maior número da lista {listamaior(listacheia)}")

print (f"Menor número da lista {listamenor(listacheia)}")

print (f"Média aritmetica da lista {listamedio(listacheia)}")
