menu = '''

Selecione a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Quanto deseja depositar? => "))
        if valor_deposito < 0:
            print("\nInfelizmente, a operação não pôde ser realizada. Não é possível depositar valores negativos.")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("\nOperação realizada com sucesso.")
        continue

    elif opcao == 's':
        valor_saque = float(input("Quanto deseja sacar? => "))
        if valor_saque >= saldo:
            print("\nInfelizmente, a operação não pôde ser realizada. Saldo insuficiente.")

        elif valor_saque > limite:
            print("\nInfelizmente, a operação não pôde ser realizada. Valor do saque maior que o limite.")

        elif valor_saque < 0:
            print("\nInfelizmente, a operação não pôde ser realizada. Valor do saque é inválido.")

        elif numero_saques >= LIMITE_SAQUES:
            print("\nInfelizmente, a operação não pôde ser realizada. O limite diário de saques foi atingido.")

        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print("\nOperação realizada com sucesso.")
        continue

    elif opcao == 'e':
        if extrato:
            print(f"""

########### Extrato ###########

{extrato}
Saldo atual: R$ {saldo:.2f}

###############################
""")
        else:
            print("\n## Não foram realizadas movimentações. ##")
        continue

    elif opcao == 'q':
        print("\nObrigado por usar nosso serviço.")
        break

    else:
        print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")
        continue