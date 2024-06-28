class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Trim-trim")
    
    def parar(self):
        print("Freiando bicicleta ...")
        print("Bicicleta parada.")
    
    def correr(self):
        print("Pedalando ...")
        print("Zum-zum")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

caloi_1 = Bicicleta("vermelha", "C-123-V", 2022, 600)
# caloi_1.buzinar()
# caloi_1.parar()
# caloi_1.correr()
# print(caloi_1.cor, caloi_1.modelo, caloi_1.ano, caloi_1.valor)

print(caloi_1)