#Exercício 10: Implemente um algoritmo que solicite ao usuário a
#quantidade de salgados consumidos na cantina e o valor do
#salgado (considere que todos possuem o mesmo preço). Solicite
#também ao usuário a quantidade de sucos consumida e o valor
#do suco (considere, também, que todos possuem o mesmo
#preço). Em seguida, exiba o valor total da compra.




precosalgado = float(input("Qual o preço do salgado?"))
quantsalg = int(input("Quantos salgados você comprou na cantina?"))
precosuco = float(input("Qual o preço do suco?"))
quantsuco = int(input("Quantos sucos você comprou na cantina?"))



divida = (precosalgado*quantsalg)+(precosuco*quantsuco)

print  ("Você deve pagar: R$", divida)