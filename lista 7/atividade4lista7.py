'''4 - Exercício: Funcionario e ContratoDeTrabalho (1..1).
Objetivo: Modelar um 1..1 onde a "parte" (Contrato) é obrigatória e contém a lógica de
cálculo que o "todo" (Funcionario) utiliza.
Classes: ContratoDeTrabalho e Funcionario.
Regras:
• A classe ContratoDeTrabalho deve ter salario_bruto (float) e percentual_impostos
(float, ex: 0.11 para 11% de INSS).
• O ContratoDeTrabalho deve ter um método chamado valor_impostos que calcula e
retorna o valor exato do desconto (ex: salario_bruto * percentual_impostos).
• A classe Funcionario deve ter nome e cargo.
• Um Funcionario deve ter exatamente um ContratoDeTrabalho para ser criado
(1..1).
• O __init__ do Funcionario deve receber nome, cargo, e também o salario_bruto e o
percentual_impostos necessários para criar sua própria instância de
ContratoDeTrabalho (Composição). O atributo funcionario.contrato nunca pode ser
None.
• Crie um método chamado salario_liquido na classe Funcionario. Este método deve:
◦ Acessar o salario_bruto do seu contrato.
◦ Acessar o valor_impostos calculado pelo seu contrato.
◦ Retornar o salario_bruto menos o valor_impostos.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo Funcionario. Faça, também, o Diagrama de Classes da sua
implementação final.4 - Exercício: Funcionario e ContratoDeTrabalho (1..1).
Objetivo: Modelar um 1..1 onde a "parte" (Contrato) é obrigatória e contém a lógica de
cálculo que o "todo" (Funcionario) utiliza.
Classes: ContratoDeTrabalho e Funcionario.
Regras:
• A classe ContratoDeTrabalho deve ter salario_bruto (float) e percentual_impostos
(float, ex: 0.11 para 11% de INSS).
• O ContratoDeTrabalho deve ter um método chamado valor_impostos que calcula e
retorna o valor exato do desconto (ex: salario_bruto * percentual_impostos).
• A classe Funcionario deve ter nome e cargo.
• Um Funcionario deve ter exatamente um ContratoDeTrabalho para ser criado
(1..1).
• O __init__ do Funcionario deve receber nome, cargo, e também o salario_bruto e o
percentual_impostos necessários para criar sua própria instância de
ContratoDeTrabalho (Composição). O atributo funcionario.contrato nunca pode ser
None.
• Crie um método chamado salario_liquido na classe Funcionario. Este método deve:
◦ Acessar o salario_bruto do seu contrato.
◦ Acessar o valor_impostos calculado pelo seu contrato.
◦ Retornar o salario_bruto menos o valor_impostos.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo Funcionario. Faça, também, o Diagrama de Classes da sua
implementação final.'''

class ContratoDeTrabalho:
    def __init__(self, salario_bruto, percentual_impostos):
        self.salario_bruto = salario_bruto
        self.percentual_impostos = percentual_impostos

    def valor_impostos(self):
        return self.salario_bruto*self.percentual_impostos

    def __repr__(self):
        return f"Salário Bruto: R${self.salario_bruto}. Percentual de impostos: {self.percentual_impostos}"

class Funcionario:
    def __init__(self, nome, cargo, salario_bruto, percentual_impostos):
        self.nome = nome
        self.cargo = cargo
        self.contrato = ContratoDeTrabalho(salario_bruto, percentual_impostos)

    def __repr__(self):
        return f"Nome: {self.nome}. Cargo: {self.cargo}"

    def salario_liquido(self):
        return self.contrato.salario_bruto - self.contrato.valor_impostos()

nome = input("Digite o nome do funcionario: ")
cargo = input("Digite o cargo do funcionario: ")
salario = float(input("Digite o salario bruto do funcionario: "))
impostos = float(input("Digite o percentual de impostos do funcionario (Ex.: 0.2 = 20%): "))
funcionario = Funcionario(nome,cargo,salario,impostos)

while True:
    print("Funcionário")
    print("-------------------")
    print("1 – Consultar funcionário")
    print("2 – Consultar contrato")
    print("3 – Consultar valor dos impostos")
    print("4 – Consultar salário líquido")
    print("0 – Sair")

    opcao = int(input("Digite a opção que você deseja: "))

    if opcao == 0:
        break

    elif opcao == 1:
        print(funcionario)

    elif opcao == 2:
        print(funcionario.contrato)

    elif opcao == 3:
        print (f"O valor dos impostos é: R$ {funcionario.contrato.valor_impostos()}")

    elif opcao == 4:
        print(f"O salário líquido é: R$ {funcionario.salario_liquido()}")



    
        