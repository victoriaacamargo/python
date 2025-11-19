km = int(input('Qual a distância você percorreu na viagem?'))
p = km * 0.50
pm = km * 0.45
if km <=200:
    print('O preço da sua passagem será igual a R${:.2f}.'.format(p))
else:
    print('O preço da sua passagem será igual a R${:.2f}.'.format(pm))

