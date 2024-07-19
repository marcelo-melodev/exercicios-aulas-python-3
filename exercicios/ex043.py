peso = float(input('Informe o peso da pessoa:'))
altura = float(input('Informe a altura da pessoa:'))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'O imc da pessoa é de {imc:.1f}.')
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print(f'O imc da pessoa é de {imc:.1f}.')
    print('Você está no peso normal!')
elif imc >= 25 and imc <= 30:
    print(f'O imc da pessoa é de {imc:.1f}.')
    print('Vosê está com sobre peso!')
elif imc >= 30 and imc <= 40:
    print(f'O imc da pessoa é de {imc:.1f}.')
    print('Você está com Obesidade!')
else:
    print(f'o imc da pessoa é de {imc:.1f}.')
    print('Você está com Obesidade Morbida!') 



    

