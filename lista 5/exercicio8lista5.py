'''8 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada no formato
de string, por exemplo: “15:31”. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para imprimir a saída. A função que faz a conversão deve ter duas
saídas: uma com a hora convertida e outra com “A”, caso seja “A.M.” e “P”, caso seja
“P.M.”. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar.'''

def converter(hora, minutos):
    if hora>12:
        resul = (f"{hora-12} : {minutos} PM")
    else:
        resul = (f"{hora} : {minutos} AM")
    return resul

def imprimir(resul):
    print (resul)
    
while True:
    print ("Convertor de horas")
    print ("1- Converter horas")
    print ("2- Imprimir últma conversão")
    print ("0- sair")
    opcao = int(input("Digite a opção que deseja"))
    
    if opcao == 0:
        break
    
    if opcao == 1:
        h = int(input("Digite o números de horas: "))
        m = int(input("Digite o números de minutos: "))
        r = (converter(h, m))
        
    if opcao == 2:
        print (r)