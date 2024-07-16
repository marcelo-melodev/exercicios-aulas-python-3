viagem = float(input('Digite quantos KM tem a sua viagem!'))
preço = viagem * 0.50
if viagem <= 200:
    print('Sua viagem possui {} KM e o valor da Passagem será R${:.2f}'.format(viagem,preço))
else:
    viagem >=200
    preço = viagem * 0.45
    print('Sua viagem possui {} KM e o valor da passagem será R$ {:.2f}'.format(viagem,preço))

