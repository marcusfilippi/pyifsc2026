''''9 – Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
dados do disco, utilizando como base, o exercício 7.'''

'''7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
peso, baseado, também, no nome informado.'''

import pickle


estudantes = []
class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    def people(self):
        return f"Nome: {self.nome}. Idade: {self.idade}. Peso: {self.peso}KG. Altura: {self.altura}"
        
while True:
    print ("Cadastro de Pessoas")
    print ("-------------------")
    print ("1 – Cadastrar")
    print ("2 – Listar")
    print ("3 – Excluir")
    print ("4 – Atualizar")
    print ("5 – Salvar dados")
    print ("6 – Carregar dados")
    print ("0 – Sair")
    
    opcao = int(input("Digite a opção que você deseja: "))
    
    if opcao==0:
        break
    elif opcao == 1:
        n = input("Digite o nome do novo cadastrado: ")
        i = int(input("Digite a idade "))
        a = float(input("Digite a altura do novo cadastrado: "))
        p = float(input("Digite o peso do novo cadastrado"))
        estudantes.append(Pessoa(n,i,a,p))
        print ("Adicionado com sucesso")
        
    elif opcao == 2:
        for e in estudantes:
            print(e.people())
            
    elif opcao == 3:
        excluir = input("Digite o nome do estudante que você deseja excluir: ")
        for e in estudantes:
            if e.nome == excluir:
                estudantes.remove(e)
                print ("Deletado com sucesso")
                break
            
    elif opcao == 4:
        atualizar = input("Digite o nome do estudante que você deseja atualizar: ")
        for e in estudantes:
            if e.nome == atualizar:
                i = int(input("Digite a nova idade: "))
                a = float(input("Digite a nova altura: "))
                p = float(input("Digite o novo peso: "))
                e.peso = p 
                e.altura = a
                e.idade = i
                print ("Dados atualizados com sucesso")
                
    elif opcao == 5:
        with open('estudantes.pkl', 'wb') as f:
            pickle.dump (estudantes, f)
            print ("Lista Salva")
            
    elif opcao == 6:
        with open('estudantes.pkl', 'rb') as f:
            estudantes = pickle.load(f)
            print ("Dados carregados :)")