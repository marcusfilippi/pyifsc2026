#Escreva um programa que leia números inteiros do teclado. O programa deve ler os
#números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de
#números digitados, assim como a soma e a média aritmética.

i=0
somanumeros = 0
num=1

while num!=0:
         num = int(input("Escolha um número: "))
         if num!=0:
          somanumeros = num + somanumeros
          i = i +1

media = somanumeros/i

print (f"O total de números digitados foi {i}, a soma deles foi {somanumeros}, e a média aritmética deles foi {media}")