import math

co = int(input('Digite um número para o cateto oposto:'))
ca = int(input('Digite um número para o cateto adjacente:'))
hip = math.hypot(co,ca)
print('Se o cateto oposto é {} e o cateto adjacente é {}, então sua hipotenusa é igual a {:.2f}'.format(co,ca,hip))
