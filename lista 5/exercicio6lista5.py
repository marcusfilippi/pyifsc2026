'''6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
usuário para inserir as horas e minutos, e exiba o tempo total em minutos.'''

def tempo_total(h, m):
    i = h *60
    r = i + m
    return r

horas = int(input("Digite o número de horas que vocẽ jogou: "))
minutos = int(input("Digite o número de minutos a mais que as horas que vocẽ jogou vocẽ jogou: "))

resul = tempo_total(horas, minutos)

print (f"Você jogou {resul} minutos")