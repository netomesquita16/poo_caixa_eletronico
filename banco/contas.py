from abc import ABC, abstractmethod
from clientes import Cliente
from operacoes import Historico, Operacao

class Conta(ABC):
    def __init__(self, numero: int, cliente: Cliente):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__historico = Historico() 

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float):
        self.__saldo = valor

    @property
    def historico(self):
        return self.__historico

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_operacao(Operacao("Depósito", valor))
            print("\n Depósito realizado com sucesso!")
        else:
            print("\n Valor de depósito inválido.")

    @abstractmethod
    def sacar(self, valor: float):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.0):
        super().__init__(numero, cliente)
        self.__limite = limite

    def sacar(self, valor: float):
        if valor <= 0:
            print("\n Valor inválido para saque.")
            return False

        saldo_disponivel = self.saldo + self.__limite
        if valor > saldo_disponivel:
            print(f"\n Saldo insuficiente. Seu limite disponível é R$ {saldo_disponivel:.2f}")
            return False

        self.saldo -= valor
        self.historico.adicionar_operacao(Operacao("Saque Conta-Corrente", valor))
        print("\n Saque realizado com sucesso!")
        return True

class ContaPoupanca(Conta):
    def __init__(self, numero: int, cliente: Cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor: float):
        if valor <= 0:
            print("\n Valor inválido para saque.")
            return False

        if valor > self.saldo:
            print(f"\n Saldo insuficiente. Saldo disponível: R$ {self.saldo:.2f}")
            return False

        self.saldo -= valor
        self.historico.adicionar_operacao(Operacao("Saque Poupança", valor))
        print("\n Saque realizado com sucesso!")
        return True

class Banco:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__contas = [] 

    def adicionar_conta(self, conta: Conta):
        self.__contas.append(conta)

    def buscar_conta(self, numero: int) -> Conta:
        for conta in self.__contas:
            if conta.numero == numero:
                return conta
        return None