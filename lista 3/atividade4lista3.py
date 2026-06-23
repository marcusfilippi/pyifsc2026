#4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
#um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
#lista. Seu programa deve ter um menu com a seguinte estrutura:
#1 – Cadastrar
#2 - Excluir
#3 - Listar
#0 - Sair
#A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se
#houver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço
#disponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo
#nome da placa) e informar se houve sucesso ou falha. Já a opção listar deve
#simplesmente listar todas as placas cadastradas. Dica: utilize um valor padrão para definir
#um espaço vago na lista.

placas = [0] * 15
contplacas = 0
x = 0
i = 0
p = 0
y = 0
codigoaniquilado = 0

while True:
    print("Menu:")
    print("----")
    print("1 – Cadastrar")
    print("2 – Excluir")
    print("3 – Listar")
    print("0 – Sair")

    opcao = int(input("Opção: "))

    if opcao == 0:
        break

    elif opcao == 1:
        if contplacas <= 14:
            i = int(input("Digite seu código:"))
            if i != 0:
                x = 0 

                while True:
                    if placas[x] == 0:
                        placas[x] = i
                        contplacas = contplacas + 1
                        break
                    x = x + 1
            else:
                print("Não é possível adicionar um código igual a 0.")
        else:
            print("15 códigos já armazenados. Você chegou no limite!")

    elif opcao == 2:
        codigoaniquilado = int(input("Digite o código a ser excluído:"))

        excluiu = False
        p = 0  

        while p <= 14:
            if placas[p] == codigoaniquilado:
                placas[p] = 0
                contplacas = contplacas - 1 
                excluiu = True
                break
            p = p + 1

        if excluiu:
            print("Excluiu mesmo")
        else:
            print("Código não encontrado")

    elif opcao == 3:
        print("Listando...")
        y = 0  

        while y <= 14:
            if placas[y] != 0:
                print(f"Produto: {y}. Código: {placas[y]}")
            y = y + 1

        print("Fim da lista.")
               
                
