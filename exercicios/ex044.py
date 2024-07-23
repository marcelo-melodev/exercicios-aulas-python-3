import math
print('=========== Lojas Marcelo==========')
preço = float(input('Preço das compras: R$'))
print('Escolha a sua forma de pagamento!')
print('[1] á vista Dinheiro ou cheque:')
print('[2] á vista cartão de crédito:')
print('[3] 2x no cartão de crédito:')
print('[4] 3x ou mais no cartão de crédito:')
opção = int(input('Qual a sua opção?'))
if opção ==1:
    print(f'Sua compra de R${preço} vai custar R${preço*10//100 - preço}')
elif opção == 2:
    print(f'Sua compra de R${preço:.1f} vai custar R${preço*5//100 - preço}')
elif opção == 3:
    print(f'Sua compra de R${preço} vai custar R${preço}')
else:
   parcelas = int(input('Escolha a quantidade de parcelas'))
   print(f'Sua compra parcelada em {parcelas}x de R${(preço*20/100 + preço) / parcelas} com juros.')
   print(f'Sua compra de {preço} vai custar {preço*20/100 + preço} no final.')
