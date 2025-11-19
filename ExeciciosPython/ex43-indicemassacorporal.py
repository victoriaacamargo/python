peso = float(input('Qual o seu peso? (Kg)'))
alt = float(input('Qual a sua altura? (m)'))
IMC = peso / (alt * alt)
if IMC < 18.5:
    print('Você está ABAIXO do peso ideal.')
elif IMC < 25:
    print('Você está com o peso IDEAL.')
elif IMC < 30:
    print('Você está com SOBREPESO.')
elif IMC < 40:
    print('Você está com OBESIDADE.')
elif IMC > 40:
    print('Você está com OBESIDADE MÓRBIDA.')