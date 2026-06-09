#3 – Faça um programa que exiba na tela a contagem iniciando no número 1 e indo até um
#número informado pelo usuário. Considere que a contagem pode ser até um número
#positivo ou até um número negativo.

import time

num = int(input("Escreva um número"))


 
if num>0:
    i = 1
    while i<=num:
        print (i)
        i = i +1
        time.sleep(1) 

else:
    i = -1
    while i>=num:
        print (i)
        i = i-1
        time.sleep(1) 