class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = plano.custo_chamada(duracao)

        if custo <= plano.verificar_saldo():
            plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${plano.verificar_saldo():.2f}"

        else:
            return "Saldo insuficiente para fazer a chamada."


class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, plano):
        super().__init__(nome, numero, plano)
        self.saldo = self.plano.saldo


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao):
        return duracao * 0.1

    def deduzir_saldo(self, custo):
        self.saldo -= custo


nome = input()
numero = input()
saldo_inicial = float(input())

plano = Plano(saldo_inicial)
usuario_pre_pago = UsuarioPrePago(nome, numero, plano)

destinatario = input()
duracao = int(input())

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
