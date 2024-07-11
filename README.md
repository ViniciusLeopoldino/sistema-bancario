# Sistema Bancário
Este projeto implementa um sistema bancário simples em Python, permitindo ao usuário realizar operações básicas como depósito, saque, exibição de extrato e reset diário de saques. O sistema foi desenvolvido como uma solução inicial para modernização das operações de um banco.

## Funcionalidades
* Depósito: Permite ao usuário depositar valores na conta.
* Saque: Permite ao usuário realizar até 3 saques diários com limite máximo de R$ 500,00 por saque.
* Extrato: Exibe todos os depósitos e saques realizados, além do saldo atual da conta.
* Novo Dia: Reseta o contador de saques diários, simulando a passagem de um dia.

## Como Executar
* Certifique-se de ter o Python instalado em sua máquina.
* Faça o download ou clone este repositório.
* Navegue até o diretório do projeto.
* Execute o script banco.py usando o comando:
> python banco.py

# Menu de Operações
Ao executar o script, você verá um menu com as seguintes opções:

> Menu:
> 1. Depositar
> 2. Sacar
> 3. Extrato
> 4. Novo Dia
> 5. Sair

# Exemplo de Uso

1. Depositar:

* Escolha a opção 1.
* Insira o valor a ser depositado.
* O valor será adicionado ao saldo da conta e registrado no extrato.

2. Sacar:

* Escolha a opção 2.
* Insira o valor a ser sacado.
* Se o valor for válido e dentro dos limites diários, ele será subtraído do saldo da conta e registrado no extrato.

3. Extrato:

* Escolha a opção 3.
* Veja a lista de todos os depósitos e saques realizados, bem como o saldo atual da conta.

4. Novo Dia:

* Escolha a opção 4.
* O contador de saques diários será resetado, permitindo novos saques no dia seguinte.

5. Sair:

* Escolha a opção 5 para encerrar o programa.

# Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Você pode abrir uma issue ou enviar um pull request com suas sugestões.
