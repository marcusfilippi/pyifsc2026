#6 - Jogo do Pedra, Papel, Tesoura. Solicite as escolhas do jogador 1 e do jogador 2
#(“pedra”, “papel” ou “tesoura”). Use condicionais para determinar quem ganhou:
#• Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.
#• Exiba uma mensagem como “Jogador 1 venceu!” ou “Empate!”.

jog1 = str(input("Jogador 1: pedra, papel ou tesoura! Digite a sua escolha:"))
jog2 = str(input("Jogador 2: pedra, papel ou tesoura! Digite a sua escolha:"))

if jog1 == jog2:
    print ("Empate")

if jog1 == "pedra" and jog2 == "tesoura":
    print ("Jogador 1 ganhou!")

if jog1 == "papel" and jog2 == "pedra":
    print ("Jogador 1 ganhou!")

if jog1 == "tesoura" and jog2 == "papel":
    print ("Jogador 1 ganhou!")

if jog2 == "pedra" and jog1 == "tesoura":
    print ("Jogador 2 ganhou!")

if jog2 == "papel" and jog1 == "pedra":
    print ("Jogador 2 ganhou!")

if jog2 == "tesoura" and jog1 == "papel":
    print ("Jogador 2 ganhou!")