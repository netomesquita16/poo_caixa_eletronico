from contas import Banco, ContaCorrente, ContaPoupanca
from clientes import Cliente

def main():
    banco = Banco("Banco Central POO")
    contador_contas = 1

    while True:
        print("\n" + "="*30)
        print("====== CAIXA ELETRÔNICO ======")
        print("1 - Criar Conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar Saldo")
        print("5 - Histórico")
        print("0 - Sair")
        print("="*30)

        opcao = input("Escolha uma opção: ")
        

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            cliente = Cliente(nome, cpf)

            print("Tipo de Conta:")
            print("1 - Conta-Corrente")
            print("2 - Conta-Poupança")
            tipo = input("Escolha: ")

            numero_conta = contador_contas
            contador_contas += 1

            if tipo == '1':
                conta = ContaCorrente(numero_conta, cliente)
                banco.adicionar_conta(conta)
                print(f"\n Conta-Corrente criada com sucesso! O número da sua conta é {numero_conta}")
            elif tipo == '2':
                conta = ContaPoupanca(numero_conta, cliente)
                banco.adicionar_conta(conta)
                print(f"\n Conta-Poupança criada com sucesso! O número da sua conta é {numero_conta}")
            else:
                print("\n Tipo de conta inválido.")

        elif opcao in ['2', '3', '4', '5']:
            try:
                num_conta = int(input("\nDigite o número da conta: "))
                conta = banco.buscar_conta(num_conta)

                if not conta:
                    print("\n Conta não encontrada.")
                    continue

                if opcao == '2': 
                    valor = float(input("Digite o valor para depósito: R$ "))
                    conta.depositar(valor)
                
                elif opcao == '3': 
                    valor = float(input("Digite o valor para saque: R$ "))
                    conta.sacar(valor)

                elif opcao == '4': 
                    print(f"\n Saldo atual da conta {conta.numero} \nTitular: {conta.cliente.nome}: R$ {conta.saldo:.2f}")

                elif opcao == '5': 
                    print(f"\n=== HISTÓRICO === \n Conta Nº: {conta.numero} - Titular: {conta.cliente.nome} ")
                    conta.historico.imprimir()

            except ValueError:
                print("\n Entrada inválida. Digite valores numéricos quando solicitado.")

        elif opcao == '0':
            print("\n Encerrando o sistema. Até breve!")
            break

        else:
            print("\n Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()