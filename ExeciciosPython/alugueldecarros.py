d = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados?'))
pd = (60*d) + (km*0.15)
print('Total a pagar é de {:.2f}'.format(pd))


