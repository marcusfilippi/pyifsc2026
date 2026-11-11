import os
import pickle

class Membro:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.localizacao = None
        
    def __repr__(self):
        return f"Nome: {self.nome}. Idade: {self.idade}."
    
class Localizacao:
    def __init__(self, localizacao, data, hora):
        self.localizacao = localizacao
        self.data = data
        self.hora = hora
        
    def __repr__(self):
        return f"Localização: {self.localizacao} | Data: {self.data} | Hora: {self.hora}"
    
    
class Login:
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
         
    def __repr__(self):
        return f"Email: {self.email}. Senha: {self.senha}"
    

email = ""
senha = ""
        
membros =[]
login = None
    

nome_arquivo = "membros.pkl"

if os.path.isfile("membros.pkl"):
    with open("membros.pkl", "rb") as f:
        membros = pickle.load(f)

if os.path.isfile("login.pkl"):
    with open("login.pkl", "rb") as f:
        login = pickle.load(f)


while True:
    print ("----------------")
    print ("Login Securikyd")
    print ("----------------")
    print ("1 - Criar Conta")
    print ("2 - Fazer login")
    print ("0 - Sair")
    
    opcao = int(input("Digite a opção que você deseja: "))
    
    if opcao == 0:
        break
    
    elif opcao == 1:
        email = input("Digite o email da sua nova conta: ")
        senha = input("Digite a senha da sua nova conta: ")
        login = Login(email, senha)
        print ("Conta criada com sucesso! Faça login para acessa-lá")
        
    elif opcao == 2:
        e = input("Digite o email da sua conta: ")
        s = input("Digite a senha da sua conta: ")
        
        if login is not None and e == login.email and s == login.senha:
            print ("Login bem-sucedido! Estamos te redirecionando")
            
            while True:
                print ("----------------")
                print ("Securikyd")
                print ("----------------")
                print ("1 - Adicionar membros na familia")
                print ("2 - Excluir membro na familia")
                print ("3 - Adicionar última localização de um membro")
                print ("4 - Verificar a última localização de um membro")
                print ("5 - Listar toda a familia")
                print ("6 - Mostrar email e senha")
                print ("7 - Alterar email ou senha")
                print ("8 - Salvar dados")
                print ("0 - sair")
                
                opcao = int(input("Digite a opção que você deseja: "))
                
                if opcao == 0:
                    break
                
                if opcao == 1:
                    n = input("Digite o nome do novo membro: ")
                    i = input("Digite a idade do novo membro: ")
                    membros.append (Membro(n,i))
                    print("Membro adicionado com sucesso!")
                    
                elif opcao == 2:
                    for i in range(len(membros)):
                        print(f"Índice {i}: {membros[i]}")
                        
                    r = int(input("Digite o número do membro que você quer excluir: "))
                    
                    if r >= 0 and r<len(membros):
                        membros.pop(r)
                        print ("Excluido com sucesso!")
                        
                    else:
                        print ("Indice inválido, tente novamente")

                elif opcao == 3:
                    for i in range(len(membros)):
                        print(f"Índice {i}: {membros[i]}")
                        
                    l = int(input("Digite o indice do membro que vocẽ quer atualizar a última localização: "))
                    
                    if l >= 0 and l<len(membros):
                        loc = input("Digite a nova localização: ")
                        data = input("Digite a data desta atualização (DD/MM/AAAA): ")
                        hora = input("Digite a hora desta atualização (HH:MM): ")
                        membros[l].localizacao = Localizacao(loc,data,hora)
                        print ("Localização adicionada com sucesso!")
                        
                    else:
                        print ("Indice inválido, tente novamente")
                
                elif opcao == 4:
                    for i in range(len(membros)):
                        print(f"Índice {i}: {membros[i]}")
                        
                    r = int(input("Digite o indice do membro que você quer ver: "))
                    
                    if r >= 0 and r<len(membros):
                       print (repr(membros[r],repr(membros[r].localizacao)))
                    else:
                        print ("Indice inválido, tente novamente")
                        
                elif opcao == 5:
                    for i in range(len(membros)):
                        print (repr(membros[i]))
                        
                elif opcao == 6:
                    se = input("Digite a sua senha: ")
                    if se == login.senha:
                        print (login)
                    
                elif opcao == 7: 
                    se = input("Digite a sua senha: ")
                    if se == login.senha:
                        print ("1 - Alterar E-Mail")
                        print ("2 - Alterar Senha")
                        
                        op = int(input("Digite a opção que você deseja: "))
                        
                        if op == 1:
                            emn = input("Digite seu novo E-Mail: ")
                            login.email = emn
                            print ("E-Mail alterado com sucesso.")
                            
                        elif op == 2:
                            sen = input("Digite a sua nova senha: ")
                            login.senha = sen
                            print ("Senha alterada com sucesso.")
                        
                elif opcao == 8:
                    
                    with open('membros.pkl', 'wb') as f:
                        pickle.dump (membros, f)
            
                    with open('login.pkl', 'wb') as f:
                        pickle.dump (login, f)
                    print ("Dados Salvos")
                
                
                
        else: 
            print ("Senha ou email incorretos, tente novamente")        