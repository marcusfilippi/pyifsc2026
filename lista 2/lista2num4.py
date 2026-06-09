#4 – Implemente um algoritmo que exiba na tela os números pares de 0 até um número
#digitado pelo usuário. Dica: você pode utilizar o operador módulo (%) ou contar de 2 em 2

import time

num = int(input("Escreva um número:"))

i=0

while i<=num:
       print(i)
       i = i +2
       time.sleep(0.5)
       