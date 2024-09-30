# Sistema Bancário - README

Este é um projeto de um simples sistema bancário implementado em Python, que permite criar clientes, contas e realizar operações básicas como depósitos, saques e consulta de extrato. Abaixo, você encontrará uma descrição das funcionalidades e como utilizar o sistema.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- **Criação de clientes**: É possível criar clientes do tipo pessoa física, armazenando informações como CPF, nome, data de nascimento e endereço.
- **Criação de contas**: Um cliente pode possuir uma ou mais contas correntes, que são associadas a ele no momento de criação.
- **Depósitos e saques**: As operações de depósito e saque são realizadas a partir do CPF do cliente, permitindo movimentar o saldo da conta associada.
- **Consulta de extrato**: Exibe todas as transações (depósitos e saques) realizadas na conta de um cliente, bem como o saldo atual.
- **Listagem de contas**: Lista todas as contas criadas no sistema, exibindo informações como agência, número da conta e titular.

## Estrutura do Projeto

- **Cliente e Pessoa Física**: Classes que representam clientes, com a `PessoaFisica` herdando de `Cliente`.
- **Conta e Conta Corrente**: A classe `Conta` representa uma conta bancária, enquanto a `ContaCorrente` adiciona regras específicas para saque, como limite de valor e número de saques diários.
- **Transações**: `Saque` e `Deposito` são classes de transações que herdam da classe abstrata `Transacao`. Elas possuem um método `registrar` que aplica a transação na conta e registra no histórico.
- **Histórico**: A classe `Historico` armazena todas as transações feitas na conta para exibição no extrato.
- **Menu Interativo**: O sistema possui um menu que permite ao usuário navegar pelas funcionalidades do sistema.

## Como Usar

1. **Criar um novo cliente**: Utilize a opção `[nu] Novo usuário` para adicionar um cliente ao sistema.
2. **Criar uma nova conta para o cliente**: Após criar o cliente, use a opção `[nc] Nova conta` para associar uma conta ao cliente recém-criado.
3. **Realizar depósitos e saques**: Com uma conta ativa, você pode usar `[d] Depositar` para adicionar saldo à conta ou `[s] Sacar` para retirar saldo.
4. **Consultar extrato**: Para visualizar o histórico de transações e o saldo da conta, use `[e] Extrato`.
5. **Listar todas as contas**: A opção `[lc] Listar Contas` permite visualizar todas as contas cadastradas no sistema.
6. **Sair do sistema**: Use `[q] Sair` para encerrar o sistema.

## Regras de Negócio

- Um cliente só pode ser criado se o CPF fornecido não estiver cadastrado previamente.
- Um cliente pode possuir várias contas, mas cada conta é associada a apenas um cliente.
- A conta corrente possui um limite para saques diários (padrão de 3 saques) e valor máximo por saque (padrão de R$ 500).
- O sistema mantém um histórico de todas as transações realizadas em uma conta.

## Exemplo de Uso

Ao iniciar o sistema, um menu será exibido com opções para criar clientes, contas, realizar transações e consultar extratos. O usuário interage digitando a letra correspondente à operação desejada.

### Fluxo de Criação de Cliente e Conta

1. **Criar Cliente**: Escolha `[nu]` e preencha os dados solicitados (CPF, nome, data de nascimento e endereço).
2. **Criar Conta**: Escolha `[nc]`, informe o CPF do cliente e uma nova conta será criada para ele.
3. **Realizar Transações**: Com a conta ativa, use `[d]` para depósitos e `[s]` para saques.

### Fluxo de Consulta de Extrato

1. Escolha `[e]` e informe o CPF do cliente para exibir o histórico de transações e saldo atual da conta.

## Requisitos

- Python 3.x

## Como Executar

Certifique-se de ter o Python instalado em sua máquina e execute o comando abaixo no terminal para iniciar o sistema:

```bash
python desafio3_pt2.py
```
