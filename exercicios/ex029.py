velo = float(input('Qual é a velocidade atual do carro?'))
if velo > 80:
    multa = (velo - 80)*7
    print('Você excedeu a velocidade permitida que é de 80km/h')
    print('A sua multa por excesso de de velocidade é de R$ {:.2f}'.format(multa))
else:
    print('Tenha um bom dia e boa viagem!')
