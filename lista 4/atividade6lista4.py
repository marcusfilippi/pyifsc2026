'''6 – Elabore um programa que funcionará como um cadastro notas de um estudante. Seu
programa deve permitir que notas sejam cadastradas ou removidas (através do seu
índice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também
deve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve
avisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para
calcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6
e reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação
com o seu programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
0 - Sair
Opção:'''

notas = []

while True:
    print("Notas:")
    print("----")
    print("1 – Cadastrar")
    print("2 – Excluir")
    print("3 – Listar")
    print("4 – Calcular média")
    print("0 – Sair")

    opcao = int(input("Opção: "))

    if opcao == 0:
        break

    elif opcao == 1:
       notas.append (float(input("Digite a nota a ser adicionada: ")))

    elif opcao == 2:
        if len(notas) == 0:
           print("Não há notas cadastradas")
        else:
            notaaniquilada = int(input("Digite o número da nota que que você quer excluir: "))
            if notaaniquilada>= 0 and notaaniquilada <len(notas):
                notas.pop(notaaniquilada)
                print(f"Tem {notaaniquilada}, excluindo...")
            else:
                 print(f"Não tem {notaaniquilada}, não dá pra excluir.")


    elif opcao == 3:
        if not notas:
            print ("Sua lista de notas está vazia.")
        else:
            print("Listando...")
            print (notas)
            print ("Fim da lista.")
    
    elif opcao ==4:
         soma = sum(notas)
         quantnotas = len(notas)
         media = soma/quantnotas

         print(f"A média do aluno é: {media}")