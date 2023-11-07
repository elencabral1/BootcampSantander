print('Exercício completo')

def mostrar_menu():
    print('Menu de operações')
    print('[A] Mostrar Saldo')
    print('[B] Efetuar depósito')
    print('[C] Efetuar Saque')
    print('[D] Finalizar')
    opcao_selecionada = input('Escolha uma opção: ')
    return opcao_selecionada

saldo = 0
encerrar_programa = False

while not encerrar_programa:
    opcao_selecionada = mostrar_menu()

    if opcao_selecionada == 'A':
        print('Seu saldo é', saldo)
    elif opcao_selecionada == 'B':
        valor = int(input('Digite o valor a depositar: '))
        saldo += valor
        print('Depósito efetuado')
    elif opcao_selecionada == 'C':
        valor = int(input('Digite o valor a retirar: '))
        if valor > saldo:
            print('Saque não permitido, saldo insuficiente')
        else:
            saldo -= valor
            print('Saque efetuado')
    elif opcao_selecionada == 'D':
        encerrar_programa = True
    else:
        print('Opção inválida, tente novamente')
