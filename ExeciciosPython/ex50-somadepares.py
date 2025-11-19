soma = 0
for c in range (0,6):
    num1 = int(input('Digite um número inteiro:'))
    if num1 % 2 == 0:
        soma = soma + num1
print('A soma de todos os números pares é {}.'.format(soma))