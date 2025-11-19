from datetime import date
atual = date.today().year
totmenor = 0
totmaior = 0
for p in range(1,8):
    nasc = int(input('Que a pessoa nasceu?'. format(p)))
    idade = atual - nasc
    if idade >= 21:
        totmenor += 1
    else:
        totmaior += 1
        print('Tivemos {} pessoas maiores de idade.'.format(totmaior))
        print('E também tivemos {} pessoas menores de idade.'.format(totmenor))
