'''3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
exiba o valor a ser pago.'''

precoproduto = float(input("Digite o valor do produto comprado: R$"))
quant = int(input("Digite a quantidade de produtos comprados: "))

precofinal = precoproduto*quant

if precofinal>=100:
    precofinal = precofinal-((precofinal/100)*10)

print (f"O valor a ser pago é de: R${precofinal}")
