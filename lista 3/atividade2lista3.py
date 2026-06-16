#2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
#de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
#reprovado(a)).

notas = [0,0,0,0]

x = 0
totalnota = 0
while x<=3:
   notas[x] = float(input("Nota: "))
   totalnota = totalnota + notas[x]
   x += 1

media = totalnota/4

if media >= 6:
   print (f"Sua média foi: {media}")
   print ("Você foi aprovado")

else:
   print (f"Sua média foi: {media}")
   print ("Você foi reprovado")
