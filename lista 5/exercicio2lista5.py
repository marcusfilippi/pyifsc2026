'''2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou
ímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o
resultado na tela.'''

def imparpar(a):
    p = a%2
    if p == 0:
        s = ("é par")
        
    else:
        s = ("é impar")
        
    return s

num = int(input("Digite o número que vocẽ quer ver se é ímpar ou par: "))

r = imparpar(num)

print (r)