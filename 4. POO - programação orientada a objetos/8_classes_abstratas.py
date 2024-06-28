from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass

    # Pra trabalhar com setters abstratos,
    # tem que ser dessa maneira indireta:

    @marca.setter
    def marca(self, value):
        self._marca_setter(value)

    @abstractmethod
    def _marca_setter(self, value):
        pass


class ControleTV(ControleRemoto):
    def __init__(self, marca='LG'):
        self._marca = marca

    def ligar(self):
        print("Ligando a TV...")
        print("TV ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, value):
        self._marca_setter(value)

    def _marca_setter(self, value):
        self._marca = value


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle.marca = 'Philco'
print(controle.marca)