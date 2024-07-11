# Variáveis globais
saldo = 0.0
depositos = []
saques = []
saques_diarios = 0

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")

def sacar(valor):
    global saldo, saques_diarios
    if saques_diarios >= 3:
        print("Limite diário de saques atingido.")
        return
    if valor > 500:
        print("O valor máximo por saque é de R$ 500.00.")
        return
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return

    saldo -= valor
    saques.append(valor)
    saques_diarios += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def extrato():
    print("\nExtrato:")
    print("Depósitos:")
    for deposito in depositos:
        print(f"R$ {deposito:.2f}")
    print("Saques:")
    for saque in saques:
        print(f"R$ {saque:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")

def novo_dia():
    global saques_diarios
    saques_diarios = 0
    print("Novo dia iniciado. Contador de saques diários resetado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Novo Dia")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depositar: "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para sacar: "))
            sacar(valor)
        elif opcao == "3":
            extrato()
        elif opcao == "4":
            novo_dia()
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamar o menu para iniciar o programa
menu()
