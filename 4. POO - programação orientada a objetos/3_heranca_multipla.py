class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

# class Gato(Mamifero):
#     pass

# gato = Gato(numero_patas=4, cor_pelo="preto")
# print(gato)

# class Ornitorrinco(Mamifero, Ave):
#     def __init__(self, **kw):
#         super().__init__(**kw)

# ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo="marrom", cor_bico="preto")
# print(ornitorrinco)

##############################################################

## SEM MIXIN:

# class Ave(Animal):
#     def __init__(self, cor_bico, falante=False, **kw):
#         super().__init__(**kw)
#         self.cor_bico = cor_bico
#         self.falante = falante
    
#     def falar(self):
#         if self.falante == True:
#             return "Eu estou falando!"

# corvo = Corvo(numero_patas=2, cor_bico="preto", falante=True)
# print(corvo.falar())

## COM MIXIN:

# Cria mixin:

class FalanteMixin:
    def falar(self):
        return "Eu estou falando!"

# Coloca mixin como herança:

class Corvo(Ave, FalanteMixin):
    def __init__(self, **kw):
        super().__init__(**kw)

# Não precisa colocar como atributo:

corvo = Corvo(numero_patas=2, cor_bico="preto")
print(corvo.falar())