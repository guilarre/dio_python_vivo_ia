class MeuIterador:
    def __init__(self, numeros: list[int]): ## o : list[int] é só uma anotação p indicar qual é o tipo de dado
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[1, 2, 3]):
    print(i)