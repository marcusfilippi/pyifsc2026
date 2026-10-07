'''3 – Crie uma classe chamada ContaBancaria com:
• Atributos: titular e saldo.
• Um método chamado depositar que recebe um valor e adiciona ao saldo.
• Um método chamado sacar que recebe um valor e subtrai do saldo (não precisa
validar o saldo).
• Um método chamado mostrar_saldo que retorna o saldo atual.
Teste criando uma conta, fazendo depósitos, saques e exibindo o saldo.'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, deposito):
        self.saldo = self.saldo +deposito
        
    def sacar(self, saque):
        self.saldo = self.saldo - saque
    
    def mostrar_saldo(self):
        return f"O seu saldo atual é {self.saldo}"

# programa principal

t = input("Titular: ")
s = float(input("Saldo: "))

conta1  = ContaBancaria(t,s)
deposito = float(input("Digite o valor do deposito: "))
conta1.depositar(deposito)
saque = float(input("Digite o valor do saque: "))
conta1.sacar(saque)
print(conta1.mostrar_saldo())