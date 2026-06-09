#Exercício 08: Implemente um algoritmo que leia a quantidade
#de partidas de um campeonato de futebol e indique a
#quantidade de minutos total (de todas as partidas juntas).
#Considere que cada partida terá sempre o mesmo tempo.

tomtalminpart = int(input("Total de minutos de uma partida: "))
quantpart = int(input("Total de partidas no campeonato: "))

minutosjogados = tomtalminpart*quantpart

print ("o total de minutos jogados no campeonato foi de", minutosjogados, "minutos")
