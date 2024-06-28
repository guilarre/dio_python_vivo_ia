class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado): # Sobrescrevendo o init para conter +1 atributo
        super().__init__(cor, placa, numero_rodas) # Inicializando os mesmos atributos da classe pai
        self.carregado = carregado # Novo atributo

    def esta_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não'} estou carregado")

caminhao = Caminhao("roxo", "gfd-8712", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)