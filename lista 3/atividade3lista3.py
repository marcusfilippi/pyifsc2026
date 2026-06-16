#3 – Faça um programa que funcionará como um cadastro de códigos de produtos de uma
#loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize
#os elementos da lista com -1, este valor indicará que o elemento está vago para o
#cadastro. Seu programa deve ter um menu com uma opção para cadastrar um novo
#código (apenas um por vez) e para listar os todos códigos cadastrados (não devem ser
#listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha
#na hora de cadastrar um novo código e também não deve ser possível cadastrar um
#produto com o código -1. No momento do cadastro, não deve ser informado o valor do
#índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:

codigos = [-1] * 10
contadornum = 0
x =0
p =0

while True:
    print ("Menu:")
    print ("----")
    print ("1 – Cadastrar")
    print ("2 – Listar todos")
    print ("0 – Sair ")

    opcao = int(input("Opção: "))

    if opcao == 0:
         break 
    elif opcao == 2 :
         print ("Listando...")
         while p <= contadornum-1:
              if codigos[p] == -1:
                  break
              else:
               print(f"Produto: {p}. Código: {codigos[p]}")
               p = p+1
         print ("Fim da lista.")
         p = 0

    elif opcao == 1:
         if contadornum <= 9:
          x = int(input("Digite código desejado: "))
          if x != -1: 
           codigos [contadornum] = x
           contadornum = contadornum + 1
           print ("Código cadastrado com sucesso!")
         else:
             print("10 códigos já armazenados. Você chegou no limite!")