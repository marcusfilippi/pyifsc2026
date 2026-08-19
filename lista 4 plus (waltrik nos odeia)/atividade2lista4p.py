'''2 - A situação de logística da Empresa Alpha Entregas está necessitando de melhorias no
controle das saídas e retornos dos caminhões:
a) Considere que a empresa possui 8 caminhões numerados de 001 a 008;
b) Cada caminhão tem seu respectivo condutor, a relação dos condutores e seus
códigos está abaixo;
c) As entregas são monitoradas através do controle no retorno de cada caminhão;
d) Precisamos receber os dados do código do caminhão e do código do condutor,
somente assim consideraremos que a mercadoria daquela rota foi entregue;
e) O algoritmo deve prever o cadastro dos caminhões e dos condutores;
f) O algoritmo deve prever um cadastro com uma lista de todos os caminhões que
saem diariamente;
g) A cada saída diária dos caminhões, deve-se registrar a data e hora de saída de
cada veículo, bem como o condutor responsável;
h) Quando do retorno de cada caminhão, deve-se registrar a data e hora de
chegada;
i) O sistema deve ter opções para verificar se um determinado caminhão retornou da
rota ou não, mostrando a data, hora e nome do condutor, consultando por código do
veículo;
j) O sistema deve ter opções para listar o cadastro de caminhões;
k) O sistema deve ter opções para listar os condutores;
l) O sistema deve ter opções para listar, por data, a lista dos veículos que
retornaram;
m) Precisamos saber, em determinado momento, se todas as entregas do dia foram
realizadas.
Relação de Condutores:
001 – Roberto Souza
002 – João Graciano
003 – Karine Silva
004 – Pedro Luiz
005 – Maria Catarina
006 – Júlio Cardoso
007 – Altivo Antônio
008 – Jorge Gonçalves
009 – Marcos Vinícius
010 – Heleno Nunes
011 – Mara Cristina
012 – Otávio Rocha
Relação dos Veículos
001 – Monobloco
002 – Scania 112 HW
003 – Volkswagen Express 4150
004 – Volkswagen Express 6160
005 – Volkswagen VW 17230 Worker
006 – Volkswagen Express 9170
007 – Iveco Daily 40s14
008 – Iveco Tectro 310E28 '''

condutores = {'001' : "Roberto Souza",
'002' : "João Graciano",
'003' : "Karine Silva",
'004' : "Pedro Luiz",
'005' : "Maria Catarina",
'006' : "Júlio Cardoso",
'007' : "Altivo Antônio",
'008' : "Jorge Gonçalves",
'009' : "Marcos Vinícius",
'010' : "Heleno Nunes",
'011' : "Mara Cristina",
'012' : "Otávio Rocha"}

veiculos = {'001' : "Monobloco",
'002' : "Scania 112 HW",
'003' : "Volkswagen Express 4150",
'004' : "Volkswagen Express 6160",
'005' : "Volkswagen VW 17230 Worker",
'006' : "Volkswagen Express 9170",
'007' : "Iveco Daily 40s14",
'008' : "Iveco Tectro 310E28"}

saidas = []

while True:
    print("Rastreio de veículos:")
    print("-----------")
    print("1 – Cadastrar condutor")
    print("2 – Excluir condutor")
    print("3 – Listar condutor")
    print("4 - Excluir veículo")
    print("5 - Listar veículos")
    print("6 - Cadastrar veículo")
    print("7 - Registar saída")
    print("8 - Registar retorno")
    print("9 - Listar histórico do caminhão")
    print("10 - Verificar se as entregas do dia acabaram")
    print("0 – Sair")

    opcao = int(input("Digite a opção que você quer:"))

    if opcao == 0:
        break

    elif opcao == 1: 
        novcas = str(input("Digite o código do novo cadastrado:")).zfill(3)

        if novcas in condutores:
            print("Código já existente, tente outro")
        else:
            nomecas = str(input("Digite o nome do novo cadastrado:"))
            condutores[novcas] = nomecas

    elif opcao ==2:
        codaniquilado = str(input("Digite o código que você quer excluir:")).zfill(3)

        if codaniquilado in condutores:
            del condutores[codaniquilado]
            print("Excluido com sucesso.")
        else:
            print("Código não encontrado, tente outro")

    elif opcao == 3: 
        for codigo, nome in condutores.items():
            print(f'{codigo} - {nome}')

    elif opcao == 4:
        codaniquilado = str(input("Digite o código que você quer excluir:")).zfill(3)

        if codaniquilado in veiculos:
            del veiculos[codaniquilado]
            print("Excluido com sucesso.")
        else:
            print("Código não encontrado, tente outro")
    
    elif opcao == 5:
        for codigo, nome in veiculos.items():
            print(f'{codigo} - {nome}')

    elif opcao == 6:
        novcas = str(input("Digite o código do novo cadastrado:")).zfill(3)

        if novcas in veiculos:
            print("Código já existente, tente outro")
        else:
            nomecas = str(input("Digite o nome do novo cadastrado:"))
            veiculos[novcas] = nomecas

    elif opcao == 7:
        codveiculosaiu = str(input("Digite o código do veículo que saiu")).zfill(3)
        if codveiculosaiu in veiculos:
             codcondutorsaiu = str(input("Digite o código do condutor que saiu")).zfill(3)
             if codcondutorsaiu in condutores:
                datasaida = str(input("Digite a data de saída do caminhão(DD/MM/AAAA:)"))
                horasaida = str(input("Digite a hora de saída(HH/MM):"))
                saida = {"veiculo": codveiculosaiu,
                        "condutor": codcondutorsaiu,
                        "data_saida": datasaida,
                        "hora_saida": horasaida,
                        "data_retorno": None,
                        "hora_retorno": None}
                saidas.append (saida)
        else:
            print ("Veiculo não encontrado")

    elif opcao == 8:
        codveiculoretorno = str(input("Digite o código do veículo que retornou")).zfill(3)
        codcondurretorno = str(input("Digite o código do condutor que retornou")).zfill(3)
        for s in saidas:
            if s['veiculo'] == codveiculoretorno and s['condutor'] == codcondurretorno and s['data_retorno'] is None:
                dataretorno = str(input("Digite a data que o veiculo retornou(DD/MM/AAAA)"))
                horaretorno = str(input("Digite a hora que o veiculo retornou (HH/MM)"))
                s['data_retorno'] = dataretorno
                s['hora_retorno'] = horaretorno
                print ("Registrado com sucesso!")
        
    elif opcao == 9 :
        codhistorico = str(input("Digite o código do veículo que vocẽ deseja ver o histórico: ")).zfill(3)
        for s in saidas:
           if s['veiculo'] == codhistorico:
                    print (f"Veiculo: {s['veiculo']}")
                    print (f"Condutor: {condutores[s['condutor']]}")
                    print (f"Data de saída: {s['data_saida']}")
                    print (f"Hora da saída: {s['hora_saida']}")
                    print (f"Data de retorno: {s['data_retorno']}")
                    print (f"Hora de retorno: {s['hora_retorno']}")
                    if s['data_retorno'] is None:
                        print("Veiculo ainda não retornou")
                    else:
                        print("Veiculo retornou")

    elif opcao == 10:
        diaverificar = str(input("Digite a data que você quer verificar as entregas(DD/MM/AAAA): "))
        todos_retornaram = True
        for s in saidas:
         if s['data_retorno'] == diaverificar:
                print (f"Veiculo: {s['veiculo']}")
                print (f"Condutor: {condutores[s['condutor']]}")
                print (f"Data de saída: {s['data_saida']}")
                print (f"Hora da saída: {s['hora_saida']}")
                print (f"Data de retorno: {s['data_retorno']}")
                print (f"Hora de retorno: {s['hora_retorno']}")

         if s['data_saida'] == diaverificar:
                if s['data_retorno'] is None:
                 todos_retornaram = False

        if todos_retornaram:
                  print("Todas as entregas do dia foram realizadas!")
        else:
                  print("Ainda existem caminhões que não retornaram.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
