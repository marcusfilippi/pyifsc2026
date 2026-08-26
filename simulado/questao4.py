'''4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
significados como valores. Inicie com:
"apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
situação difícil, ou usar de meios extremos e exagerados"
Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
não encontrada”.'''

palavras = { "apelar" : "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados"}

i=0

while i<4:
    novapalavra = str(input("Digite uma nova palavra a ser cadastrada:"))

    if novapalavra in palavras:
            print("palavra já existente, tente outra")
    else:
            novadescr = str(input("Digite a descrição da palavra: "))
            palavras[novapalavra] = novadescr
    i= i+1

consul = str(input("Digite a palavra a ser pesquisada: "))


for palavra, significado in palavras.items():
    if palavra == consul:
        print (palavra)
        print (significado)

