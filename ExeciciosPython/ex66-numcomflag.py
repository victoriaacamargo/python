num = soma = 0
valores = 0
while True:
  num = int(input('Digite um valor:'))
  if num == 999:
     break
  soma += num
  valores += 1
print(f'A soma dos {valores} valores é igual a {soma}!')