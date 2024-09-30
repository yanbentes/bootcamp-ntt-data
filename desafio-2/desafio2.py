def realizar_deposito(saldo: float, deposito: float, extrato: str, /) -> tuple[float, str]:
    if deposito > 0:
        saldo += deposito
        extrato += f"\n + R$ {deposito:.2f}"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\n!!! Operação falhou! Valor inválido !!!")

    return saldo, extrato


def realizar_saque(*, saldo: float, saque: float, extrato: str, limite: float, num_saques: int, limite_saques: int) -> tuple[float, str]:
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = num_saques >= limite_saques

    if excedeu_saques:
        print("\n!!! Operação falhou! Você excedeu o limite de saques diários !!!")
    elif excedeu_limite:
        print("\n!!! Operação falhou! Limite do valor de saque excedido !!!")
    elif excedeu_saldo:
        print("\n!!! Operação falhou! Você não tem saldo suficiente !!!")
    elif saque > 0:
        saldo -= saque
        extrato += f"\n - R$ {saque:.2f}"
        num_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\n!!! Operação falhou! Valor inválido !!!")

    return saldo, extrato


def exibir_extrato(extrato: str) -> None:
    print("******** EXTRATO ********")
    print(extrato)
    print(f"\n Saldo: R$ {saldo:.2f}\n")
    print("*************************")


def criar_usuario(usuarios: list) -> None:
    cpf = input("Digite seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n!!! Este CPF já foi cadastrado !!!")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso.")


def filtrar_usuario(cpf: int, usuarios: list) -> list:
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia: str, numero_conta: int, usuarios: list) -> list or None:
    cpf = input("Digite seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n!!! Usuário não encontrado, falha na criação de conta !!!")


def listar_contas(contas: list) -> None:
    for conta in contas:
        conta = (
            f"""\nAgencia:\t{conta['agencia']}"""
            f"""\nC/C:\t\t{conta['numero_conta']}"""
            f"""\nTitular:\t{conta['usuario']['nome']}"""
        )
        print(conta)


menu = """
********* MENU **********

[d]\tDepositar
[s]\tSacar
[e]\tExtato
[nc]\tNova conta
[lc]\tListar Contas
[nu]\tNovo usuário
[q]\tSair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
contas = []
usuarios = []

LIMITE_SAQUES = 3
AGENCIA = "0001"

while True:
    opcao = input(menu)

    if opcao == "d":
        try:
            deposito = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = realizar_deposito(saldo, deposito, extrato)
        except ValueError:
            print("\n!!! Operação falhou! Valor não é um número !!!")
    elif opcao == "s":
        try:
            saque = float(input("Digite o valor do saque: "))
            saldo, extrato = realizar_saque(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES
            )
        except ValueError:
            print("\n!!! Operação falhou! Valor não é um número !!!")
    elif opcao == "e":
        exibir_extrato(extrato)
    elif opcao == "nu":
        criar_usuario(usuarios)
    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    elif opcao == "lc":
        listar_contas(contas)
    elif opcao == "q":
        break
    else:
        print("\n!!! Operação inválida! por favor selecione novamente a operação desejada !!!")
