import random
adivinhe = str(input('Tente adivinhar o número escolhido pelo computador: '))
adivinhe = random.randint(0,5)
if adivinhe >= 5:
    print('Você venceu!')
else:
    print('Você perdeu!')