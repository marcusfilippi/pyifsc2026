import pickle

class Membro:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.localizacao = None
        
    def __repr__(self):
        return f"Nome: {self.nome}. Idade: {self.idade}. Última localização: {self.localizacao} "
    
class Login:
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
         
    def __repr__(self):
        return f"Email: {self.email}. Senha: {self.senha}"
    

        
membros =[]
login = []
    

with open('membros.pkl', 'rb') as f:
            membros = pickle.load(f)
            
with open('login.pkl', 'rb') as f:
            login = pickle.load(f)


while True:
    print ("Login Securikyd")
    print ("_______________")
    print ("1 - Criar Conta")
    print ("2 - Fazer login")
    print ("0 - Sair")
    
    opcao = int(input("Digite a opção que vocẽ deseja: "))
    
    if opcao == 0:
        break
    
    elif opcao == 1:
        email = input("Digite o email da sua nova conta: ")
        senha = input("Digite a senha da sua nova conta: ")
        print ("Conta criada com sucesso! Faça login para acessa-lá")
        
    elif opcao == 2:
        e = input("Digite o email da sua conta: ")
        s = input("Digite a senha da sua conta: ")
        
        if e == email and s == senha:
            print ("Login bem-sucedido! Estamos te redirecionando")
            
            while True:
                print ("Securikyd")
                print ("_______________")
                print ("1 - Adicionar membros na familia")
                print ("2 - Excluir membro na familia")
                print ("3 - Adicionar última localização de um membro")
                print ("4 - Verificar a última localização de um membro")
                print ("5 - Listar toda a familia")
                print ("7 - Mostrar email e senha")
                print ("8 - Alterar email ou senha")
                print ("9 - Salvar dados")
                print ("0 - sair")
                
                opcao = int(input("Digite a opção que você deseja: "))
                
                if opcao == 1:
                    n = input("Digite o nome do novo membro: ")
                    i = input("Digite a idade do novo membro: ")
                    membros.append (Membro(n,i))
                    print("Membro adicionado com sucesso!")
                    
                elif opcao == 2:
                    for i in range(len(membros)):
                        print(f"Índice {i}: {membros[i]}")
                        
                    r = int("Digite o número do membro que você quer excluir: ")
                    
                    if r >= 0 and r<=len(membros):
                        membros.pop(r)
                        print ("Excluido com sucesso!")
                        
                    else:
                        print ("Indice inválido, tente novamente")

                elif opcao == 3:
                    for i in range(len(membros)):
                        print(f"Índice {i}: {membros[i]}")
                        
                    l = int(input("Digite o indice do membro que vocẽ quer atualizar a última localização: "))
                    
                    if l >= 0 and l<=len(membros):
                        loc = input("Digite a nova localização: ")
                        membros[l].localizacao = loc
                        
                    else:
                        print ("Indice inválido, tente novamente")
                
                elif opcao == 4:
                    for i in range(len(membros)):
                        print(f"Índice {i}: {membros[i]}")
                        
                    r = int("Digite o indice do membro que você quer ver: ")
                    
                    if r >= 0 and r<=len(membros):
                       print (repr(membros[r]))
                    else:
                        print ("Indice inválido, tente novamente")
                        
                elif opcao == 5:
                    for i in range(len(membros)):
                        print (repr(membros[i]))
                        
                elif opcao == 6:
                        
                elif opcao == 9:
                    
                    with open('membros.pkl', 'wb') as f:
                        pickle.dump (membros, f)
            
                    with open('login.pkl', 'wb') as f:
                        pickle.dump (login, f)
                    print ("Dados Salvos")
                
                
                
        else: 
            print ("Senha ou email incorretos, tente novamente")        