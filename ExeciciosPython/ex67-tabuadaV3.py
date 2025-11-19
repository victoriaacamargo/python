while True:
  num = int(input('Digite um número para ver a tabuada:'))
  if num <0:
      break
  print('-' * 30)
  for c in range(1,11):
    print('{} x {} = {}.'.format(num,c,num*c))
  print('-' * 30)
print('Programa encerrado.Volte sempre!')
