#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

class ContaBancaria:
    _total_contas = 0
    def __init__(self, titular, saldo, status=False) -> None:
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = status
        ContaBancaria._total_contas += 1
    def __str__(self) -> str:
        return f'{self._titular} | R$:{self._saldo} | {self._ativo}'
    
    
    def alternar_estado(self):
        self._ativo = True
    @classmethod
    def total_contas(cls):
        return cls._total_contas

#Crie duas instâncias da classe e imprima essas instâncias
conta1 = ContaBancaria('moises', 1050)
conta2 = ContaBancaria('silvana', 50)
print(conta1)
print(conta2)
print()
#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
conta1.alternar_estado()
print(f'{conta1}')
print(f'Total de contas: {ContaBancaria.total_contas()}')

#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
#  Crie uma instância da classe e imprima o valor da propriedade titular.
conta3 = ContaBancariaPythonica("Fernanda", 1500)
print(f"Titular da conta 3: {conta3.titular}")

#Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
#Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:
    # ... (outros métodos e atributos)

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")