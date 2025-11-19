from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    dif = idade-18
    print('Você ja deveria ter se alistado há {} anos.'.format(dif))
    ano = atual - dif
    print('Seu alistamento foi em {}.'.format(ano))