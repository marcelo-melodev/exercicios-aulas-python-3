import math
print('==========LOJA MARCELO==========')
preço= float(input('Informe o preço da compra:'))
print('Escolha a forma de pagamento!')
print('[1] Á vista Dinheiro ou Cheque:')
print('[2] Á vista cartão de crédito:')
print('[3] 2x No cartão de crédito:')
print('[4] 3x Ou mais no cartão de crédito:')
opção = int(input('Qual a sua opção?'))
if opção == 1:
    print(f'Sua compra de R${preço} vai custar R${preço*10//100 - preço}')
elif opção == 2:
    print(f'Sua compra de R${preço} vai custar R${preço*5//100 - preço}')
elif opção == 3:
    print(f'Sua compra de R${preço} vai custar R${preço}')
else:
    parcelas = int(input('Escolha a quantidade de parcelas:'))
    print(f'Sua compra parcelada em {parcelas}x de R${(preço*20/100 + preço) / parcelas} com juros')
    print(f'Sua compra de {preço} vai custar {preço*20/100 + preço} no final')