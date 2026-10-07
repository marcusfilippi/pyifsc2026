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