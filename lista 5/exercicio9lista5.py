'''9 - Construa uma função que receba uma data no formato DD/MM/AAAA (string) e
devolva uma string com a data por extenso, por exemplo: “doze de agosto de dois mil e
vinte e quatro”. Seu algoritmo deve ser capaz de converter datas entre os anos de 2000 e
2100.'''

def dataextenso(data):
    partes = data.split("/")

    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    meses = [
        "",
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro"
    ]

    dias = {
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
        20: "vinte",
        21: "vinte e um",
        22: "vinte e dois",
        23: "vinte e três",
        24: "vinte e quatro",
        25: "vinte e cinco",
        26: "vinte e seis",
        27: "vinte e sete",
        28: "vinte e oito",
        29: "vinte e nove",
        30: "trinta",
        31: "trinta e um"
    }

    resul = dias[dia] + " de "+ meses[mes] + " de " + str(ano)
    print (resul)
    return resul

data = str(input("Digite a data que vocẽ quer ter por extenso(DD/MM/AAAA): "))

dataextenso(data)
