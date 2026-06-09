#8 – Suponha que você recebeu a última fatura do seu cartão de crédito no valor de R$
#1.000,00 e que você não possa pagá-la. Faça um programa que calcule sua dívida total
#com o banco depois de uma quantidade de meses informada durante a execução do 
#programa. Considere que a taxa de juros mensal de um cartão de crédito é de 15,30% ao
#mês. Fonte da taxa de juros utilizada: https://einvestidor.estadao.com.br/educacaofinanceira/juros-cartao-de-credito-dicas-para-evitar-dividas/
#A título de curiosidade, simule sua dívida final no prazo de 2 anos (24 meses).

divida = float(1000)

meses = int(input("Digite o número de meses que você vai atrasar a dívida:"))

i = 1

while i<=meses:
    divida = ((divida/100)*15.30)+divida
    i = i+1

print (f"Sua dívida total será de: R$ {divida:.2f}")