#velo = float(input('Qual é a velocidade atual do carro?'))
#if velo > 80:
    #multa = (velo - 80)*7
    #print('Você excedeu a velocidade permitida que é de 80km/h')
    #print('A sua multa por excesso de de velocidade é de R$ {:.2f}'.format(multa))
#else:
    #print('Tenha um bom dia e boa viagem!')
refazendo os códigos
velo = float(input('Qual é a velocidade atual do caro?'))
if velo > 80:
    multa = (velo - 80)*7
    print('Você excedeu a velocidade permitida que éde 80 KM/h')
    print(f'A sua multa por excesso de velocidade é de R$ {multa:.2f}')
else:
    print('Tenha uma boa viagem!')