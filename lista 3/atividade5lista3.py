#5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
#sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
#ser através de um menu com as seguintes opções:
#1 – Cadastrar
#2 - Excluir
#3 - Alterar
#4 - Listar
#0 - Sair
#A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
#excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
#solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
#da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
#das pessoas cadastradas. 

nome = [0] * 15
peso = [0] * 15
idade = [0] * 15
altura = [0] * 15

x = 0
p = 0
i = 0
y = 0
m = 0
pessoaaniquilada = 0 
contpessoas = 0
pessoamudar = 0

while True:
    print("Menu:")
    print("----")
    print("1 – Cadastrar")
    print("2 – Excluir")
    print("3 – Alterar")
    print("4 – Listar")
    print("0 – Sair")

    opcao = int(input("Opção: "))

    if opcao == 0:
        break

    elif opcao == 1:
        if contpessoas <= 14:
            i = str(input("Digite seu nome:"))
            x = 0 

            while True:
                if nome[x] == 0:
                    nome[x] = i
                    i = int(input("Digite sua idade:"))
                    idade[x] = i
                    i = float(input("Digite sua altura (Em metros):"))
                    altura[x] = i
                    i = float(input("Digite seu peso(em KG):"))
                    peso[x] = i
                    contpessoas = contpessoas + 1
                    break
                x = x + 1

    elif opcao == 2:
        pessoaaniquilada = str(input("Digite o nome a ter seus dados excluídos:"))

        excluiu = False
        p = 0  

        while p <= 14:
            if nome[p] == pessoaaniquilada:
                nome[p] = 0
                peso[p] = 0
                altura[p] = 0
                idade[p] = 0
                contpessoas = contpessoas - 1 
                excluiu = True
                break
            p = p + 1

        if excluiu:
            print("Excluiu mesmo")
        else:
            print("Nome não encontrado")

    elif opcao == 3:
        pessoamudar = str(input("Digite o nome a ter seus dados alterados:"))

        mudou = False
        y = 0 

        while y <= 14:
            if nome[y] == pessoamudar:
                print("1 – Mudar Nome")
                print("2 – Mudar Peso")
                print("3 – Mudar Altura")
                print("4 – Mudar idade")
                i = int(input("Digite o código da informação que você quer alterar: "))

                if i == 1:
                    m = str(input("Digite o nome a ficar no lugar: "))
                    nome[y] = m

                elif i == 2:
                    m = float(input("Digite o peso a ficar no lugar: "))
                    peso[y] = m

                elif i == 3:
                    m = float(input("Digite a altura a ficar no lugar: "))
                    altura[y] = m

                elif i == 4:
                    m = int(input("Digite a idade a ficar no lugar:"))
                    idade[y] = m

                mudou = True
                break

            y = y + 1

        if not mudou:
            print("Nome não encontrado")

    elif opcao == 4:
        print("Listando...")
        y = 0  

        while y <= 14:
            if nome[y] != 0:
                print(f"Nome: {nome[y]}. Idade: {idade[y]}. Peso: {peso[y]}. Altura: {altura[y]}.")
            y = y + 1

        print("Fim da lista.")