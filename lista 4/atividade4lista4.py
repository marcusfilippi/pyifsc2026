'''4 – Faça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser
cadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado
na tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a
remoção dela e imprima a lista novamente.'''

cidades = []
cidadesdigitadas = int(input("Digite o número de cidades a serem digitadas: "))

x = 0

while x<cidadesdigitadas:
    cidades.append (str(input("Digite o nome da cidade: ")))
    x = x+ 1

x =0

print("Listando...")
while x < cidadesdigitadas:
    print (f" Cidade {x+1}: {cidades[x]}")
    x = x +1

aniquilacao = str(input("Digite o nome de uma cidade a ser aniquilada (lembre-se de escrever igual está na lista):"))

cidades.remove (aniquilacao)

x=0
print("Listando...")
while x < cidadesdigitadas-1:
    print (f" Cidade {x+1}: {cidades[x]}")
    x = x +1
