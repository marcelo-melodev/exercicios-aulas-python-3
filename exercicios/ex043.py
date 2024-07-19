import math
peso = float(input('Informe o peso da pessoa: (Kg)'))
altura = float(input('Informe o altura da pessoa: (m)'))
imc = peso / altura**2
if imc < 18.5:
    print(f'O IMC dessa pessoa é {imc:.2f}:')
    print('Você está abaixo do peso.')
elif imc == 18.5 <= 25:
    print(f' O IMC dessa pessoa é {imc:.2f}')
    print('Você está com o peso ideal.')
elif imc == 25 <= 30:
    print(f'O IMC dessa pessoa é {imc:.2f}:')
    print('Você está com sobre peso.')
elif imc == 30 <= 40:
    print(f'O IMC dessa pessoa é {imc:.2f}:')
    print('Você com obesidade.')
else:
    print(f'O IMC dessa pessoa é {imc:.2f}:')
    print('Você com OBESIDADE MORBIDA!')