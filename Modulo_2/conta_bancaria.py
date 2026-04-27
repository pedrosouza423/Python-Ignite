class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        
    def sacar(self, valor):
        if(valor > 0 and valor <= self.__saldo):
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")

    def obterSaldo(self):
        print(f"Saldo atual: R${self.__saldo}")

    
conta = ContaBancaria()
conta.obterSaldo()  # Saída: 0
conta.depositar(100)
conta.obterSaldo()  # Saída: 100
conta.sacar(30)
conta.obterSaldo()  # Saída: 70
