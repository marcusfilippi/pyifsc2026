#Exercício 09: Implemente um algoritmo que solicite ao usuário a
#quantidade de salgados consumidos na cantina e o valor do
#salgado (considere que todos possuem o mesmo preço).
#Lembre-se que o preço é um número de ponto flutuante e não
#um inteiro. Em seguida, exiba o valor total da compra.

precosalgado = float(input("Qual o preço do salgado?"))
quantsalg = int(input("Quantos salgados você comprou na cantina?"))

divida = precosalgado*quantsalg

print  ("Você deve pagar: R$", divida)
