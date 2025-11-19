s = float(input('Qual é o salário do funcionário?'))
a1 = s+(s*10/100)
a2 = s+(s*15/100)
if s > 1250:
    print('Quem ganhava R${}, passará a ganhar R${}.'.format(s,a1))
else:
    print('Quem ganhava R${}, passará a ganhar R${}.'.format(s,a2))

