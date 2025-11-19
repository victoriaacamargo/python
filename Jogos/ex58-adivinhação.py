from random import randint
computador = randint(0,10)
print('Olá, sou seu computador... \nAcabei de pensar em um número de 0 a 10. \nConsegue adivinhar qual é? ')
acertou = False
palpites = 0
num = int(input('Qual é o seu palpite:'))
while not acertou:
    if num > computador:
        num = int(input('Menos... Tente novamente:'))
        palpites += 1
    if num < computador:
        num = int(input('Mais... Tente novamente:'))
        palpites += 1
    if num == computador:
        acertou = True
        palpites += 1


print('Acabou! Você acertou com {} tentativas.'.format(palpites))
