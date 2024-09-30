# Desafio DIO Sistema Bancário

Este projeto implementa um sistema bancário simples, onde o usuário pode realizar operações como depósito, saque, criação de usuários, criação de contas, visualização de contas e extrato. O sistema foi desenvolvido em Python.

## Funcionalidades

- **Depósito:** O usuário pode inserir um valor para ser depositado na conta. O sistema valida o valor para garantir que seja positivo e numérico.
- **Saque:** O usuário pode sacar um valor, desde que tenha saldo suficiente, não exceda o limite de saque, e não tenha ultrapassado o número máximo de saques diários.
- **Extrato:** O usuário pode visualizar o extrato das operações realizadas, assim como o saldo atual.
- **Criação de Usuário:** Permite cadastrar um novo usuário com nome, CPF, data de nascimento e endereço.
- **Criação de Conta:** Permite criar uma nova conta bancária associada a um usuário existente (CPF obrigatório).
- **Listar Contas:** Exibe todas as contas criadas, incluindo agência, número da conta e nome do titular.
- **Encerrar:** O usuário pode encerrar o programa a qualquer momento.

## Requisitos

- Python 3.x

## Como Executar

1. Clone o repositório ou faça o download dos arquivos do projeto.
2. Navegue até o diretório do projeto.
3. Execute o programa com o comando:

    ```bash
    python app.py
    ```

4. O menu interativo será exibido, e você poderá escolher as operações disponíveis.

## Exemplo de Uso

Ao executar o programa, será exibido um menu com as seguintes opções:

```bash
********* MENU **********

[d]  Depositar
[s]  Sacar
[e]  Exibir Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuário
[q]  Sair

=>
```

## Observações
- O limite de saque diário é de 3 saques.
- O limite de valor por saque é de R$500,00.
- O sistema exige que o usuário seja cadastrado antes da criação de uma conta.
- O extrato inclui todas as operações realizadas, tanto depósitos quanto saques, e o saldo é atualizado em tempo real.
