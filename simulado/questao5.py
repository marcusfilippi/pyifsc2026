'''5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
• 1 – Adição;
• 2 – Subtração;
• 3 – Multiplicação;
• 4 – Divisão;
• 0 – Sair.
Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.'''

while True:
    print ("1-Adição")
    print ("2-Subtração")
    print ("3-Multiplicação")
    print ("4-Divisão")
    print ("0-Sair")

    opcao = int(input("Digite a opção: "))

    if opcao==0:
        break
    elif opcao ==1:
        n1 = float(input("Digite um numero"))
        n2 = float(input("Digite outro numero"))

        resul = n1+n2

        print (resul)

    elif opcao ==2:
        n1 = float(input("Digite um numero"))
        n2 = float(input("Digite outro numero"))

        resul = n1-n2

        print (resul)
    
    elif opcao ==3:
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero"))

        resul = n1*n2

        print (resul)

    elif opcao ==4:
        n1 = float(input("Digite um numero"))
        n2 = float(input("Digite outro numero"))

        resul = n1/n2

        print (resul)

