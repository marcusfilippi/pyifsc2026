class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
n = str(input("Nome: "))
i = int(input("Idade: "))

estudante1 = Estudante(n, i)
 
n = str(input("Nome: "))
i = int(input("Idade: "))

estudante2 = Estudante(n, i)

n = str(input("Nome: "))
i = int(input("Idade: "))

estudante3 = Estudante(n, i)

print ("Estudante 1: ")
print (estudante1.nome)
print (estudante1.idade)
print ("Estudante 2: ")
print (estudante2.nome)
print (estudante2.idade)
print ("Estudante 3: ")
print (estudante3.nome)
print (estudante3.idade)