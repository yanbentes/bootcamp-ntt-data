# Desafio DIO Sistema Bancário Simples

Este projeto implementa um sistema bancário simples, onde o usuário pode realizar operações como depósito, saque, e visualizar o extrato. O sistema foi desenvolvido em Python.

## Funcionalidades

- **Depósito:** O usuário pode inserir um valor para ser depositado na conta. O sistema valida o valor para garantir que seja positivo e numérico.
- **Saque:** O usuário pode sacar um valor, desde que tenha saldo suficiente e não exceda o limite diário de saques. O sistema valida o valor do saque e as condições de saldo e limites.
- **Extrato:** O usuário pode visualizar o extrato das operações realizadas, assim como o saldo atual.
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
[d] Depositar
[s] Sacar
[e] Exibir Extrato
[q] Sair

=>
```
