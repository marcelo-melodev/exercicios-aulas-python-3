casa = int(input('Digite o valor da casa:'))
s = int(input('Digite o Salário do comprador:'))
anos = int(input('Em quantos anos desejar pagar?'))
r = 12 * anos
prest = casa / r
orça1 = 30/100 - prest
#orça2 = prest - 30/100 * s
if prest > 30/100 * s:
    print('A casa de R${} parcelada em {} anos terá uma prestação de R${:.2f}. O valor ultrapassou 30% do seu Salário EMPRÉSTIMO NEGADO!'.format(casa,anos,prest))
#elif prest == s - 30/100:
    #print('A casa de R${} parcelada em {} anos terá uma prestação de R${:.2f}. EMPRÉSTIMO CONSEDIDO!'.format(casa,anos,prest))
else:
    #s >= prest * 30/100
    print('A casa de R${} parcelada em {} anos terá uma prestação de R${:.2f}. EMPRÉSTIMO CONSEDIDO!'.format(casa,anos,prest))
    