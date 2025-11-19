nome = str(input('DIgite seu nome completo:')).strip()
n = nome.split()
print('Muito prazer em te conhecer {}!'.format(nome))
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))

