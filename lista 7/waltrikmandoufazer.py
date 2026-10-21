class Motor:
    def __init__(self, potencia_cv):
        self.potencia_cv = potencia_cv
        self.ligado = False
    def __repr__(self):
        return f"<Potência do motor: {self.potencia_cv}, ligado: {self.ligado}>"
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def esta_ligado(self):
        return self.ligado


class Carro:
    def __init__(self, modelo: str, ano: int, motor_potencia: int):
        self.modelo = modelo
        self.ano = ano
        self.motordocarro = Motor(motor_potencia)
    def __repr__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Motor: {self.motordocarro}"
    def ligar_carro(self):
        self.motordocarro.ligar()
    def desligar_carro(self):
        self.motordocarro.desligar()
    def esta_ligado(self):
        return self.motordocarro.esta_ligado()


# Criar um carro
m = input("Digite o modelo: ")
a = int(input("Ano: "))
p = int(input("Potência CV: "))
carrinho = Carro(m, a, p)
print("Primeiro teste")
print(carrinho)
print("Segundo teste")
carrinho.ligar_carro()
print(carrinho)
if carrinho.esta_ligado():
    print("O fuscão do Rodolfo está ligado")
else:
    print("O fuscão do Rodolfo está desligado")
print("Terceiro teste")
carrinho.desligar_carro()
if carrinho.esta_ligado():
    print("O fuscão tá ligado")
else:
    print("O fuscão está desligado")