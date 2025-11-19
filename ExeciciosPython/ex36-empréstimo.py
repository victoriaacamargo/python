casa = float(input('Qual o valor da casa que você quer comprar?'))
salario = float(input('Qual é o seu salário?'))
anos = int(input('Em quantos anos você quer pagar a casa?'))
ex = salario + (salario * 30/100)
p = salario / anos
if salario <= ex:
    print('Sua prestação mensal será de R${:.2f} para ser paga em até {} anos.'.format(p,anos))
elif salario > ex:
    print('Seu empréstimo foi negado!')
