'''4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o
resultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4
números ao usuário, chamar a função e exibir o resultado da soma na tela.'''

def soma(lista):
    s = 0
    for elemento in lista:
        s = s + elemento
    return s


l = []
l.append(int(input("Digite um número pra somar: ")))
l.append(int(input("Digite um número pra somar: ")))
l.append(int(input("Digite um número pra somar: ")))
l.append(int(input("Digite um número pra somar: ")))

print("Soma dos elementos da lista: ", soma(l))

