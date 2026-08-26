'''11 – Crie um algoritmo com uma função que retorna um valor em reais escrito por
extenso. Por exemplo, caso seja passado “1.74” como parâmetro para a função, ela deve
retornar: um real e setenta e quatro centavos. Caso seja passado “3251.90”, deve retornar
“três mil duzentos e cinquenta e um reais e noventa centavos”.'''
def extenso(a):
    numero = int(a)

    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
             ]      

    diferentes = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }

    dezenas = [
        "", "", "vinte", "trinta", "quarenta",
        "cinquenta", "sessenta", "setenta",
        "oitenta", "noventa"
    ]

    centenas = [
        "", "cento", "duzentos", "trezentos",
        "quatrocentos", "quinhentos", "seiscentos",
        "setecentos", "oitocentos", "novecentos"
    ]

    if numero == 1:
        return "um real"

    if numero < 10:
        return unidades[numero] + " reais"

    if numero < 20 and numero>9:
        return diferentes[numero] + " reais"

    if numero>=20 and numero<100:
        dezena = numero//10
        unidade = numero%10

        if unidade == 0:
            return dezenas[dezena] + " reais"
        else:
            return dezenas[dezena]+ " e "+unidades[unidade] + " reais"

    if numero >=100 and numero<1000:
        if numero == 100:
            return "cem reais"

        centena = numero // 100
        resto = numero % 100
        
        if resto == 0:
            return centenas[centena] + " reais"
        
        return centenas[centena] + " e " + extenso(resto)

    if numero>=1000 and numero<10000:
        milhar = numero // 1000
        resto = numero % 1000

        if resto == 0:
            return unidades[milhar] + " mil reais"

        return unidades[milhar] + " mil e " + extenso(resto)

def virgulas(a):
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
             ]      

    diferentes = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }

    dezenas = [
        "", "", "vinte", "trinta", "quarenta",
        "cinquenta", "sessenta", "setenta",
        "oitenta", "noventa"
    ]

    partes = f"{a:.2f}".split('.')
    numero = int(partes[1])

    if numero == 0:
        return ""

    if numero == 1:
        return " e um centavo"

    if numero < 10:
        return " e " + unidades[numero] + " centavos"

    if numero < 20 and numero>9:
        return " e " + diferentes[numero] + " centavos"

    if numero>=20 and numero<100:
        dezena = numero//10
        unidade = numero%10

        if unidade == 0:
            return " e " + dezenas[dezena] + " centavos"
        else:
            return " e " + dezenas[dezena] + " e " + unidades[unidade] + " centavos"

valor = float(input("Digite o valor que deseja: "))

resul = extenso(valor) + virgulas(valor)

print(resul)







