'''5 – Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def people(self):
        return f"Nome: {self.nome}. Idade: {self.idade}. Peso: {self.peso}KG. Altura: {self.altura}"
     
        
    def imc(self, imc):
        imc = self.peso/(self.altura*self.altura)
        return imc
    
    def imcnome(self):
        return f"Nome: {self.nome}. IMC: {self.imc(self)}"
        
        
n = input("Nome: ")
i = int(input("Idade: "))
p = float(input("Peso: "))
a = float(input("Altura: "))


pessoa1  = Pessoa(n, i, p, a)
print (pessoa1.people())
print (f"O IMC de {pessoa1.nome} é: {pessoa1.imc(pessoa1)}")
print (pessoa1.imcnome())

n = input("Nome: ")
i = int(input("Idade: "))
p = float(input("Peso: "))
a = float(input("Altura: "))


pessoa2  = Pessoa(n, i, p, a)
print (pessoa2.people())
print (f"O IMC de {pessoa2.nome} é: {pessoa2.imc(pessoa2)}")
print (pessoa2.imcnome())

n = input("Nome: ")
i = int(input("Idade: "))
p = float(input("Peso: "))
a = float(input("Altura: "))


pessoa3  = Pessoa(n, i, p, a)
print (pessoa3.people())
print (f"O IMC de {pessoa3.nome} é: {pessoa3.imc(pessoa3)}")
print (pessoa3.imcnome())