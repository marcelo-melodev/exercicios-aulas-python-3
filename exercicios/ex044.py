import math
print('=========== Lojas Marcelo==========')
preço = float(input('Preço das compras: R$'))
print('Escolha a sua forma de pagamento!')
print('[1] á vista Dinheiro ou cheque:')
print('[2] á vista cartão de crédito:')
print('[3] 2x no cartão de crédito:')
print('[4] 3x ou mais no cartão de crédito:')
opção = input('Qual é a sua opção?')
if preço == 1:
    print('')