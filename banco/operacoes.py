from datetime import datetime

class Operacao:
    def __init__(self, tipo: str, valor: float):
        self.__tipo = tipo
        self.__valor = valor
        self.__data = datetime.now()

    def __str__(self):
        return f"[{self.__data.strftime('%d/%m/%Y %H:%M:%S')}] {self.__tipo}: R$ {self.__valor:.2f}"

class Historico:
    def __init__(self):
        self.__operacoes = []

    def adicionar_operacao(self, operacao: Operacao):
        self.__operacoes.append(operacao)

    def imprimir(self):
        if not self.__operacoes:
            print("Nenhuma operação registrada.")
        else:
            for op in self.__operacoes:
                print(op)