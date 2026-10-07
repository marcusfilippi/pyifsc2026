'''6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
conforme abaixo:
Cadastro de Pessoas
-------------------
1 – Cadastrar
2 – Listar
0 – Sair
Opção: '''

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
    print ("0 – Sair")
    
    opcao = int(input("Digite a opção que você deseja: "))
    
    if opcao==0:
        break
    if opcao == 1:
        n = input("Digite o nome do novo cadastrado: ")
        i = int(input("Digite a idade "))
        a = float(input("Digite a altura do novo cadastrado: "))
        p = float(input("Digite o peso do novo cadastrado"))
        estudantes.append(Pessoa(n,i,a,p))
        
    if opcao == 2:
        for e in estudantes:
            print(e.people())