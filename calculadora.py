

# Feita por Gallego-Dev
# Diogo Borges
while True:
    print(
        "\n=====================================\n"
        "  Calculadora de Múltiplas Operações\n"
        "  Autor: 🅶🅰🅻🅻🅴🅶🅾-🅳🅴🆅\n"
        "  Python | Projetos em Terminal\n"
        "====================================="
    )

    print('1 Soma')
    print('2 Subtração')
    print('3 Multiplicação')
    print('4 Divisão')
    print('5 Sair')
    try:
        opcao = int(input('\n        Qual a sua opcao: '))
    except ValueError:
        print('         ⚠️Digite um numero \n    Correspondente a uma operação!⚠️')
        continue
    print()
    if opcao == 1:
        try:
            num1 = int(input('Digite o primeiro numero: '))
        except ValueError:
            print('     Digite apenas \n        Numeros!')
            continue
        print()
        try:
            num2 = int(input('Digite o segundo numero: '))
        except ValueError:
            print('     Digite apenas \n        Numeros!')
            continue
        print()
        soma = num1 + num2
        print(f'\nO resultato da soma entre {num1} + {num2} = {soma}')
        print()
        ctnt1 = input('       Você Deseja continuar? \n               [S/N] ').strip().upper()
        if ctnt1 == 'S':
            continue

        elif ctnt1 == 'N':
            print("\nPrograma finalizado.")
            print("Desenvolvido por 🅶🅰🅻🅻🅴🅶🅾-🅳🅴🆅 | Python Dev Iniciante")
            break

    elif opcao == 2:
            try:
                num1 = int(input('Digite o primeiro numero: '))
            except ValueError:
                print('     Digite apenas \n        Numeros!')
                continue
            print()
            try:
                num2 = int(input('Digite o segundo numero: '))
            except ValueError:
                print('     Digite apenas \n        Numeros!')
                continue
            print()
            sub = num1 - num2
            print(f'\n O resultado da subtraçao entre {num1} - {num2} = {sub}')
            print()
            ctnt2 = input('       Você Deseja continuar? \n               [S/N] ').strip().upper()

            if ctnt2 == 'S':
                continue

            elif ctnt2 == 'N':
                print("\nPrograma finalizado.")
                print("Desenvolvido por 🅶🅰🅻🅻🅴🅶🅾-🅳🅴🆅 | Python Dev Iniciante")
                break

    elif opcao == 3:
            try:
                num1 = int(input('Digite o primeiro numero: '))
            except ValueError:
                print('     Digite apenas \n        Numeros!')
                continue
            print()
            try:
                num2 = int(input('Digite o segundo numero: '))
            except ValueError:
                print('     Digite apenas \n        Numeros!')
                continue
            print()
            mul = num1 * num2
            print(f'\n O resultado da multiplicação entre {num1} x {num2} = {mul}')
            print()
            ctnt3 = input('       Você Deseja continuar? \n               [S/N] ').strip().upper()

            if ctnt3 == 'S':
                continue

            elif ctnt3 == 'N':
                print("\nPrograma finalizado.")
                print("Desenvolvido por 🅶🅰🅻🅻🅴🅶🅾-🅳🅴🆅 | Python Dev Iniciante")
                break

    elif opcao == 4:
            try:
                num1 = int(input('Digite o primeiro numero: '))
            except ValueError:
                print('     Digite apenas \n        Numeros!')
                continue
            print()
            try:
                num2 = int(input('Digite o segundo numero: '))
                if num2 == 0:
                    print('⚠️ Não é possível dividir por zero')
                    continue
            except ValueError:
                print('     Digite apenas \n        Numeros!')
                continue
            print()
            div = num1 / num2
            print(f' O resultado da divisão entre {num1} ÷ {num2} = {div}')
            print()
            ctnt4 = input('       Você Deseja continuar? \n               [S/N] ').strip().upper()

            if ctnt4 == 'S':
                continue

            elif ctnt4 == 'N':
                print("\nPrograma finalizado.")
                print("Desenvolvido por 🅶🅰🅻🅻🅴🅶🅾-🅳🅴🆅 | Python Dev Iniciante")
                break

    elif opcao == 5:
        print('Programa finalizado.')
        break

    else:
        print()



