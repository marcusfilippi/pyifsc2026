'''10 – Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
dados do disco, utilizando como base, o exercício 8.'''

'''8 – Implemente um algoritmo com as duas classes definidas logo abaixo. Seu algoritmo
deve ter um menu com as seguintes opções:
Sistema de Cadastro
-------------------
1 – Cadastrar estudante
2 – Cadastrar professor
3 – Listar estudantes
4 – Listar professores
5 – Alterar estudante pela matrícula
6 – Alterar estudante pelo nome
7 – Alterar professor pela matrícula
8 – Alterar professor pelo nome
9 – Excluir estudante pela matrícula
10 – Excluir professor pela matrícula
0 – Sair
Opção: '''

import pickle
estudantes = []
professores = []

class Estudante:
    def __init__(self, matricula, nome, sobrenome, idade):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def apresentare(self):
        return f"Matricula: {self.matricula}. Nome: {self.nome}. Sobrenome: {self.sobrenome}. Idade: {self.idade}"
    
class Professor:
    def __init__(self, matricula, nome, sobrenome, idade, especializacao):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.especializacao = especializacao
        
    def apresentarp(self):
        return f"Matricula: {self.matricula}. Nome: {self.nome}. Sobrenome: {self.sobrenome}. Idade: {self.idade}. Especialização: {self.especializacao}"
    
while True:
    print ('''Sistema de Cadastro
            -------------------
            1 – Cadastrar estudante
            2 – Cadastrar professor
            3 – Listar estudantes
            4 – Listar professores
            5 – Alterar estudante pela matrícula
            6 – Alterar estudante pelo nome
            7 – Alterar professor pela matrícula
            8 – Alterar professor pelo nome
            9 – Excluir estudante pela matrícula
            10 – Excluir professor pela matrícula
            11 – Salvar dados
            12 – Carregar dados
            0 – Sair
            Opção: ''')
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 0:
        break
    
    elif opcao == 1:
        m = int(input("Digite a matricula do novo cadastrado: "))
        n = input("Digite o nome do novo cadastrado: ")
        s = input("Digite o sobrenome do novo cadastrado: ")
        i = int(input("Digite a idade do novo cadastrado: "))
        estudantes.append(Estudante(m, n, s, i))
        print ("Adicionado com sucesso")
        
    elif opcao == 2:
        m = int(input("Digite a matricula do novo cadastrado: "))
        n = input("Digite o nome do novo cadastrado: ")
        s = input("Digite o sobrenome do novo cadastrado: ")
        i = int(input("Digite a idade do novo cadastrado: "))
        e = input("Digite a especialização do novo cadastrado: ")
        professores.append(Professor(m, n, s, i, e))
        print ("Adicionado com sucesso")
        
    elif opcao == 3:
        for e in estudantes:
            print(e.apresentare())
            
    elif opcao == 4:
        for e in professores:
            print(e.apresentarp())
            
    elif opcao == 5:

        matricula = input("Digite a matrícula do estudante: ")
        for i in estudantes:
            if i.matricula == matricula:
                i.nome = input("Digite o novo nome: ")
                i.idade = int(input("Digite a nova idade: "))
                i.sobrenome = input("Digite o novo sobrenome: ")
                print("Atualizado com sucesso")
                break

    elif opcao == 6:

        nome = input("Digite o nome do estudante: ")
        for i in estudantes:
            if i.nome == nome:
                i.matricula = input("Digite a nova matrícula: ")
                i.idade = int(input("Digite a nova idade: "))
                i.sobrenome = input("Digite o novo sobrenome: ")
                print("Estudante atualizado!")
                break

    elif opcao == 7:

        matricula = input("Digite a matrícula do professor: ")
        for i in professores:
            if i.matricula == matricula:
                i.nome = input("Digite o novo nome: ")
                i.idade = int(input("Digite a nova idade: "))
                i.especializacao = input("Digite a nova especialização: ")
                print("Professor atualizado!")
                break

    elif opcao == 8:

        nome = input("Digite o nome do professor: ")
        for i in professores:
            if i.nome == nome:
                i.matricula = input("Digite a nova matrícula: ")
                i.idade = int(input("Digite a nova idade: "))
                i.especializacao = input("Digite a nova especialização: ")
                print("Professor atualizado!")
                break

    elif opcao == 9:

        matricula = input("Digite a matrícula do estudante: ")
        for i in estudantes:
            if i.matricula == matricula:
                estudantes.remove(i)
                print("Estudante excluído!")
                break

    elif opcao == 10:

        matricula = input("Digite a matrícula do professor: ")
        for i in professores:
            if i.matricula == matricula:
                professores.remove(i)
                print("Professor excluído!")
                break
            
    elif opcao==11:
        
        with open('estudant.pkl', 'wb') as f:
            pickle.dump (estudantes, f)
            
        with open('professores.pkl', 'wb') as f:
            pickle.dump (professores, f)
            print ("Lista Salva")
            
    elif opcao == 12:
        with open('estudant.pkl', 'rb') as f:
            estudantes = pickle.load(f)
            
        with open('professores.pkl', 'rb') as f:
            professores = pickle.load(f)
            print ("Dados carregados :)")
            
    