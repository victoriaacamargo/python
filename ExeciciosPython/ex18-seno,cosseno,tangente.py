import math

ang = int(input('Qual é o ângulo?'))
anguloradiano = math.radians(ang)
seno = math.sin(anguloradiano)
cos = math.cos(anguloradiano)
tang = math.tan(anguloradiano)
print('Se o ângulo é {:.2f}, então seu seno é {:.2f}, seu cosseno é {:.2f} e a sua tangente é {:.2f}.'.format(ang,seno, cos, tang))
