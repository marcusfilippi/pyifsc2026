'''2 – Crie um programa que registrará as notas de um estudante. O programa deve
perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
notas e, ao final, exibir todas as notas digitadas na tela.'''

notas = []

notasdigitadas = int(input("Digite o número de notas a serem digitadas: "))

x = 0

while x<notasdigitadas:
    notas.append (input("Digite a nota: "))
    x = x+ 1

x = 0

while x < notasdigitadas:
    print (f" Nota {x+1}: {notas[x]}")
    x = x +1

