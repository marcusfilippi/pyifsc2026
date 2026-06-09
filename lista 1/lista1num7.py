#7 - Qual é o seu Signo? Solicite o dia e o mês de nascimento do usuário. Com base
#nesses valores, use condicionais para determinar o signo.

mes = int(input("Digite o mês que você nasceu:"))
dia = int(input("Digite o dia que você nasceu:"))

if (mes == 3 and dia >=21) or ( mes == 4 and dia <=19):
    print("Você é de Aries!")

if (mes == 4 and dia >=20) or ( mes == 5 and dia <=20):
    print("Você é de Touro!")

if (mes == 5 and dia >=21) or ( mes == 6 and dia <=20):
    print("Você é de Gẽmeos!")

if (mes == 6 and dia >=21) or ( mes == 7 and dia <=22):
    print("Você é de Cancêr!")

if (mes == 7 and dia >=23) or ( mes == 8 and dia <=22):
    print("Você é de Leão!")

if (mes == 8 and dia >=23) or ( mes == 9 and dia <=22):
    print("Você é de Virgem!")

if (mes == 9 and dia >=23) or ( mes == 10 and dia <=22):
    print("Você é de Libra!")

if (mes ==10 and dia >=23) or ( mes == 11 and dia <=21):
    print("Você é de Escorpião!")

if (mes ==11 and dia >=22) or ( mes == 12 and dia <=21):
    print("Você é de Sagitário!")

if (mes ==12 and dia >=22) or ( mes == 1 and dia <=19):
    print("Você é de Capricórnio!")

if (mes ==1 and dia >=20) or ( mes == 2 and dia <=18):
    print("Você é de Aquario!")

if (mes ==2 and dia >=19) or ( mes == 3 and dia <=20):
    print("Você é de Peixes!")