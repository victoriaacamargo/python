l = float(input('Qual é a largura da sua parede?'))
a = float(input('Qual é a altura da sua parede?'))
p = a*l
t = p/2
print('Você vai precisar de {:.1f} litros de tinta para pintar sua parede de {:.1f}lx{:.1f}a com área total de {:.1f}m'.format(t,l,a,p))