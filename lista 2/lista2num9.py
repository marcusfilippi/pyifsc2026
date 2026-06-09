#9 – Considere que você deseja fazer uma reserva mensal, em dinheiro, para a compra de
#um determinado presente para você mesmo(a). Considere que todo mês você depositará,
#em uma poupança no banco, um mesmo valor em reais. Faça um programa que leia o
#valor que será depositado mensalmente e exiba na tela o valor acumulado mês a mês
#durante 24 meses. Considere que a taxa de juros de uma poupança é 0,5% ao mês, que
#a poupança não possui nenhum saldo inicial. Você pode utilizar uma calculadora de juros
#compostos para validar o cálculo do seu algoritmo, por exemplo o site:
#https://www.idinheiro.com.br/calculadoras/calculadora-juros-compostos/

dinmensal = float(input("Quanto de dinheiro você irá colocar mensalmente? R$"))

i =1 
jurospoupanca = 0.5
poupanca = 0

while i<=24:
           poupanca = ((poupanca/100)*jurospoupanca)+poupanca
           poupanca = poupanca + dinmensal
           i = i +1

print (f"No final você terá: R$ {poupanca:.2f}")