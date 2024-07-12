from datetime import datetime, timedelta

data_atual = datetime.now()

tipo_carro = input("Escolha o tipo de carro. (P, M ou G). => ") # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou às: {data_atual.strftime("%d-%m-%Y %H:%M:%S")} e ficará pronto às {data_estimada.strftime("%d-%m-%Y %H:%M:%S")}.")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou às: {data_atual.strftime("%d-%m-%Y %H:%M:%S")} e ficará pronto às {data_estimada.strftime("%d-%m-%Y %H:%M:%S")}.")
elif tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou às: {data_atual.strftime("%d-%m-%Y %H:%M:%S")} e ficará pronto às {data_estimada.strftime("%d-%m-%Y %H:%M:%S")}.")