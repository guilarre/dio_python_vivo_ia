class Conta:
    def __init__(self, num_agencia, saldo=0):
        self._saldo = saldo
        self.num_agencia = num_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        # ... (regras de autenticação e outras verificações)
        return self._saldo

    # def __str__(self):
    #     return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.mostrar_saldo)
print(conta.num_agencia)