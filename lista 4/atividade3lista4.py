'''3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
deve fazer isso de duas formas: com while e com for.
Exibição com while:
Nota: 9.0
Nota: 7.5
Nota: 8.0
Exibição com for:
Nota: 9.0
Nota: 7.5
Nota: 8.0'''

notas = []

notasdigitadas = int(input("Digite o número de notas a serem digitadas: "))

x = 0

while x<notasdigitadas:
    notas.append (float(input("Digite a nota: ")))
    x = x+ 1

x = 0

print ("Exibição com While: ")
while x < notasdigitadas:
    print (f" Nota {x+1}: {notas[x]}")
    x = x +1



print("Exibição com For:")
for x in range(len(notas)):
    print(f"Nota {x+1}: {notas[x]}")