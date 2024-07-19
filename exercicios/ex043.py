import math
peso = float(input('Informe o peso da pessoa: (Kg)'))
altura = float(input('Informe o altura da pessoa: (m)'))
imc = peso / altura**2
if imc < 18.5:
    print(f'O IMC dessa pessoa é {imc:.2f}:')
    print('Você está abaixo do peso.')
elif imc == 18.5 < 25:
        print(f'Você está com o IMC de {imc:.2f}:')
        print('Seu peso está normal!')
elif imc == 25 < 30:
      print(f'Você está com o IMC de {imc:.2f}:')
      print('Você esta com sobrepeso!')
elif imc > 30 < 40:
      print(f'Você está com o IMC de {imc:.2f}.')
      print('Você esta com Obesidade!')
elif imc >= 40:
      print(f'Você esta com o ICM {imc:.2f}:')
      print('Você está com Obesidade Morbida!')

    

