menu = """

[d] Depositar
[s] Sacar
[e] Extato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3


def realizar_deposito(l_saldo: float, l_extrato: str) -> tuple[float, str]:
    try:
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0:
            l_saldo += deposito
            l_extrato += f"\n + R$ {deposito:.2f}"
        else:
            print("Operação falhou! Valor inválido.")
    except ValueError:
        print("Operação falhou! Valor não é um número.")

    return l_saldo, l_extrato


def realizar_saque(l_saldo: float, l_extrato: str, l_num_saques: int, l_limite: float) -> tuple[float, str, int]:
    try:
        saque = float(input("Digite o valor do saque: "))
        if num_saques >= LIMITE_SAQUES:
            print("Operação falhou! Você excedeu o limite de saques diários.")
        elif saque > limite:
            print("Operação falhou! Limite do valor de saque excedido.")
        elif (l_saldo - saque) < 0:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif (l_saldo - saque) >= 0 and saque > 0:
            l_saldo -= saque
            l_extrato += f"\n - R$ {saque:.2f}"
            l_num_saques += 1
        else:
            print("Operação falhou! Valor inválido.")
    except ValueError:
        print("Operação falhou! Valor não é um número.")

    return l_saldo, l_extrato, l_num_saques


def exibir_extrato(extrato: str) -> None:
    print("******** EXTRATO ********")
    print(extrato)
    print(f"\n Saldo: R$ {saldo:.2f}\n")
    print("*************************")


while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = realizar_deposito(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, num_saques = realizar_saque(saldo, extrato, num_saques, limite)
    elif opcao == "e":
        exibir_extrato(extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida! por favor selecione novamente a operação desejada.")
