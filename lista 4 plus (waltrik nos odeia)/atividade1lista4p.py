'''1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
professores já cadastrados no sistema de uso dos laboratórios.
O sistema deve possuir:
• Um cadastro completo de professores (adicionar, alterar, excluir e listar) que
associe o código do professor ao seu nome, alguns professores já devem ser précadastrados, veja a lista abaixo;
• Um cadastro completo dos acessos dos professores aos laboratórios (adicionar,
alterar, excluir e listar), serão utilizados 6 laboratórios com as nomenclaturas
Lab102, Lab103, Lab104, Lab105, Lab106, Lab107 – os laboratórios são fixos no
sistema, o que pode ser alterado são os acessos, alguns professores já devem
ser pré-cadastrados nos laboratórios, veja a outra lista abaixo (para facilitar a
implementação, sugere-se que os laboratórios sejam associados ao código do
professor e não ao seu nome);
• Teste de acesso ao laboratório: deve ser possível informar o nome de um
laboratório e um código de professor para verificar se o acesso é permitido ou não
(por exemplo, nesse teste deveria ser possível escolher o Lab103 e informar o
código de professor 002, nesse caso, o sistema deve negar o acesso).
Pré-cadastro de Professores (códigos x nomes)
001 – Prof Thiago Paes
002 – Prof Schalata
003 – Prof Ignácio
004 – Prof Ryan
005 – Prof André
006 – Profª Fabiana
007 – Prof Alberto
008 – Prof Juliano
009 – Prof Thiago Waltrik
010 – Prof João Eduardo
Pré-cadastro de Acessos (laboratório x professor)
• Lab102 – Prof Ignácio, Prof Thiago Paes, Profª Ryan, Prof André, Profª
Fabiana;
• Lab103 – Prof Alberto;
• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;
• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof
João Eduardo.'''

profs = {   '001' : "Prof Thiago Paes",
'002' : "Prof Schalata",
'003' : "Prof Ignácio",
'004' : "Prof Ryan",
'005' : "Prof André",
'006' : "Profª Fabiana",
'007' : "Prof Alberto",
'008' : "Prof Juliano",
'009' : "Prof Thiago Waltrik",
'010' : "Prof João Eduardo"}

lab102 = ['003', '001', '004', '005', '006']

lab103 = ['007']

lab104 = ['004','002', '008', '005']

lab105 = ['003','001', '007', '009']

lab106 = ['003','001','002','009']

lab107 = ['010','001','009','005','002']


while True:
    print("Acesso a laboratórios:")
    print("-----------")
    print("1 – Cadastrar professor")
    print("2 – Excluir professor")
    print("3 – Listar professor")
    print("5 - Teste de acesso")
    print("6 - Excluir acesso laboratórios:")
    print("7 - Listar acesso laboratórios:")
    print("8 - Cadastrar acesso laboratórios:")
    print("0 – Sair")

    opcao = int(input("Digite a opção que você quer:"))

    if opcao == 0:
        break

    elif opcao == 1:

        novcas = str(input("Digite o código do novo cadastrado:")).zfill(3)

        if novcas in profs:
            print("Código já existente, tente outro")
        else:
            nomecas = str(input("Digite o nome do novo cadastrado:"))
            profs[novcas] = nomecas


    elif opcao == 2:

        codaniquilado = str(input("Digite o código que você quer excluir:")).zfill(3)

        if codaniquilado in profs:
            del profs[codaniquilado]
            print("Excluido com sucesso.")
        else:
            print("Código não encontrado, tente outro")


    elif opcao == 3:

        for codigo, nome in profs.items():
            print(f'{codigo} - {nome}')


    elif opcao == 5:

        print("1 – lab102")
        print("2 – lab103")
        print("3 – lab104")
        print("4 – lab105")
        print("5 - lab106")
        print("6 - lab107")

        codtestar = int(input("Digite o laboratório a ser testado:"))

        if codtestar == 1:
            codtestar = lab102
        elif codtestar == 2:
            codtestar = lab103
        elif codtestar == 3:
            codtestar = lab104
        elif codtestar == 4:
            codtestar = lab105
        elif codtestar == 5:
            codtestar = lab106
        elif codtestar == 6:
            codtestar = lab107
        else:
            print("Laboratório inválido")
            continue

        proftestar = str(input("Digite o código do professor a ser testado:")).zfill(3)

        if proftestar in codtestar:
            print("Acesso permitido")
        else:
            print("Acesso negado")


    elif opcao == 8:

        print("1 – lab102")
        print("2 – lab103")
        print("3 – lab104")
        print("4 – lab105")
        print("5 - lab106")
        print("6 - lab107")

        codtestar = int(input("Digite o laboratório para cadastrar um acesso:"))

        codnovo = str(input("Digite o código do professor a ser adicionado:")).zfill(3)

        if codnovo not in profs:
            print("Código inválido")
            continue

        if codtestar == 1:
            lab102.append(codnovo)

        elif codtestar == 2:
            lab103.append(codnovo)

        elif codtestar == 3:
            lab104.append(codnovo)

        elif codtestar == 4:
            lab105.append(codnovo)

        elif codtestar == 5:
            lab106.append(codnovo)

        elif codtestar == 6:
            lab107.append(codnovo)

        else:
            print("Laboratório inválido")


    elif opcao == 7:

        print("1 – lab102")
        print("2 – lab103")
        print("3 – lab104")
        print("4 – lab105")
        print("5 - lab106")
        print("6 - lab107")

        codtestar = int(input("Digite o laboratório a ter os acessos listados:"))

        if codtestar == 1:
            print(lab102)

        elif codtestar == 2:
            print(lab103)

        elif codtestar == 3:
            print(lab104)

        elif codtestar == 4:
            print(lab105)

        elif codtestar == 5:
            print(lab106)

        elif codtestar == 6:
            print(lab107)

        else:
            print("Código inválido")


    elif opcao == 6:

        print("1 – lab102")
        print("2 – lab103")
        print("3 – lab104")
        print("4 – lab105")
        print("5 - lab106")
        print("6 - lab107")

        codtestar = int(input("Digite o laboratório para excluir um acesso:"))

        codnovo = str(input("Digite o código a ser excluído nesta sala:")).zfill(3)

        if codtestar == 1:

            if codnovo in lab102:
                lab102.remove(codnovo)
                print("Acesso excluído com sucesso.")
            else:
                print("Esse professor não possui acesso a este laboratório.")

        elif codtestar == 2:

            if codnovo in lab103:
                lab103.remove(codnovo)
                print("Acesso excluído com sucesso.")
            else:
                print("Esse professor não possui acesso a este laboratório.")

        elif codtestar == 3:

            if codnovo in lab104:
                lab104.remove(codnovo)
                print("Acesso excluído com sucesso.")
            else:
                print("Esse professor não possui acesso a este laboratório.")

        elif codtestar == 4:

            if codnovo in lab105:
                lab105.remove(codnovo)
                print("Acesso excluído com sucesso.")
            else:
                print("Esse professor não possui acesso a este laboratório.")

        elif codtestar == 5:

            if codnovo in lab106:
                lab106.remove(codnovo)
                print("Acesso excluído com sucesso.")
            else:
                print("Esse professor não possui acesso a este laboratório.")

        elif codtestar == 6:

            if codnovo in lab107:
                lab107.remove(codnovo)
                print("Acesso excluído com sucesso.")
            else:
                print("Esse professor não possui acesso a este laboratório.")

        else:
            print("Laboratório inválido")
