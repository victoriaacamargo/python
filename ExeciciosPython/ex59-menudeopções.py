num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))
op1 = num1 + num2
op2 = num1*num2
op3 = num1 > num2 or num2 > num1
opção = 0
print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa')
print('>'*10)
while opção != 5:
    op = int(input('Qual é a sua opção:'))
    if op == 1:
        print('A soma entre {} e {} é igual a {}'.format(num1,num2,op1))
    elif op == 2:
        print('A multiplicação entre {} e {} é igual a {}.'.format(num1,num2,op2))
    elif op == 3:
        if num1>num2:
            maior = num1
        else:
            maior = num2
            print('Entre {} e {}, o maior valor é {}'.format(num1,num2,maior))
        print('')
    elif op == 4:
        print('Informe os novos números:')
        num1 = int(input('Primeiro valor:'))
        num2 = int(input('Segundo valor:'))
    elif op == 5:
        print('Finalizando...')
        import time
        time.sleep(2)
        print('Programa Finalizado. Volte sempre!')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-='*10)
