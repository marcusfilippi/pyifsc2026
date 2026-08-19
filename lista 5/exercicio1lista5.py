'''1 – Crie um programa com uma função para calcular a média aritmética simples entre 3
notas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.'''

def media(a, b, c):
    m = (a+b+c)/3
    return m

v1 = float(input("Digite a primeira nota: "))
v2 = float(input("Digite a segunda nota: "))
v3 = float(input("Digite a terceira nota: "))

r = media(v1, v2, v3)

print (f"A sua média é: {r}")