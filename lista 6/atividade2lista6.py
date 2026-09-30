'''2 – Crie uma classe chamada Carro com:
• Atributos: marca e cor.
• Um método chamado pintar que recebe uma nova cor como argumento e altera o
atributo cor para essa nova cor.
• Um método chamado mostrar_cor que retorna a cor atual do carro.
Teste criando um objeto, alterando sua cor com o método pintar e exibindo a nova cor
com mostrar_cor'''

class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        
    def pintar(self, novacor):
        self.cor = novacor
    
    def mostrarcor(self):
        return f"A cor atual do carro é {self.cor}"

# programa principal

m = input("Marca: ")
c = input("Cor: ")

carro1  = Carro(m,c)
nc = str(input("Digite a nova cor que o carro vai ficar: "))
carro1.pintar(nc)
print(carro1.mostrarcor())