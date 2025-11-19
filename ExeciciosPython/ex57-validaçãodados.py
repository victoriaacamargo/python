s = str(input('Digite seu sexo: [M/F]')).upper().strip()[0]
while s not in 'MF':
    s = str(input('Dado inválido. Tente novamente:')).upper().strip()[0]
print('Obrigado pela informação!')

