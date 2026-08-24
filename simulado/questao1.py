'''1 – Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando
é divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.'''

ano = int(input("Digite o ano que você quer conferir se é bissexto: "))

if (ano%4==0) and (ano%100!=0):
    print ("Este ano é bissexto!")

elif (ano%400==0):
    print ("Este ano é bissexto!")

else:
    print ("Este ano não é bissexto!")