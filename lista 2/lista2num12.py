#12 – Implemente um programa que funcione como uma calculadora entre dois números
#informados. Seu programa deve exibir um menu que solicite a operação a ser realizada
#entre dois números (adição, subtração, divisão e multiplicação) e os dois números a
#serem utilizados no cálculo. Se o usuário digitar uma opção inválida, deve alertar o
#usuário e exibir o menu novamente. Utilize um menu, como o abaixo, no seu programa:
#Menu
#-------
#1 – Adição
#2 – Subtração
#3 – Divisão
#4 – Multiplicação
#0 - Sair
#Digite a opção:

sinal = int(input("Menu\n-------\n1 – Adição\n2 – Subtração\n3 – Divisão\n4 – Multiplicação\n0 - Sair\nDigite a opção: "))

if sinal == 0:
   print ("Você saiu da calculadora")


else:
 num1 = float(input("Digite seu primeiro número: "))

 num2 = float(input("Digite seu segundo número: "))

 if sinal == 1:
      resul = (num1 + num2)
 elif sinal == 2:
     resul = (num1-num2)
 elif sinal == 3:
     resul = (num1/num2)
 else:
     resul = (num1*num2)

 print ("O resultado da sua conta é:", resul)