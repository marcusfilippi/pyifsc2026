#6 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da
#tabuada, em vez de começar iniciar no 1 e terminar no 10.

num = int(input("Escreva um número:"))

i = int(input("Escreva de onde você quer que sua tabuada comece:"))

x = int(input("Escreva aonde você quer que sua tabuada termine:"))

if i<x:
    while i <= x:
      resul = num*i
      msg = f"{num} X {i} = {resul}"
      print (msg)
      i = i +1

else: 
    while i >= x:
      resul = num*i
      msg = f"{num} X {i} = {resul}"
      print (msg)
      i = i -1