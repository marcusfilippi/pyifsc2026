'''3 - VagaDeEstacionamento e Carro (0..1 - Associação Simples)
Objetivo: Modelar um relacionamento 0..1 onde a "parte" (Carro) vem de fora
(Agregação/Associação).
Classes: Carro e VagaDeEstacionamento.
Regras:
A classe Carro é simples, tem apenas placa e modelo.
• A classe VagaDeEstacionamento tem um id_vaga (ex: "A-101").
• Uma VagaDeEstacionamento pode estar ocupada por zero ou um Carro (0..1). O
atributo carro_estacionado começa como None.
• Crie um método ocupar_vaga(carro_obj). Este método deve verificar se a vaga já
está None. Se estiver livre, associa o carro_obj (vindo de fora) à vaga e retorna
True. Se já estiver ocupada, não faz nada e retorna False.
• Crie um método liberar_vaga() que simplesmente seta carro_estacionado de volta
para None.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo VagaDeEstacionamento. Faça, também, o Diagrama de
Classes da sua implementação final.'''

class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo
        
    def __repr__(self):
        return f"Placa: {self.placa}. Modelo do carro: {self.modelo}"
    
class VagaDeEstacionamento: 
    def __init__(self, id_vaga):
        self.id_vaga = id_vaga
        self.carro_estacionado = None
        
    def ocupar_vaga(self, carro_obj):
        if self.carro_estacionado == None:
            self.carro_estacionado = carro_obj
            return True
        else:
            return False
        
    def liberar_vaga(self):
        self.carro_estacionado=None
        
carros = []        
        
while True:
    print ("Vaga Estacionamento")
    print ("-------------------")
    print ("1 – Cadastrar carro")
    print ("2 – Listar carro")
    print ("4 – Estacionar carro")
    print ("5 – Liberar vaga")
    print ("6 – Consultar vaga")
    print ("0 – Sair")
    
    opcao = int(input("Digite a opção que você deseja: "))
    
    if opcao == 0:
        break
    
    elif opcao == 1:
        p = input("Digite a placa do carro: ")
        m = input("Digite o modelo do carro: ")
        carros.append = Carro(p,m)
        
    elif opcao == 2:
        print (carros)
        
    elif opcao ==3:
        
        