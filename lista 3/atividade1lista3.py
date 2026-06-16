#1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
#programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
#apresentar apenas as idades que forem maiores ou iguais a 16.

idades = [0,0,0,0,0,0]

x = 0
while x<=5:
   idades[x] = int(input("Idade: "))
   x += 1

x= 0
while x<=5:
   if idades[x]>=16:
      print (idades[x])
   x += 1
