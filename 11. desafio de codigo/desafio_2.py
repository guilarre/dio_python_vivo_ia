class UsuarioTelefone:
    def __init__(self, nome, plano):
        self._nome = nome
        self._plano = plano

    @property
    def nome(self):
        return self._nome

    @property
    def plano(self):
        return self._plano

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


class PlanoTelefone(UsuarioTelefone):
    def __init__(self, nome, plano, saldo):
        super().__init__(nome, plano)
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def verificar_saldo(self):
        if self.saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


nome = input()
plano = input()
saldo = float(input())

plano = PlanoTelefone(nome, plano, saldo)
print(plano.verificar_saldo())
