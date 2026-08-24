'''2 – Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
exiba os números do menor para o maior.'''

lista =[]

i = 0

while i<15:
    num = int(input("Digite o número que você quer adicionar na cartela (entre 1 e 75): "))
    if num<=75 and num>=1:
        lista.append(num)
    i = i +1

lista = sorted(lista)

print (lista)