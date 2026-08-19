'''3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu
programa principal deve solicitar a altura e o raio do cilindro em metros, chamar a função
e exibir o resultado na tela. '''

import math

def volumecilin(a, r):
    v = math.pi * a * (r*r)
    return v

alt = float(input("Digite a altura do cilindro em metros: "))
raio = float(input("Digite o raio do cilindro em metros: "))

resul = volumecilin(alt, raio)

print (f"A area do seu cilindro é {resul}")