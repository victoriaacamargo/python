carro = int(input('Qual a velocidade do carro?'))
m = (carro - 80) * 7
if carro <=80:
    print('Você está dentro do limite de velocidade.')
else:
    print('Você está acima do limite de velocidade e pagará uma multa de {} reais.'.format(m))