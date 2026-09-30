class Professores:
    def __init__(self, nome, sobrenome, especializacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.especializacao = especializacao
        
    def apresentar(self):
        return f"O nome do professor é {self.nome} {self.sobrenome} e sou professor de {self.especializacao}"

n = str(input("Nome: "))
s = input("Sobrenome: ")
e = input("Especialização: ")

professor1 =  Professores(n, s, e)   

n = str(input("Nome: "))
s = input("Sobrenome: ")
e = input("Especialização: ")

professor2 =  Professores(n, s, e)   
    
print (professor1.apresentar())
print (professor2.apresentar())