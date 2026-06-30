#1 – Implemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome
#do primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,
#deve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o
#programa deve exibir o nome de todos os bairros cadastrados na tela.

bairros = []

bairros.append("Ambrósio")

print ("Coloque os nomes dos bairros de Garopaba! Eu começo:")
print ("1- Ambrósio")
print ("2- ")
print ("3- ")
print ("4- ")
print ("5- ")
print ("6- ")
print ("Agora é com você!")





x=1

while x<=5:
    bairros.append (input("Digite o nome de 5 bairros de garopaba: "))
    x = x +1

limite = len(bairros)

x = 0

print ("Listando...")
while x<limite:
    print (f"Bairro {x+1}: {bairros[x]}")
    x =x+1