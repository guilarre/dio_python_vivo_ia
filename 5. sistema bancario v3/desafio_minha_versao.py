import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

#################################### Classes ####################################

class Cliente:
    def __init__(self):
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, endereco, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = cpf
        self.contas = []


class Conta:
    def __init__(self, usuario, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._usuario = usuario
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, usuario, numero):
        return cls(usuario, numero)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def usuario(self):
        return self._usuario
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\nInfelizmente, a operação não pôde ser realizada. Valor do saque maior que o saldo.")
        
        elif valor > 0:
            self._saldo -= valor
            print("\nOperação realizada com sucesso.")
            return True
        
        else:
            print("\nInfelizmente, a operação não pôde ser realizada. Valor do saque é inválido.")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nOperação realizada com sucesso.")
        
        else:
            print("\nInfelizmente, a operação não pôde ser realizada. O valor informado é inválido.")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, usuario, numero, limite=500, limite_saques=3):
        super().__init__(usuario, numero)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\nInfelizmente, a operação não pôde ser realizada. Valor do saque maior que o limite.")
        
        elif excedeu_saques:
            print("\nInfelizmente, a operação não pôde ser realizada. O limite diário de saques foi atingido.")

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""
            Agência:\t\t\t{self.agencia}
            Conta:\t\t\t\t{self.numero}
            Titular:\t\t\t{self.usuario.nome}
            Limite de valor de saque:\tR$ {self.limite}
            Limite de saques diário:\t{self.limite_saques}x
        """

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques
    
    @property
    def numero(self):
        return self._numero


class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



#################################### Funções ####################################

def cadastrar_usuario(usuarios):
    print("### Você selecionou a opção para cadastro de usuário. ###\n\n")

    cpf = ''
    while cpf == '':
        cpf = input("Por favor, informe o CPF do usuário (somente números).\n\n=> ")

    usuario_existe = filtrar_usuario(cpf, usuarios)

    if usuario_existe:
        print("\nUsuário já existe. Por favor, crie uma conta para este usuário através do menu principal.")
        return

    else:
        nome, data_nascimento, endereco = '', '', ''

        while nome == '':
            nome = input("Por favor, informe o nome do usuário.\n\n=> ")

        while data_nascimento == '':
            data_nascimento = input("Por favor, informe a data de nascimento do usuário.\n\n=> ")

        while endereco == '':
            endereco = input("Por favor, informe o endereço do usuário (logradouro, nro - bairro - cidade/sigla estado).\n\n=> ")

        usuario = PessoaFisica(nome, data_nascimento, endereco, cpf)
        usuarios.append(usuario)

        print("\nO usuário foi cadastrado com sucesso!")

    ## feat: tentar entender como retornar direto para a opção de cadastrar conta sem ter que fazer tudo dentro desta função. 

    # if usuario_existe:
    #     while True:
    #         opcao_nova_conta = input("Usuário já existe. Gostaria de criar uma conta nova para esse usuário?\n\nDigite [s] se Sim ou [n] se Não.\n\n=> ")

    #         if opcao_nova_conta == 's':
    #             cadastrar_conta(cpf, usuarios)
            
    #         elif opcao_nova_conta == 'n':
    #             break
            
    #         else:
    #             print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")
    #             continue


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario.cpf == cpf]
    if usuario_filtrado:
        return usuario_filtrado[0]
    else:
        return None


def recuperar_conta_usuario(usuario):
    if not usuario.contas:
        print("\nUsuário não possui contas!")
        return
    
    else:
        return usuario.contas[0]


def cadastrar_conta(numero_conta, usuarios, contas):
    print("### Você selecionou a opção para cadastro de contas. ###\n\n")

    cpf = ''
    while cpf == '':
        cpf = input("Por favor, informe o CPF do usuário.\n\n=> ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### Conta criada com sucesso! ###")
        
        conta = ContaCorrente.nova_conta(usuario=usuario, numero=numero_conta)
        usuario.adicionar_conta(conta)
        
        # adicionar conta pra lista externa usada p/ contagem do numero de conta
        contas.append(conta)

    else:
        print("\nUsuário não encontrado. Por favor, cadastre o usuário primeiro.")


def listar_contas(usuarios):
    cpf = ''
    while cpf == '':
        cpf = input("Por favor, informe o CPF do usuário.\n\n=> ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        if len(usuario.contas) != 0:
            for conta in usuario.contas:
                print("=" * 100)
                print(textwrap.dedent(str(conta)))
        
        else:
            print("\nO CPF informado não possui contas cadastradas.")

    else:
        print("\nO CPF informado não possui cadastro.")
        return

## fixme: tem que selecionar para qual conta quer fazer depósito caso haja mais de 1 conta por user
def depositar(usuarios):
    cpf = ''
    while cpf == '':
        cpf = input("Por favor, informe o CPF do usuário.\n\n=> ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        try:
            valor = float(input("Quanto deseja depositar? => "))
        except:
            print("\nValor inválido. Tente novamente.")
            
        transacao = Deposito(valor)
        conta = recuperar_conta_usuario(usuario) ## fixme: se tiver + de 1 conta?

        if conta:
            usuario.realizar_transacao(conta, transacao)

        else:
            print("\nErro! Usuário não possui contas.")
            return

    else:
        print("\nErro! Usuário não encontrado!")
        return


def sacar(usuarios):
    cpf = ''
    while cpf == '':
        cpf = input("Por favor, informe o CPF do usuário.\n\n=> ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        try:
            valor = float(input("Quanto deseja sacar? => "))
        except:
            print("\nValor inválido. Tente novamente.")

        transacao = Saque(valor)
        conta = recuperar_conta_usuario(usuario) ## se tiver + de 1 conta?

        if conta:
            usuario.realizar_transacao(conta, transacao)

        else:
            print("\nErro! Usuário não possui contas.")
            return

    else:
        print("\nErro! Usuário não encontrado!")
        return


def exibir_extrato(usuarios):
    cpf = ''
    while cpf == '':
        cpf = input("Por favor, informe o CPF do usuário.\n\n=> ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = recuperar_conta_usuario(usuario)

        if conta:
            transacoes = conta.historico.transacoes
            extrato = ''

            ## problema no espaçamento pra deposito vs. saque (teria que fazer um condicional pra colocar +1 tab para saque)
            if transacoes:
                for transacao in transacoes:
                    extrato += f"\n{transacao['tipo']}:\t\tR$ {transacao['valor']:.2f}"

            else:
                extrato = "\nNão foram realizadas movimentações nesta conta."
                return

            print("\n================ EXTRATO ================")
            print(extrato)
            print("===========================================")

        else:
            print("\nErro! Usuário não possui contas.")
            return
    
    else:
        print("\nErro! Usuário não encontrado!")
        return


################################## Mensagens ##################################

def menu():
    menu = '''

    =============== MENU ===============

    Selecione a opção desejada:

    [c]\tMenu de cadastro
    [l]\tListar minhas contas
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair

    => '''
    return input(textwrap.dedent(menu))

def menu_cadastro():
    menu_cadastro = """

    ============= CADASTRO =============

    Você selecionou o menu de cadastro. Selecione a opção desejada:

    [u]\tCadastrar usuário
    [c]\tCadastrar conta
    [r]\tRetornar ao menu anterior
    [q]\tSair

    => """
    return input(textwrap.dedent(menu_cadastro))


###################################### Main ######################################

def main():
    usuarios = []

    # lista usada apenas para a contagem dos numeros de conta
    contas = []

    while True:
        opcao = menu()

        if opcao == 'c':
            while True:
                opcao_cadastro = menu_cadastro()

                if opcao_cadastro == 'u':
                    cadastrar_usuario(usuarios)

                elif opcao_cadastro == 'c':
                    numero_conta = len(contas) + 1
                    cadastrar_conta(numero_conta, usuarios, contas)

                elif opcao_cadastro == 'r':
                    break

                elif opcao_cadastro == 'q':
                    print("\nObrigado por usar nosso serviço.")
                    quit()

                else:
                    print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")

        elif opcao == 'l':
            listar_contas(usuarios)

        elif opcao == 'd':
            depositar(usuarios)

        elif opcao == 's':
            sacar(usuarios)

        elif opcao == 'e':
            exibir_extrato(usuarios)

        elif opcao == 'q':
            print("\nObrigado por usar nosso serviço.")
            quit()

        else:
            print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")

main()