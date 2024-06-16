def recomendar_plano(consumo):
    if consumo <= 10:
        return print("Plano Essencial Fibra - 50Mbps")
    elif consumo > 10 and consumo <= 20:
        return print("Plano Prata Fibra - 100Mbps")
    else:
        return print("Plano Premium Fibra - 300Mbps")

def main():
    consumo = float(input())
    recomendar_plano(consumo)

main()