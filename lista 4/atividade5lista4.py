'''5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
Crie um menu, conforme abaixo, para permitir a interação com o seu programa:
Amigos Próximos
---------------
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair'''

amigos = []

while True:
    print("Amigos próximos <3:")
    print("----")
    print("1 – Cadastrar")
    print("2 – Excluir")
    print("3 – Listar")
    print("0 – Sair")

    opcao = int(input("Opção: "))

    if opcao == 0:
        break

    elif opcao == 1:
       amigos.append (str(input("Digite o nome do amigo a ser adicionado: ")))

    elif opcao == 2:
        