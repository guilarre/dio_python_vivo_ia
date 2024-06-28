import textwrap

################################## Mensagens ##################################

def menu():
    menu = '''

    =============== MENU ===============

    Selecione a opção desejada:

    [c]\tMenu de cadastro
    [l]\tListar minhas contas
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair

    => '''
    return input(textwrap.dedent(menu))

def menu_cadastro():
    menu_cadastro = """

    ============= CADASTRO =============

    Você selecionou o menu de cadastro. Selecione a opção desejada:

    [u]\tCadastrar usuário
    [c]\tCadastrar conta
    [r]\tRetornar ao menu anterior
    [q]\tSair

    => """
    return input(textwrap.dedent(menu_cadastro))

def msg_extrato(saldo, extrato):
    msg_extrato = f"""\n########### Extrato ###########\n\n{extrato}\nSaldo atual:\tR$ {saldo:.2f}\n\n###############################"""

    return print(msg_extrato)


def msg_erro_extrato(saldo):
    msg_erro_extrato = f"""\n
    ### Não foram realizadas movimentações. ###\n\n
    Saldo atual: R$ {saldo:.2f}\n\n
    ###########################################
    """
    return print(textwrap.dedent(msg_erro_extrato))

#################################### Funções ####################################

def cadastrar_usuario(lista_usuarios):
    print("### Você selecionou a opção para cadastro de usuário. ###\n\n")

    cpf = input("Por favor, informe o CPF do usuário (somente números).\n\n=> ")
    usuario_novo = filtrar_usuario(cpf, lista_usuarios)

    if usuario_novo:
        while True:
            opcao_nova_conta = input("Usuário já existe. Gostaria de criar uma conta nova para esse usuário?\n\nDigite [s] se Sim ou [n] se Não.\n\n=> ")

            if opcao_nova_conta == 's':
                cadastrar_conta(cpf)
            
            elif opcao_nova_conta == 'n':
                break
            
            else:
                print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")
                continue

    else:
        nome = input("Por favor, informe o nome do usuário.\n\n=> ")
        data_nascimento = input("Por favor, informe a data de nascimento do usuário.\n\n=> ")
        endereco = input("Por favor, informe o endereço do usuário (logradouro, nro - bairro - cidade/sigla estado).\n\n=> ")

        lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("\nO usuário foi cadastrado com sucesso!")


def filtrar_usuario(cpf, lista_usuarios):
    usuario_filtrado = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    if usuario_filtrado:
        return usuario_filtrado[0]
    else:
        return None


def cadastrar_conta(agencia, numero_conta, lista_usuarios):
    print("### Você selecionou a opção para cadastro de contas. ###\n\n")

    cpf = input("Por favor, informe o CPF do usuário.\n\n=> ")
    usuario = filtrar_usuario(cpf, lista_usuarios)

    if usuario:
        print("\n### Conta criada com sucesso! ###")
        return {"usuario": usuario, "conta": {"agencia": agencia, "numero_conta": numero_conta}}

    else:
        print("\nUsuário não encontrado. Por favor, cadastre o usuário primeiro.")


def listar_contas(lista_usuarios, lista_contas):
    cpf = input("Por favor, informe o CPF do usuário.\n\n=> ")
    usuario = filtrar_usuario(cpf, lista_usuarios)

    if usuario:
        for conta in lista_contas:
            linha = f"""
                Agência:\t{conta['conta']['agencia']}
                C/c:\t\t{conta['conta']['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))
    else:
        print("O CPF informado não possui contas cadastradas.")


def depositar(valor_deposito, saldo, extrato, /):
    if valor_deposito < 0:
        print("\nInfelizmente, a operação não pôde ser realizada. Não é possível depositar valores negativos.")
    else:
        saldo += valor_deposito
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print("\nOperação realizada com sucesso.")
    
    return saldo, extrato


def sacar(*, valor_saque, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor_saque > limite:
        print("\nInfelizmente, a operação não pôde ser realizada. Valor do saque maior que o limite.")

    elif valor_saque > saldo:
        print("\nInfelizmente, a operação não pôde ser realizada. Saldo insuficiente.")

    elif valor_saque < 0:
        print("\nInfelizmente, a operação não pôde ser realizada. Valor do saque é inválido.")

    elif numero_saques >= LIMITE_SAQUES:
        print("\nInfelizmente, a operação não pôde ser realizada. O limite diário de saques foi atingido.")

    else:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        print("\nOperação realizada com sucesso.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        msg_extrato(saldo, extrato)
    else:
        msg_erro_extrato(saldo)

###################################### Main ######################################

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    lista_usuarios = []
    lista_contas = []
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == 'c':
            while True:
                opcao_cadastro = menu_cadastro()
                if opcao_cadastro == 'u':
                    cadastrar_usuario(lista_usuarios)

                elif opcao_cadastro == 'c':
                    numero_conta = len(lista_contas) + 1
                    conta = cadastrar_conta(AGENCIA, numero_conta, lista_usuarios)
                    
                    if conta:
                        lista_contas.append(conta)
                        print(lista_contas)

                elif opcao_cadastro == 'r':
                    break

                elif opcao_cadastro == 'q':
                    print("\nObrigado por usar nosso serviço.")
                    quit()

                else:
                    print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")

        elif opcao == 'l':
            listar_contas(lista_usuarios, lista_contas)

        elif opcao == 'd':
            while True:
                try:
                    valor_deposito = float(input("Quanto deseja depositar? => "))
                except:
                    print("\nValor inválido. Tente novamente.")
                    continue
                break
            saldo, extrato = depositar(valor_deposito, saldo, extrato)

        elif opcao == 's':
            while True:
                try:
                    valor_saque = float(input("Quanto deseja sacar? => "))
                except:
                    print("\nValor inválido. Tente novamente.")
                    continue
                break

            saldo, extrato, numero_saques = sacar(
                valor_saque=valor_saque,
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'q':
            print("\nObrigado por usar nosso serviço.")
            quit()

        else:
            print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")

main()