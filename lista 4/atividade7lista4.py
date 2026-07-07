'''7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
não existam notas cadastradas, seu programa deve informar “Erro: não há notas
cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
5 – Mostrar maior nota
6 – Mostrar menor nota
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
    print("5- Mostrar maio nota")
    print("6 - Mostrar menor nota")
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
  
    elif opcao == 6:
        menor = min(notas)
        print = (f"A menor nota é: {menor}")

    elif opcao == 5:
        maior = max(notas)
        print = (f"A maior nota é: {maior}")

    