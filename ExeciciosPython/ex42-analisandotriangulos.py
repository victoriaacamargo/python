seg1 = float(input('Primeiro segmento:'))
seg2 = float(input('Segundo seguimento:'))
seg3 = float(input('Terceiro segmento:'))
if (seg1+seg2)>seg3 and (seg1+seg3)>seg2 and (seg2+seg3)>seg1:
    print('Os segmentos podem formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
     print('EQUILÁTERO.')
    if seg1 != seg2 !=seg3 != seg1:
     print('ESCALENO.')
    else:
     print('ISÓSCELES.')
else:
    print('Os segmentos não podem formar um triângulo.')